import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

def model_churn(df):
    X = df[['age', 'transaction_amount']]  # Features
    y = df['churn']  # Target variable

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    print(classification_report(y_test, predictions))

if __name__ == "__main__":
    df = pd.read_csv('data/segmented_customer_data.csv')
    model_churn(df)
