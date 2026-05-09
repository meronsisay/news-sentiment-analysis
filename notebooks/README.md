# Exploratory Data Analysis

## `eda_news_sentiment.ipynb`

Comprehensive exploratory analysis of the financial news dataset (1.4 million articles spanning 2009–2020).

**Analysis Components**

| Component | Methodology | Key Output |
|-----------|-------------|-------------|
| Descriptive Statistics | Character count distribution | Mean: 73 chars, Median: 64 chars |
| Publisher Analysis | Frequency aggregation & market share | Top 5 publishers: 52.9% of articles |
| Time Series | Daily volume with spike detection (2σ threshold) | 85 spike days, 95.6% coverage |
| Topic Modeling | CountVectorizer, TF-IDF, bigrams, LDA | Key phrases: "price target", "52 week" |
| Email Domain Extraction | Regex pattern matching | 8,088 email-contributed articles |

**Key Findings**

- **Market Event Correlation**: Largest news spike (2,739 articles) on March 12, 2020 – Black Thursday COVID crash
- **Publisher Concentration**: Benzinga ecosystem accounts for 52.9% of total news volume
- **Temporal Coverage**: 95.6% of trading days have news (3,955 of 4,135 days)

**Visualizations Included**

- Headline length distribution (histogram + box plot)
- Publisher activity (bar chart + market share pie chart)
- Daily news volume with spike detection (time series)
- Word/phrase frequency tables

---
## Technical Analysis

### `technical_indicators.ipynb`

Automated pipeline for calculating technical indicators and generating trading signals for any stock portfolio.

**Calculated Indicators**

| Indicator | Purpose | Typical Parameters |
|-----------|---------|---------------------|
| SMA (20 & 50) | Trend direction | Short & long-term moving averages |
| RSI (14) | Momentum & overbought/oversold | 14-day period (30/70 thresholds) |
| MACD (12,26,9) | Trend strength & momentum | Fast=12, Slow=26, Signal=9 |

**Signal Framework**

| Indicator | Bullish | Bearish |
|-----------|---------|---------|
| Moving Averages | Price > SMA-50 | Price < SMA-50 |
| MACD | MACD > Signal line | MACD < Signal line |
| RSI | < 30 (Oversold) | > 70 (Overbought) |

**Metrics Calculated**

- Total return & annualized volatility
- Sharpe ratio (risk-adjusted return)
- Maximum drawdown

**Sample Output** (Tech stocks, 2009–2023)

| Stock | Return | Volatility | Sharpe | Signal |
|-------|--------|------------|--------|--------|
| NVDA | +24,692% | 45.9% | 0.99 | HOLD |
| AAPL | +6,908% | 28.6% | 1.07 | HOLD |
| AMZN | +5,490% | 34.7% | 0.89 | HOLD |

**Visualizations per Asset**

- Price with moving average overlays
- RSI with overbought/oversold thresholds
- MACD histogram with signal line

**Extensibility**

- Add any stock ticker by modifying input list
- Adjust indicator parameters to test different strategies
- Integrate with news sentiment for enhanced signals