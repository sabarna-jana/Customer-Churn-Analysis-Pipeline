import pandas as pd
import numpy as np
import os

def clean_data(input_path, output_path):
    """
    Loads, cleans, and processes the Telco Customer Churn dataset.
    """
    print(f"Loading data from {input_path}...")
    if not os.path.exists(input_path):
        print(f"Error: File {input_path} not found.")
        return

    # Load dataset
    df = pd.read_csv(input_path)

    # 1. Remove duplicates
    initial_shape = df.shape
    df.drop_duplicates(inplace=True)
    if df.shape != initial_shape:
        print(f"Removed {initial_shape[0] - df.shape[0]} duplicate rows.")

    # 2. Convert TotalCharges to numeric
    # TotalCharges contains empty strings for new customers (tenure=0)
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

    # 3. Fill missing values
    # TotalCharges missing where tenure is 0, fill with 0
    df['TotalCharges'] = df['TotalCharges'].fillna(0)

    # 4. Create new features
    # Tenure Group
    def map_tenure(tenure):
        if tenure <= 12:
            return '0-12 Months'
        elif tenure <= 24:
            return '1-2 Years'
        elif tenure <= 36:
            return '2-3 Years'
        elif tenure <= 48:
            return '3-4 Years'
        elif tenure <= 60:
            return '4-5 Years'
        else:
            return 'Over 5 Years'

    df['tenure_group'] = df['tenure'].apply(map_tenure)

    # Monthly Revenue Segment
    # Divide into 3 segments based on MonthlyCharges
    df['monthly_revenue_segment'] = pd.qcut(df['MonthlyCharges'], 3, labels=['Low', 'Medium', 'High'])

    # Customer Lifetime Value (Simplified: MonthlyCharges * tenure)
    # This represents historical revenue generated from the customer
    df['customer_lifetime_value'] = df['MonthlyCharges'] * df['tenure']

    # 5. Save the cleaned dataset
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Cleaned data saved to {output_path}")
    print(f"Final dataset shape: {df.shape}")

if __name__ == "__main__":
    RAW_DATA_PATH = "data/raw/telco_churn.csv"
    PROCESSED_DATA_PATH = "data/processed/cleaned_data.csv"
    
    clean_data(RAW_DATA_PATH, PROCESSED_DATA_PATH)
