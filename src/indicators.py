import pandas as pd
import numpy as np
import talib


def add_moving_averages(df, windows=[20, 50]):
    """
    Add Simple and Exponential Moving Averages.
    
    SMA = average closing price over N days
    EMA = weighted average (more weight to recent days)
    """
    close = df['Close'].values
    
    for window in windows:
        # Simple Moving Average
        df[f'SMA_{window}'] = talib.SMA(close, timeperiod=window)
        
        # Exponential Moving Average
        df[f'EMA_{window}'] = talib.EMA(close, timeperiod=window)
    
    return df


def add_rsi(df, period=14):
    """
    Add Relative Strength Index.
    
    RSI = 100 - (100 / (1 + RS))
    where RS = Average Gain / Average Loss over N periods
    
    Readings:
    - > 70: Overbought (potential sell signal)
    - < 30: Oversold (potential buy signal)
    - 30-70: Neutral
    """
    close = df['Close'].values
    df['RSI'] = talib.RSI(close, timeperiod=period)
    return df


def add_macd(df, fast=12, slow=26, signal=9):
    """
    Add MACD (Moving Average Convergence Divergence).
    
    MACD = Fast EMA (12) - Slow EMA (26)
    Signal Line = EMA of MACD (9)
    Histogram = MACD - Signal Line
    
    Signals:
    - MACD crosses above Signal = Bullish
    - MACD crosses below Signal = Bearish
    - Histogram positive = Momentum up
    - Histogram negative = Momentum down
    """
    close = df['Close'].values
    
    # MACD line, Signal line, Histogram
    df['MACD'], df['MACD_signal'], df['MACD_hist'] = talib.MACD(
        close, 
        fastperiod=fast, 
        slowperiod=slow, 
        signalperiod=signal
    )
    
    return df


def check_rsi_signal(df):
    """Detect overbought (>70) or oversold (<30) conditions."""
    rsi = df['RSI'].iloc[-1]
    
    if rsi > 70:
        return {'status': 'OVERBOUGHT', 'action': 'SELL'}
    elif rsi < 30:
        return {'status': 'OVERSOLD', 'action': 'BUY'}
    else:
        return {'status': 'NEUTRAL', 'action': 'HOLD'}


def check_macd_signal(df):
    """Detect momentum shift (MACD crossover)."""
    curr_macd = df['MACD'].iloc[-1]
    curr_signal = df['MACD_signal'].iloc[-1]
    prev_macd = df['MACD'].iloc[-2]
    prev_signal = df['MACD_signal'].iloc[-2]
    
    # Crossover detection
    if prev_macd <= prev_signal and curr_macd > curr_signal:
        return {'momentum': 'BULLISH', 'action': 'BUY'}
    elif prev_macd >= prev_signal and curr_macd < curr_signal:
        return {'momentum': 'BEARISH', 'action': 'SELL'}
    
    # No crossover - check current position
    if curr_macd > curr_signal:
        return {'momentum': 'BULLISH', 'action': 'HOLD'}
    else:
        return {'momentum': 'BEARISH', 'action': 'HOLD'}


def check_ma_signal(df, short=20, long=50):
    """Detect trend and crossovers (Golden/Death Cross)."""
    curr_short = df[f'SMA_{short}'].iloc[-1]
    curr_long = df[f'SMA_{long}'].iloc[-1]
    prev_short = df[f'SMA_{short}'].iloc[-2]
    prev_long = df[f'SMA_{long}'].iloc[-2]
    
    # Crossover detection
    if prev_short <= prev_long and curr_short > curr_long:
        return {'trend': 'UPTREND', 'action': 'BUY', 'signal': 'GOLDEN CROSS'}
    elif prev_short >= prev_long and curr_short < curr_long:
        return {'trend': 'DOWNTREND', 'action': 'SELL', 'signal': 'DEATH CROSS'}
    
    # No crossover - check current trend
    if curr_short > curr_long:
        return {'trend': 'UPTREND', 'action': 'HOLD'}
    else:
        return {'trend': 'DOWNTREND', 'action': 'HOLD'}


def print_signals(df, ticker):
    """Print all signals for a stock."""
    
    # Get signals
    rsi = check_rsi_signal(df)
    macd = check_macd_signal(df)
    ma = check_ma_signal(df)
    
    # Display
    print(f"\n MOVING AVERAGE FOR {ticker}:")
    print(f"   Trend: {ma['trend']}")
    print(f"   Action: {ma['action']}")
    
    print(f"\n RSI FOR {ticker}:")
    print(f"   Status: {rsi['status']}")
    print(f"   Action: {rsi['action']}")
    
    print(f"\n MACD FOR {ticker}:")
    print(f"   Momentum: {macd['momentum']}")
    print(f"   Action: {macd['action']}")

# Minimal PyNance compliance - just calculate and print

def print_financial_metrics(df, ticker):
    """Print key financial metrics (no new columns added)."""
    
    # Calculate from close prices
    returns = df['Close'].pct_change().dropna()
    
    # 1. Total Return
    total_return = (df['Close'].iloc[-1] / df['Close'].iloc[0]) - 1
    
    # 2. Volatility (annualized)
    volatility = returns.std() * np.sqrt(252)
    
    # 3. Max Drawdown
    cumulative = (1 + returns).cumprod()
    peak = cumulative.expanding().max()
    drawdown = (cumulative - peak) / peak
    max_drawdown = drawdown.min()
    
    # 4. Sharpe Ratio
    sharpe = (returns.mean() * 252 - 0.02) / (returns.std() * np.sqrt(252))
    
    # Print results
    print(f"\n{'='*50}")
    print(f"FINANCIAL METRICS: {ticker}")
    print(f"{'='*50}")
    print(f"Total Return:      {total_return:.1%}")
    print(f"Volatility:        {volatility:.1%}")
    print(f"Max Drawdown:      {max_drawdown:.1%}")
    print(f"Sharpe Ratio:      {sharpe:.2f}")
    print(f"{'='*50}")

