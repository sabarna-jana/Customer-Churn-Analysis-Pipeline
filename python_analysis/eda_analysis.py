import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

def run_eda(csv_path, output_dir):
    """
    Performs Exploratory Data Analysis and saves visualizations.
    """
    print(f"Loading data for EDA from {csv_path}...")
    df = pd.read_csv(csv_path)

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Use a professional style
    sns.set_theme(style="whitegrid")
    
    # 1. Churn Distribution
    plt.figure(figsize=(8, 6))
    sns.countplot(x='Churn', data=df, palette='viridis')
    plt.title('Customer Churn Distribution')
    plt.savefig(os.path.join(output_dir, 'churn_distribution.png'))
    plt.close()

    # 2. Churn by Contract Type
    plt.figure(figsize=(10, 6))
    sns.countplot(x='Contract', hue='Churn', data=df, palette='magma')
    plt.title('Churn by Contract Type')
    plt.savefig(os.path.join(output_dir, 'churn_by_contract.png'))
    plt.close()

    # 3. Churn by Tenure Group
    plt.figure(figsize=(12, 6))
    # Order the tenure groups for better visualization
    tenure_order = ['0-12 Months', '1-2 Years', '2-3 Years', '3-4 Years', '4-5 Years', 'Over 5 Years']
    sns.countplot(x='tenure_group', hue='Churn', data=df, palette='coolwarm', order=tenure_order)
    plt.title('Churn by Tenure Group')
    plt.savefig(os.path.join(output_dir, 'churn_by_tenure.png'))
    plt.close()

    # 4. Churn vs Monthly Charges
    plt.figure(figsize=(10, 6))
    sns.kdeplot(df[df['Churn'] == 'No']['MonthlyCharges'], fill=True, label='No Churn', color='blue')
    sns.kdeplot(df[df['Churn'] == 'Yes']['MonthlyCharges'], fill=True, label='Churn', color='red')
    plt.title('Monthly Charges Distribution by Churn')
    plt.legend()
    plt.savefig(os.path.join(output_dir, 'churn_vs_monthly_charges.png'))
    plt.close()

    # 5. Customer Lifetime Value Distribution
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Churn', y='customer_lifetime_value', data=df, palette='Set2')
    plt.title('Customer Lifetime Value by Churn')
    plt.savefig(os.path.join(output_dir, 'clv_distribution.png'))
    plt.close()

    print(f"EDA charts saved to {output_dir}")

if __name__ == "__main__":
    PROCESSED_DATA_PATH = "data/processed/cleaned_data.csv"
    OUTPUT_DIR = "python_analysis/plots"
    
    run_eda(PROCESSED_DATA_PATH, OUTPUT_DIR)
