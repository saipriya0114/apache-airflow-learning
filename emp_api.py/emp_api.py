from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime
from datetime import timedelta
import pandas as pd
import psycopg2



def extract():
    import requests 
    url ='https://dummyjson.com/users'
    response = requests.get(url)
    print(response.status_code)
    data = response.json()
    print(data.keys())
    print(data["users"][0])
    df =pd.DataFrame(data["users"])
    print(df.head())
    df.to_csv("/opt/airflow/data/raw_data.csv",index=False)

def transform():
    df = pd.read_csv("/opt/airflow/data/raw_data.csv")
    df = df.drop_duplicates()
    df = df.rename(columns={
    "firstName": "first_name",
    "lastName": "last_name"})
    df["full_name"] = df["first_name"] + " " + df["last_name"]
    df["age_group"] = df["age"].apply(lambda x: "senior" if x >= 60 else "adult" if x >= 30 else "young") 
    df = df[[
        "id",
        "first_name",
        "full_name",
        "last_name",
        "age",
        "age_group",
        "gender",
        "email"
    ]

    ]
    df.to_csv("/opt/airflow/data/transformed_data.csv", index=False)
    print("Transformation Completed")
def load():
    df = pd.read_csv("/opt/airflow/data/transformed_data.csv")
    conn = psycopg2.connect(
    host="postgres",
    database="airflow",
    user="airflow",
    password="airflow",
    port="5432"
)
# Create cursor
    cursor = conn.cursor()

    cursor.execute("DELETE FROM employee_api")

    # Insert each row into employee table
    for _, row in df.iterrows():

        cursor.execute(
            """
            INSERT INTO employee_api
            (id, first_name, last_name, full_name, age, age_group, gender, email)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
            """,
            (
                row["id"],
                row["first_name"],
                row["last_name"],
                row["full_name"],
                row["age"],
                row["age_group"],
                row["gender"],
                row["email"]
            )
        )

    # Save changes
    conn.commit()

    # Close connection
    cursor.close()
    conn.close()

    print("Data loaded into PostgreSQL successfully!")

with DAG(
    dag_id='api_pipeline',
    start_date=datetime(2026,7,15),
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




