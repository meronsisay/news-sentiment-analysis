import matplotlib.pyplot as plt


def plot_price_with_ma(df, ticker):
    """Plot 1: Price + Moving Averages"""
    print("\n" + "=" * 50)
    print(" PLOT 1: Price Chart with Moving Averages")
    print("=" * 50)
    
    plt.figure(figsize=(14, 5))
    
    plt.plot(df['Date'], df['Close'], label='Close', linewidth=1, color='black')
    plt.plot(df['Date'], df['SMA_20'], label='SMA 20', linewidth=1, alpha=0.8)
    plt.plot(df['Date'], df['SMA_50'], label='SMA 50', linewidth=1, alpha=0.8)
    
    plt.ylabel('Price ($)')
    plt.title(f'{ticker} - Price with Moving Averages')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()


def plot_rsi(df, ticker):
    """Plot 2: RSI"""
    print("\n" + "=" * 50)
    print(" PLOT 2: RSI (Relative Strength Index)")

    print("=" * 50)
    
    plt.figure(figsize=(14, 4))
    
    plt.plot(df['Date'], df['RSI'], linewidth=1, color='purple')
    plt.axhline(70, color='red', linestyle='--', alpha=0.5, label='Overbought (70)')
    plt.axhline(30, color='green', linestyle='--', alpha=0.5, label='Oversold (30)')
    plt.fill_between(df['Date'], 70, 100, alpha=0.1, color='red')
    plt.fill_between(df['Date'], 0, 30, alpha=0.1, color='green')
    
    plt.ylabel('RSI')
    plt.title(f'{ticker} - RSI')
    plt.ylim(0, 100)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()


def plot_macd(df, ticker):
    """Plot 3: MACD"""
    print("\n" + "=" * 50)
    print(" PLOT for MACD (Moving Average Convergence Divergence)")
    print("=" * 50)
    
    plt.figure(figsize=(14, 5))
    
    plt.plot(df['Date'], df['MACD'], label='MACD', linewidth=1, color='blue')
    plt.plot(df['Date'], df['MACD_signal'], label='Signal', linewidth=1, color='red')
    
    colors = ['green' if x >= 0 else 'red' for x in df['MACD_hist']]
    plt.bar(df['Date'], df['MACD_hist'], color=colors, alpha=0.5)
    plt.axhline(0, color='black', linewidth=0.5)
    
    plt.ylabel('MACD')
    plt.xlabel('Date')
    plt.title(f'{ticker} - MACD')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()


def plot_all_indicators(df, ticker):
    """Plot all three indicators."""
    print(f"\n{'#'*50}")
    print(f"TECHNICAL ANALYSIS: {ticker}")
    print(f"{'#'*50}")
    
    plot_price_with_ma(df, ticker)
    plot_rsi(df, ticker)
    plot_macd(df, ticker)

