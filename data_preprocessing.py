import pandas as pd

def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

def clean_data(df):
    # Drop duplicates
    df.drop_duplicates(inplace=True)
    
    # Handle missing values
    df.fillna(method='ffill', inplace=True)
    
    return df

if __name__ == "__main__":
    data = load_data('data/customer_data.csv')
    clean_data = clean_data(data)
    clean_data.to_csv('data/cleaned_customer_data.csv', index=False)
