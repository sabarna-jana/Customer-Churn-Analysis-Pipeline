import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, roc_auc_score
from sklearn.preprocessing import LabelEncoder
import os

def train_and_predict(csv_path, output_csv_path):
    """
    Trains churn prediction models and generates risk level assessments.
    """
    print(f"Loading data for modeling from {csv_path}...")
    df = pd.read_csv(csv_path)

    # 1. Preprocessing
    # Drop customerID for training but keep it for final output
    customer_ids = df['customerID']
    X = df.drop(['customerID', 'Churn', 'tenure_group', 'monthly_revenue_segment'], axis=1)
    y = df['Churn'].apply(lambda x: 1 if x == 'Yes' else 0)

    # Convert categorical variables to dummy variables (One-Hot Encoding)
    # This is more robust than LabelEncoder for feature variables
    X = pd.get_dummies(X, drop_first=True)

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 2. Logistic Regression
    lr_model = LogisticRegression(max_iter=1000)
    lr_model.fit(X_train, y_train)
    lr_preds = lr_model.predict(X_test)
    lr_acc = accuracy_score(y_test, lr_preds)
    lr_auc = roc_auc_score(y_test, lr_model.predict_proba(X_test)[:, 1])

    print("\nLogistic Regression Results:")
    print(f"Accuracy: {lr_acc:.4f}")
    print(f"ROC AUC: {lr_auc:.4f}")

    # 3. Random Forest
    rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_model.fit(X_train, y_train)
    rf_preds = rf_model.predict(X_test)
    rf_acc = accuracy_score(y_test, rf_preds)
    rf_auc = roc_auc_score(y_test, rf_model.predict_proba(X_test)[:, 1])

    print("\nRandom Forest Results:")
    print(f"Accuracy: {rf_acc:.4f}")
    print(f"ROC AUC: {rf_auc:.4f}")
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, rf_preds))

    # 4. Generate Predictions for All Customers (using RF as it's usually better)
    all_probs = rf_model.predict_proba(X)[:, 1]
    
    results_df = pd.DataFrame({
        'customerID': customer_ids,
        'churn_probability': all_probs
    })

    # Define Risk Levels
    def get_risk_level(prob):
        if prob > 0.7:
            return 'High Risk'
        elif prob > 0.3:
            return 'Medium Risk'
        else:
            return 'Low Risk'

    results_df['risk_level'] = results_df['churn_probability'].apply(get_risk_level)

    # Save results for Power BI
    os.makedirs(os.path.dirname(output_csv_path), exist_ok=True)
    results_df.to_csv(output_csv_path, index=False)
    print(f"\nPrediction results saved to {output_csv_path}")

if __name__ == "__main__":
    PROCESSED_DATA_PATH = "data/processed/cleaned_data.csv"
    POWERBI_DATA_PATH = "powerbi_dashboard/powerbi_segments.csv"
    
    train_and_predict(PROCESSED_DATA_PATH, POWERBI_DATA_PATH)
