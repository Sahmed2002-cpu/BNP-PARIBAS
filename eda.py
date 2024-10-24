import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_data(df):
    # Example of plotting transaction count by customer segment
    plt.figure(figsize=(10, 6))
    sns.countplot(x='customer_segment', data=df)
    plt.title('Transaction Count by Customer Segment')
    plt.show()

if __name__ == "__main__":
    df = pd.read_csv('data/cleaned_customer_data.csv')
    plot_data(df)
