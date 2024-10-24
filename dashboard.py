import pandas as pd
import plotly.express as px

def create_dashboard(df):
    fig = px.bar(df, x='customer_segment', y='transaction_amount', title='Customer Segment Analysis')
    fig.show()

if __name__ == "__main__":
    df = pd.read_csv('data/segmented_customer_data.csv')
    create_dashboard(df)
