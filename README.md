# ✈️ Flight Operations Analytics Pipeline

An end-to-end data engineering project that integrates historical **US flight operations** and **weather observations** into a PostgreSQL data warehouse. The pipeline performs data ingestion, cleansing, transformation, dimensional modeling, and analytical querying to enable insights into airline performance, airport operations, delays, and weather impact.

---

## Architecture

```text
Flight Data (CSV)      Weather Data (CSV)
        │                     │
        └──────────┬──────────┘
                   ▼
          Data Ingestion (Python)
                   ▼
      Data Cleaning & Validation
                   ▼
     Spark Transformations (PySpark)
                   ▼
      PostgreSQL Staging Tables
                   ▼
      Star Schema Data Warehouse
                   ▼
         Analytical SQL Queries
```

---

## Tech Stack

- **Python**
- **PySpark**
- **Pandas**
- **NumPy**
- **PostgreSQL**
- **Docker**
- **SQL**
- **Git & GitHub**

---

## Dataset

This project combines two historical datasets:

### Flight Dataset
- Carrier information
- Flight number
- Origin & destination airports
- Departure & arrival delays
- Scheduled flight duration
- Cancellation codes

### Weather Dataset
- Temperature
- Visibility
- Wind speed
- Atmospheric pressure
- Precipitation

The datasets are merged to analyze how weather conditions influence flight operations.

---

## ETL Pipeline

- Extract raw flight and weather datasets
- Clean and validate records
- Handle missing values and duplicates
- Transform data using PySpark
- Load curated data into PostgreSQL
- Build a Star Schema for analytics

---

## Data Warehouse

### Dimension Tables

- `dim_airport`
- `dim_carrier`
- `dim_date`

### Fact Table

- `fact_flights`

---

## Business Analytics

The warehouse supports analysis such as:

- Airport traffic and flight volume
- Airline on-time performance
- Flight delay analysis
- Weather impact on delays
- Flight cancellation trends
- Monthly and yearly operational trends

---


---

## Skills Demonstrated

- ETL Pipeline Development
- Data Cleaning & Validation
- PySpark Data Processing
- PostgreSQL Data Warehousing
- Star Schema Design
- Analytical SQL
- Dockerized Development
