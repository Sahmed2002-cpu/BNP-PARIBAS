import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def segment_customers(df):
    features = df[['transaction_amount', 'age']]  # Example features
    kmeans = KMeans(n_clusters=3)
    df['segment'] = kmeans.fit_predict(features)
    return df

if __name__ == "__main__":
    df = pd.read_csv('data/cleaned_customer_data.csv')
    segmented_df = segment_customers(df)
    segmented_df.to_csv('data/segmented_customer_data.csv', index=False)
