from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
import numpy as np
import psycopg2


input_file = "/opt/airflow/data/employee_data.csv"
output_file ="/opt/airflow/data/cleaned_employee_data.csv"

def extract():
    df = pd.read_csv(input_file)
    print(df.head())

def transform():
    df=pd.read_csv(input_file)
    df=df.drop_duplicates()

    df['name'] = df['name'].str.upper()
    df['bonus'] = df['salary'] *0.1
    df['tax'] = df['salary'] * 0.05
    df['net_salary'] = df['salary'] - df['tax']
    df['net_salary'] = df['net_salary'].str.lower()
    df['salary_category'] = np.where(df['salary'] >= 60000, 'High', 'Medium')
    df['annual_salary'] = df['salary'] * 12

    df.to_csv(output_file, index=False)
    print("Transformation completed")

def load():

    # Read transformed CSV
    df = pd.read_csv(output_file)

    # Connect to PostgreSQL
    conn = psycopg2.connect(
        host="postgres",
        database="airflow",
        user="airflow",
        password="airflow",
        port="5432"
    )

    # Create cursor
    cursor = conn.cursor()

    # Insert each row into employee table
    for _, row in df.iterrows():

        cursor.execute(
            """
            INSERT INTO employee
            (employee_id, name, department, salary, bonus, tax, net_salary, salary_category)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
            """,
            (
                row["employee_id"],
                row["name"],
                row["department"],
                row["salary"],
                row["bonus"],
                row["tax"],
                row["net_salary"],
                row["salary_category"]
            )
        )

    # Save changes
    conn.commit()

    # Close connection
    cursor.close()
    conn.close()

    print("Data loaded into PostgreSQL successfully!")

with DAG(
    dag_id='emp_etl_pipeline',
    start_date=datetime(2026,6,22),
    schedule='@daily',
    catchup =  False
) as dag:
    extract_task = PythonOperator(
        task_id ='extract',
        python_callable=extract
    )
    transform_task = PythonOperator(
        task_id='transform',
        python_callable=transform
    )
    load_task = PythonOperator(
        task_id='load',
        python_callable=load
    )

    extract_task >> transform_task >> load_task



