# Employee API Data Pipeline using Apache Airflow

## Project Overview

This project demonstrates how to build an automated data pipeline using Apache Airflow that extracts employee data from an API, processes the data, and stores it for further analysis.

The project showcases API integration, workflow orchestration, and task automation, which are essential skills for Data Engineering.

---

## Project Objective

- Extract employee data from a REST API
- Process and validate the retrieved data
- Store the data for downstream use
- Automate the workflow using Apache Airflow

---

## Technologies Used

- Apache Airflow
- Python
- Requests Library
- JSON
- Docker

---

## Workflow

```text
Employee API
      ↓
Extract Data
      ↓
Validate Data
      ↓
Process Data
      ↓
Store Output
```

---

## Airflow Concepts Used

- DAG (Directed Acyclic Graph)
- PythonOperator
- Task Dependencies
- Scheduling
- Logging
- Error Handling

---

## Project Structure

```text
emp_api.py
README.md
```

---

## Pipeline Steps

### 1. Extract

- Connect to the Employee API
- Send HTTP request
- Retrieve employee records in JSON format

### 2. Validate

- Check API response status
- Verify data availability
- Handle missing or invalid records

### 3. Process

- Parse JSON response
- Extract required employee fields
- Format data for downstream systems

### 4. Store

- Save processed data to file/database
- Generate logs for monitoring

---

## Sample API Response

```json
{
  "id": 101,
  "name": "John Doe",
  "department": "IT",
  "salary": 50000
}
```

---

## How to Run

### Start Airflow

```bash
docker compose up -d
```

### Verify DAG

```bash
airflow dags list
```

### Trigger Pipeline

```bash
airflow dags trigger emp_api
```

---

## Expected Outcome

- Employee data successfully fetched from API
- Data processed and validated
- Workflow completed successfully
- Execution visible in Airflow UI

---

## Skills Demonstrated

- API Integration
- Data Extraction
- Workflow Orchestration
- Python Automation
- Airflow DAG Development
- JSON Data Processing

---

## Learning Outcomes

Through this project, I learned:

- How to connect to APIs using Python
- How to process JSON data
- How to automate API workflows using Airflow
- How to manage task execution and monitoring

---

## Future Enhancements

- Load API data into PostgreSQL
- Store data in AWS S3
- Add data quality checks
- Implement alert notifications
- Schedule incremental data loads

---

## Author

**Saipriya Bagadi**

Aspiring Data Engineer | Apache Airflow Learning Journey
