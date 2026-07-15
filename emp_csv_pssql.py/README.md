# Employee CSV to PostgreSQL ETL Pipeline

## Project Overview

This project demonstrates an ETL (Extract, Transform, Load) pipeline using Apache Airflow that reads employee data from a CSV file and loads it into a PostgreSQL database.

The workflow automates the movement of data from flat files into a relational database, which is a common requirement in Data Engineering.

---

## Project Objective

- Extract employee data from a CSV file
- Transform and validate the data
- Load the processed data into PostgreSQL
- Automate the workflow using Apache Airflow

---

## Technologies Used

- Apache Airflow
- Python
- Pandas
- PostgreSQL
- Docker

---

## Workflow

```text
Employee CSV File
        ↓
Extract Data
        ↓
Transform Data
        ↓
Load into PostgreSQL
        ↓
Pipeline Success
```

---

## Airflow Concepts Used

- DAG (Directed Acyclic Graph)
- PythonOperator
- Task Dependencies
- Scheduling
- Logging


---

## Project Structure

```text
emp_csv_pssql.py
data/
├── employees.csv

README.md
```

---

## ETL Process

### Extract

- Read employee data from a CSV file
- Validate file availability

### Transform

- Handle missing values
- Standardize data formats
- Remove duplicate records (if applicable)

### Load

- Connect to PostgreSQL
- Insert employee records into database tables
- Verify successful data load

---

## Database Target

Example Employee Table:

| Column |
|----------|
| employee_id |
| employee_name |
| department |
| salary |


---

## How to Run

### Start Airflow Services

```bash
docker compose up -d
```

### Verify DAG Availability

```bash
airflow dags list
```

### Trigger Pipeline

```bash
airflow dags trigger emp_csv_pssql
```

---

## Expected Outcome

- Employee records are successfully read from CSV
- Data is transformed and validated
- Records are inserted into PostgreSQL
- Airflow UI shows successful DAG execution

---

## Skills Demonstrated

- ETL Pipeline Development
- Apache Airflow Workflow Orchestration
- PostgreSQL Integration
- Data Loading Automation
- Python for Data Engineering

---

## Future Enhancements

- Incremental Data Loading
- Data Quality Checks
- Error Handling and Alerts
- AWS S3 Integration
- Dynamic File Processing

---

## Learning Outcomes

Through this project, I learned:

- Building ETL pipelines with Apache Airflow
- Reading and processing CSV files using Python
- Loading data into PostgreSQL databases
- Managing workflow dependencies and automation

---

## Author

**Saipriya Bagadi**

Aspiring Data Engineer | Apache Airflow Learning Journey
