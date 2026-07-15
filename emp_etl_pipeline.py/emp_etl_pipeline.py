from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
import numpy as np

input_file = "/opt/airflow/data/emp_data.csv"
output_file ="/opt/airflow/data/cleaned_emp_data.csv"

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
    df['salary_category'] = np.where(df['salary'] >= 60000, 'High', 'Medium')

    df.to_csv(output_file, index=False)
    print("Transformation completed")

def load():
    df = pd.read_csv(output_file)
    print(df)

with DAG(
    dag_id='emp_pssql_csv',
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


