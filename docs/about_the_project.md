## 1. Project Motivation ("Why this project?")
*   **The Business Problem:** Churn is the "silent killer" of recurring revenue businesses. Reducing churn by just 5% can increase profits by 25-95%.
*   **The Solution:** A data-driven system that moves beyond reactionary reporting to **proactive risk segmentation** using Machine Learning.

---

## 2. Technical Architecture ("How is it built?")

### A. Modular Pipeline Design
*   **Talking Point:** "I built the system using a **modular architecture**. Instead of one giant script, I separated concerns into Cleaning, EDA, Modeling, and Reporting modules. This makes the code professionally maintainable, testable, and scalable."
*   **Deep Dive:** The `run_pipeline.py` serves as an **orchestrator**, managing dependencies between stages and providing a consolidated output.

### B. Normalized Database Schema
*   **Talking Point:** "I implemented a **normalized MariaDB schema** (3NF principles) with 4 tables: `customers`, `services`, `billing`, and `churn_status`. This prevents data redundancy and ensures referential integrity through Foreign Keys."
*   **Why it impresses:** Shows you understand relational database design, not just flat files.

### C. Feature Engineering (The "Secret Sauce")
*   **Talking Point:** "I didn't just use raw data. I engineered features like `tenure_group` to capture non-linear trends and `Monthly Revenue Segment` to identify high-value/high-risk clusters."
*   **Metric Highlight:** "I calculated **Revenue at Risk**, which tells the business exactly how many dollars are on the line, shifting the conversation from 'percent churn' to 'financial impact'."

### D. Machine Learning Logic
*   **Talking Point:** "I compared Logistic Regression and Random Forest. Logistic Regression provided ~82% accuracy with high interpretability, which is crucial for business stakeholders to understand *why* a customer is at risk."
*   **Risk Segmentation:** Explain the **Risk Levels (High/Medium/Low)** logic. It's not just a 0 or 1; it's a probability-based bucket that the marketing team can actually use for targeting.

---

## 3. Business Value & ROI ("Tell me about the impact.")

*   **Proactive vs. Reactive:** "Most companies only know a customer has left *after* they cancel. My system identifies 'High Risk' customers (Probability > 70%) before they churn, allowing for immediate retention campaigns."
*   **Quantified Impact:** "Based on the analysis, we identified **$103k in monthly revenue at high risk**. If we retain just 20% of that segment, the system generates over **$20k in monthly ROI**."
*   **Communication:** "Stakeholders don't read CSVs. I automated **Excel Reports** for offline analysis and an **HTML Dashboard** for instant visual insights."

---

## 4. Tough Interview Questions & Answers

**Q: How did you handle missing data?**
*   **A:** I identified that `TotalCharges` was missing for new customers (tenure=0). I didn't delete them; I imputed the value with 0 because they hadn't been billed yet. This preserved the integrity of the 'new customer' segment.

**Q: Why use Python for cleaning if you have SQL?**
*   **A:** Python offers superior flexibility for complex feature engineering (like qcut for segments) and integrates seamlessly with the Machine Learning libraries used in later stages.

**Q: What would you improve if you had more time?**
*   **A:** I would implement **Cross-Validation** to ensure model robustness and explore **SHAP values** to provide granular explanations for why individual customers were flagged as high risk.
