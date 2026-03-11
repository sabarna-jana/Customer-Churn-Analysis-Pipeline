# Comprehensive Analytics Report: Customer Churn System

**Date:** March 11, 2026  
**Subject:** Full Lifecycle Analysis, Predictive Modeling, and Strategic Recommendations  
**Prepared for:** Executive Leadership / Senior Stakeholders  

---

## 1. Executive Summary
This report details the findings of the Customer Churn Analytics System. Our analysis covered **7,043 customers**, revealing a **churn rate of 26.54%**. The financial impact is significant, with **$139,130 in monthly revenue lost** due to churn. However, our predictive model has successfully identified a "High Risk" segment containing **1,361 customers** accounting for **$103,658 in monthly revenue**, presenting a clear opportunity for targeted retention.

---

## 2. Methodology & Data Integrity
### 2.1 Data Collection
- **Source:** Telco Customer Churn dataset.
- **Scope:** 20+ features including demographics, account information, and service usage.

### 2.2 Data Cleaning & Transformation
- **Sanitization:** Handled 11 missing values in `TotalCharges` (imputed with 0 for new customers).
- **Normalization:** Converted categorical strings to structured types.
- **Feature Engineering:** 
  - `Tenure Group`: Segmented customers into lifecycle stages (e.g., 0-12 months, 1-2 years).
  - `CLV (Customer Lifetime Value)`: Calculated as `MonthlyCharges * Tenure` to prioritize high-value retention.

### 2.3 Database Management
- Data was ingested into a **Normalized MariaDB Schema** to ensure data integrity and facilitate SQL-based business intelligence.

---

## 3. Exploratory Data Analysis (EDA) Highlights
### 3.1 Churn by Contract Type
- **Finding:** Month-to-month customers have a churn rate exceeding **40%**, while two-year contract holders churn at less than **3%**.
- **Impact:** Long-term contracts are the primary stabilizer for recurring revenue.

### 3.2 Service Performance
- **Fiber Optic Segment:** Despite being a premium service, Fiber Optic users exhibit higher churn rates than DSL users. 
- **Recommendation:** Technical audit of Fiber Optic service quality and a competitive pricing review are required.

### 3.3 Value-Added Services
- Customers with **Tech Support** and **Online Security** show significantly higher retention rates. 
- **Strategy:** "Stickiness" is achieved through service bundling rather than core connectivity alone.

---

## 4. Predictive Modeling & AI Results
### 4.1 Model Performance
We deployed a **Random Forest Classifier** and **Logistic Regression** pipeline:
- **Accuracy:** 81.5%
- **Recall (Churn):** Balanced to prioritize identifying at-risk customers (Minimizing False Negatives).
- **ROC-AUC:** 0.84 (Indicates strong discriminative power between churn and non-churn).

### 4.2 Risk Segmentation
Based on model probabilities, we categorized the customer base:
- **High Risk (>70% prob):** 1,361 customers (Priority 1)
- **Medium Risk (30-70% prob):** 1,840 customers (Priority 2)
- **Low Risk (<30% prob):** 3,842 customers (Watchlist)

---

## 5. Financial Impact Analysis
| Metric | Value |
|--------|-------|
| Total Monthly Revenue | $456,116.60 |
| Realized Revenue Loss (Churned) | $139,130.85 |
| **At-Risk Monthly Revenue (High Risk Segment)** | **$103,658.80** |

**Business Case for AI:** Retaining just **15%** of the High Risk segment through targeted outreach would save over **$15,500 per month** ($186,000 annually).

---

## 6. Strategic Recommendations
1.  **Retention Campaigns:** Launch immediate "Save" offers for the 1,361 High-Risk customers identified by the model.
2.  **Contract Migration:** Incentive Month-to-Month users to move to 1-Year plans via a "One Month Free" promotion.
3.  **Support Bundling:** Offer 3 months of free "Tech Support" to new Fiber Optic customers to improve early-lifecycle retention.
4.  **Premium Care:** Assign Customer Success Managers to the "High Value / High Risk" cluster to protect top-tier revenue.

---

**End of Report**
