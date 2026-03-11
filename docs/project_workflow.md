# Project Workflow & Architecture

## Overview
The Customer Churn Analytics System follows a modular data pipeline architecture, moving data from raw formats to actionable business intelligence.

## Data Pipeline Stages

### 1. Data Ingestion & Cleaning
- **Input**: Raw Telco Churn CSV.
- **Process**: Python (`data_cleaning.py`) handles missing values, types, and feature engineering.
- **Output**: `cleaned_data.csv`.

### 2. Database Management
- **Schema**: Normalized SQL schema (`create_tables.sql`) prevents redundancy.
- **Loading**: Automated Python script (`import_data.py`) populates the MariaDB database.

### 3. Analysis & Modeling
- **EDA**: Visual exploration (`eda_analysis.py`) identifies trends and correlations.
- **Machine Learning**: Scikit-learn (`churn_prediction.py`) trains models to predict future churn.
- **Output**: Risk segments and probability scores.

### 4. Reporting & Visualization
- **Excel**: Automated business reports (`export_reports.py`) for offline stakeholders.
- **Power BI**: Dynamic dashboard datasets for executive decision-making.

## Tool Stack
- **Python**: Pandas, Scikit-learn, Seaborn, SQLAlchemy.
- **Database**: MariaDB.
- **Reporting**: Excel (Openpyxl), Power BI.
