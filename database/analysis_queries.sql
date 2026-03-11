-- Customer Churn Analysis Queries

-- 1. Overall Churn Rate
SELECT 
    Churn, 
    COUNT(*) AS customer_count, 
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM churn_status), 2) AS churn_percentage
FROM churn_status
GROUP BY Churn;

-- 2. Churn Rate by Contract Type
SELECT 
    b.Contract, 
    cs.Churn, 
    COUNT(*) as count
FROM billing b
JOIN churn_status cs ON b.customerID = cs.customerID
GROUP BY b.Contract, cs.Churn
ORDER BY b.Contract;

-- 3. Churn by Internet Service Type
SELECT 
    s.InternetService, 
    cs.Churn, 
    COUNT(*) as count
FROM services s
JOIN churn_status cs ON s.customerID = cs.customerID
GROUP BY s.InternetService, cs.Churn
ORDER BY count DESC;

-- 4. Churn by Tenure Group
SELECT 
    b.tenure_group, 
    cs.Churn, 
    COUNT(*) as count
FROM billing b
JOIN churn_status cs ON b.customerID = cs.customerID
GROUP BY b.tenure_group, cs.Churn
ORDER BY b.tenure_group;

-- 5. Average Revenue Lost from Churn
SELECT 
    ROUND(AVG(MonthlyCharges), 2) AS avg_monthly_loss_per_customer,
    ROUND(SUM(MonthlyCharges), 2) AS total_monthly_revenue_lost
FROM billing b
JOIN churn_status cs ON b.customerID = cs.customerID
WHERE cs.Churn = 'Yes';
