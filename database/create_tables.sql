-- Customer Churn Database Schema
-- Database: churn_db

-- Table 1: customers
CREATE TABLE IF NOT EXISTS customers (
    customerID VARCHAR(20) PRIMARY KEY,
    gender VARCHAR(10),
    SeniorCitizen INT,
    Partner VARCHAR(5),
    Dependents VARCHAR(5)
);

-- Table 2: services
CREATE TABLE IF NOT EXISTS services (
    customerID VARCHAR(20),
    tenure INT,
    PhoneService VARCHAR(5),
    MultipleLines VARCHAR(20),
    InternetService VARCHAR(20),
    OnlineSecurity VARCHAR(20),
    OnlineBackup VARCHAR(20),
    DeviceProtection VARCHAR(20),
    TechSupport VARCHAR(20),
    StreamingTV VARCHAR(20),
    StreamingMovies VARCHAR(20),
    FOREIGN KEY (customerID) REFERENCES customers(customerID)
);

-- Table 3: billing
CREATE TABLE IF NOT EXISTS billing (
    customerID VARCHAR(20),
    Contract VARCHAR(20),
    PaperlessBilling VARCHAR(5),
    PaymentMethod VARCHAR(30),
    MonthlyCharges DECIMAL(10, 2),
    TotalCharges DECIMAL(10, 2),
    tenure_group VARCHAR(20),
    monthly_revenue_segment VARCHAR(10),
    customer_lifetime_value DECIMAL(12, 2),
    FOREIGN KEY (customerID) REFERENCES customers(customerID)
);

-- Table 4: churn_status
CREATE TABLE IF NOT EXISTS churn_status (
    customerID VARCHAR(20),
    Churn VARCHAR(5),
    FOREIGN KEY (customerID) REFERENCES customers(customerID)
);
