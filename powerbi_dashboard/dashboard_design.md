# Power BI Dashboard Design

This document outlines the layout and key metrics for the Customer Churn Dashboard.

## 1. Key Performance Indicators (KPIs)
- **Total Customers**: Count of all active and churned customers.
- **Churn Rate**: Percentage of customers who have churned.
- **Monthly Revenue**: Total monthly charges from all customers.
- **Revenue at Risk**: Monthly charges from customers identified as "High Risk".

## 2. Visualizations

### Churn by Contract
- **Type**: Donut Chart or Bar Chart
- **Dimension**: `Contract` (Month-to-month, One year, Two year)
- **Metric**: Churn Count

### Churn by Tenure
- **Type**: Stacked Bar Chart
- **Dimension**: `tenure_group`
- **Metric**: Count of Churn (Yes/No)

### Churn by Internet Service
- **Type**: Clustered Column Chart
- **Dimension**: `InternetService` (DSL, Fiber optic, No)
- **Metric**: Churn Count

### Customer Risk Segments
- **Type**: Treemap or Pie Chart
- **Dimension**: `risk_level` (High Risk, Medium Risk, Low Risk)
- **Metric**: Number of Customers

## 3. Data Sources
- `powerbi_customers.csv`: Main customer data.
- `powerbi_churn_metrics.csv`: Summary metrics.
- `powerbi_segments.csv`: Prediction results and risk levels.

## 4. Connection Instructions
1. Open Power BI Desktop.
2. Select **Get Data** -> **Text/CSV**.
3. Import the three CSV files from the `powerbi_dashboard/` folder.
4. (Optional) For MariaDB connection:
   - Go to **Get Data** -> **MySQL Database**.
   - Server: `localhost`, Database: `churn_db`.
   - Requires MySQL/MariaDB Connector/NET.
