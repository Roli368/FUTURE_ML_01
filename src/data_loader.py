import pandas as pd
import os

def load_data(filepath):
    """
    Loads the Superstore Sales dataset from a CSV file.
    
    Args:
        filepath (str): Path to the CSV file.
        
    Returns:
        pd.DataFrame: Loaded dataframe.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found at {filepath}")
    
    try:
        # Try loading with default encoding first
        df = pd.read_csv(filepath, encoding='utf-8')
    except UnicodeDecodeError:
        # Fallback to 'latin1' or 'cp1252' if utf-8 fails
        print("UTF-8 decoding failed, trying 'latin1'...")
        df = pd.read_csv(filepath, encoding='latin1')
        
    print(f"Data loaded successfully from {filepath}")
    print(f"Shape: {df.shape}")
    return df

def clean_data(df):
    """
    Basic data cleaning:
    - Standardize column names
    - Convert date columns to datetime
    - Sort by order date
    """
    # Standardize column names
    df.columns = df.columns.str.lower().str.replace(' ', '_').str.replace('-', '_')
    
    # Convert date columns
    date_cols = [col for col in df.columns if 'date' in col]
    for col in date_cols:
        df[col] = pd.to_datetime(df[col], errors='coerce')
    
    # Sort by order_date
    if 'order_date' in df.columns:
        df = df.sort_values('order_date')
        
    print("Data cleaned and date columns converted.")
    return df

def feature_engineering(df):
    """
    Extract time-based features from order_date.
    """
    if 'order_date' not in df.columns:
        return df
        
    df['year'] = df['order_date'].dt.year
    df['month'] = df['order_date'].dt.month
    df['day_of_week'] = df['order_date'].dt.dayofweek
    df['quarter'] = df['order_date'].dt.quarter
    
    print("Time-based features created.")
    return df

def aggregate_monthly(df):
    """
    Aggregates sales data to monthly level.
    Returns a DataFrame with 'order_date' as index and 'sales' as column.
    """
    # Ensure we use the proper column (sales) and date
    monthly_sales = df.set_index('order_date').resample('ME')['sales'].sum().reset_index()
    return monthly_sales

if __name__ == "__main__":
    # Correct path relative to where script is run or absolute
    possible_paths = [
        "../data/Sample - Superstore.csv",
        "data/Sample - Superstore.csv",
        r"c:/Users/rolir/Desktop/FUTURE-ML-01/data/Sample - Superstore.csv"
    ]
    
    data_path = None
    for path in possible_paths:
        if os.path.exists(path):
            data_path = path
            break
            
    if data_path:
        df = load_data(data_path)
        df = clean_data(df)
        df = feature_engineering(df)
        
        # Save processed transactional data
        # We save to: c:/Users/rolir/Desktop/FUTURE-ML-01/data/processed_superstore.csv
        
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # FUTURE-ML-01 root if in src/
        data_dir = os.path.join(base_dir, "data")
        os.makedirs(data_dir, exist_ok=True)
        
        output_path = os.path.join(data_dir, "processed_superstore.csv")
        df.to_csv(output_path, index=False)
        print(f"Processed transactional data saved to {output_path}")
        
        # Aggregate monthly for modeling
        df_monthly = aggregate_monthly(df)
        monthly_output_path = os.path.join(data_dir, "monthly_sales.csv")
        df_monthly.to_csv(monthly_output_path, index=False)
        print(f"Monthly aggregated data saved to {monthly_output_path}")
        
        print(df.head())
        print(df.info())
    else:
        print("Error: Dataset not found in expected locations.")
