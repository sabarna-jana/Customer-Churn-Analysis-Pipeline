# 📊 Customer Churn Analytics System

[![Python](https://img.shields.io/badge/Python-3.9+-3776ab?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![MariaDB](https://img.shields.io/badge/MariaDB-003545?style=for-the-badge&logo=mariadb&logoColor=white)](https://mariadb.org)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)

An end-to-end, enterprise-grade analytical system designed to predict and mitigate customer churn. This project demonstrates a complete data lifecycle—from raw ingestion and SQL normalization to AI-driven risk segmentation and executive dashboarding.

---

## 🚀 Executive Dashboards (Visual Showcase)

### 1. Business Intelligence Dashboard
*A high-impact interface for stakeholders, focusing on Revenue at Risk and strategic recovery.*
![Analysis Dashboard](docs/screenshots/analysis_dashboard.png)

### 2. Technical Engineering Showcase
*Detailed documentation for technical interviewers, highlighting the ML pipeline and data architecture.*
![Technical Showcase](docs/screenshots/technical_showcase.png)

---

## 💡 Why This Project Stands Out

- **Metric-Driven Outcomes**: Identifies over **$103k in monthly revenue at high risk**, providing a direct ROI-focused business case.
- **AI-Driven Action Plan**: Prioritizes the customer base into High, Medium, and Low risk segments.
- **Modular Data Engineering**: Built with a "Clean Architecture" approach, separating concerns into ETL, Inference, and Reporting.
- **Full-Stack Proficiency**: Spans the entire stack from Python/SQL to HTML/CSS Design and Power BI planning.

---

## 🛠 Project Architecture & Implementation

The system follows a 4-stage automated pipeline:

### 1. Data Ingestion & Cleaning (`data_cleaning.py`)
Implemented robust preprocessing to handle real-world data issues.
```python
# Strategic Feature Engineering Example
df['tenure_group'] = pd.cut(df['tenure'], bins=[0, 12, 24, 48, 72], 
                            labels=['0-1yr', '1-2yr', '2-4yr', '4-6yr'])
df['customer_lifetime_value'] = df['MonthlyCharges'] * df['tenure']
```

### 2. Normalized Database Design (`create_tables.sql`)
Demonstrates database proficiency through a 3NF normalized schema across four primary tables.

### 3. AI Predictive Modeling (`churn_prediction.py`)
Utilizes a Random Forest classifier to predict churn probability.
```python
# Churn Risk Segmentation Logic
probability = model.predict_proba(X_test)[:, 1]
segments = pd.cut(probability, bins=[0, 0.3, 0.7, 1.0], 
                 labels=['Low Risk', 'Medium Risk', 'High Risk'])
```

### 4. Professional Reporting Suite (`export_reports.py`)
Automates multi-sheet Excel workbooks and Power BI ready datasets for business stakeholders.

---

## ⚙️ How to Run the Project

### Prerequisites
- Python 3.9+
- MariaDB (Optional for the pipeline, required for the DB export stage)

### Quick Setup

1. **Activate Environment**:
   ```bash
   source .venv/bin/activate
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Execute the Master Pipeline**:
   ```bash
   python run_pipeline.py
   ```

### 🖥 The "WOW" Factor
Upon completion, the script will **automatically launch two premium HTML reports** in your browser, providing an instant visual overview of your results.

---

## 📁 Repository Structure
```text
Customer_Churn_Analytics/
├── data/               # Raw and Processed Datasets
├── database/           # SQL Scripts & DB Ingestion
├── python_analysis/    # Modular Python Scripts
├── excel_reports/      # Automated Business Workbooks
├── docs/               # Visuals, Insights, & Guides
├── run_pipeline.py     # Master Pipeline Orchestrator
└── README.md           # Project Documentation
```

This project is created by Sabarna Jana| Customer Churn Analytics System
