import pandas as pd
from sqlalchemy import create_engine
import os

def import_to_mariadb(csv_path, db_config):
    """
    Imports cleaned customer churn data into normalized MariaDB tables.
    """
    print(f"Reading cleaned data from {csv_path}...")
    df = pd.read_csv(csv_path)

    # Database connection string
    # Replace with actual credentials if needed
    conn_str = f"mysql+pymysql://{db_config['user']}:{db_config['password']}@{db_config['host']}/{db_config['database']}"
    
    try:
        engine = create_engine(conn_str)
        print("Connected to MariaDB successfully.")

        # 1. Customers Table
        customers_df = df[['customerID', 'gender', 'SeniorCitizen', 'Partner', 'Dependents']]
        customers_df.to_sql('customers', con=engine, if_exists='append', index=False)
        print("Inserted data into 'customers' table.")

        # 2. Services Table
        services_df = df[['customerID', 'tenure', 'PhoneService', 'MultipleLines', 'InternetService', 
                          'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 
                          'StreamingTV', 'StreamingMovies']]
        services_df.to_sql('services', con=engine, if_exists='append', index=False)
        print("Inserted data into 'services' table.")

        # 3. Billing Table
        billing_df = df[['customerID', 'Contract', 'PaperlessBilling', 'PaymentMethod', 
                         'MonthlyCharges', 'TotalCharges', 'tenure_group', 
                         'monthly_revenue_segment', 'customer_lifetime_value']]
        billing_df.to_sql('billing', con=engine, if_exists='append', index=False)
        print("Inserted data into 'billing' table.")

        # 4. Churn Status Table
        churn_df = df[['customerID', 'Churn']]
        churn_df.to_sql('churn_status', con=engine, if_exists='append', index=False)
        print("Inserted data into 'churn_status' table.")

        print("Data import completed successfully!")

    except Exception as e:
        print(f"Error during data import: {e}")

if __name__ == "__main__":
    PROCESSED_DATA_PATH = "data/processed/cleaned_data.csv"
    
    # Default configuration for MariaDB
    # User should update these credentials based on their local setup
    DB_CONFIG = {
        'host': 'localhost',
        'database': 'churn_db',
        'user': 'root',
        'password': '' # Add your password here
    }
    
    import_to_mariadb(PROCESSED_DATA_PATH, DB_CONFIG)
