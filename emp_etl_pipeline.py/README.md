# Employee ETL Pipeline using Apache Airflow

## Project Overview

This project demonstrates an End-to-End ETL (Extract, Transform, Load) pipeline built using Apache Airflow.

The pipeline extracts employee data from a source, performs basic transformations, and loads the processed data into the target system.

## Objectives

- Automate data processing using Apache Airflow
- Understand ETL workflow design
- Practice task dependencies in Airflow
- Learn data extraction, transformation, and loading concepts

## Technologies Used

- Apache Airflow
- Python
- Pandas
- Docker

## Workflow

```text
Extract Employee Data
          ↓
Transform Data
          ↓
Load Data into Target Database/File
```

## DAG Structure

| Task | Description |
|--------|------------|
| Extract | Retrieves employee data from source |
| Transform | Cleans and processes employee data |
| Load | Loads transformed data into destination |

## Project Files

```text
emp_etl_pipeline.py
README.md
```

## Airflow Concepts Used

- DAGs
- PythonOperator
- Task Dependencies
- Scheduling
- Logging

## How to Run

### Start Airflow

```bash
docker compose up -d
```

### Verify DAG

```bash
airflow dags list
```

### Trigger DAG

```bash
airflow dags trigger emp_etl_pipeline
```

## Sample Output

- Employee data extracted successfully
- Data transformed successfully
- Data loaded successfully

## Learning Outcomes

After completing this project, I learned:

- How ETL pipelines work
- How to build workflows using Airflow
- How task dependencies are managed
- How to automate data processing pipelines

## Future Improvements

- Add API-based extraction
- Load data into PostgreSQL
- Store data in AWS S3
- Implement monitoring and alerts
- Add data quality checks

## Author

**Saipriya Bagadi**

Aspiring Data Engineer
