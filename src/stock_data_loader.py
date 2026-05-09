import pandas as pd


def load_stock(ticker, data_path='../data/raw/'):
    """Load stock price dataset into a pandas DataFrame."""
    df = pd.read_csv(f'{data_path}/{ticker}.csv')
    
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values('Date').reset_index(drop=True)
    
    return df

def fix_dtypes(df):
    """Ensure columns are correctly typed AND sorted by date."""
    df = df.copy()
    df['Date'] = pd.to_datetime(df['Date'])
    
    df = df.sort_values('Date').reset_index(drop=True)
    
    df['Open'] = pd.to_numeric(df['Open'], errors='coerce')
    df['High'] = pd.to_numeric(df['High'], errors='coerce')
    df['Low'] = pd.to_numeric(df['Low'], errors='coerce')
    df['Close'] = pd.to_numeric(df['Close'], errors='coerce')
    df['Volume'] = pd.to_numeric(df['Volume'], errors='coerce')
    return df


def handle_missing(df):
    """Check for and handle missing values."""
    df = df.copy()
    df = df.ffill()      # Forward fill (pandas 2.0+)
    df = df.dropna()
    return df