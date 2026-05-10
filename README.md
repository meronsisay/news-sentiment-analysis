# Predicting Price Moves with News Sentiment

A comprehensive analytical pipeline that combines NLP sentiment analysis of financial news with technical indicators to predict stock price movements.

## Project Overview

This project addresses a critical business need: separating signal from noise in the constant stream of financial news. By quantifying sentiment in headlines and correlating it with price action, we build a foundation for predictive investment strategies.

### Business Objective

Nova Financial Solutions seeks to enhance predictive analytics capabilities by:
- Quantifying sentiment from financial news headlines using NLP
- Computing technical indicators from historical price data
- Establishing statistical correlations between news sentiment and stock price movements
- Delivering actionable investment strategy recommendations

## Repository Structure

```text
news-sentiment-analysis/
├── .github/workflows/
│ └── unittests.yml # CI/CD pipeline
├── data/raw/ # Raw dataset storage
├── notebooks/ # Jupyter notebooks for analysis
│ ├── eda_news_sentiment.ipynb
│ └── technical_indicators.ipynb
├── src/ # Reusable Python modules
│ ├── stock_data_loader.py
│ ├── indicators.py
│ └── visualizations.py
├── tests/ 
├── scripts/ 
├── .gitignore
├── requirements.txt
└── README.md
```
---


## Data Sources

- **Financial News**: 1.4M headlines (2009-2020) with publisher, date, and stock symbol metadata
- **Stock Prices**: Daily OHLCV data from Yahoo Finance

## Analysis Components

### Exploratory Data Analysis (`eda_news_sentiment.ipynb`)

| Component | Methodology | Key Finding |
|-----------|-------------|--------------|
| Descriptive Stats | Character count distribution | Mean headline length: 73 chars |
| Publisher Analysis | Frequency aggregation | Top 5 publishers control 52.9% of volume |
| Time Series | Daily volume with 2σ spike detection | 85 spike days, 95.6% coverage |
| Topic Modeling | TF-IDF, bigrams, LDA | Key phrases: "price target", "52 week" |
| Email Extraction | Regex pattern matching | 8,088 email-contributed articles |

**Key Discovery**: Largest news spike (2,739 articles) occurred on March 12, 2020 — Black Thursday COVID crash.

### Technical Analysis (`technical_indicators.ipynb`)

**Calculated Indicators**

| Indicator | Purpose | Parameters |
|-----------|---------|------------|
| SMA (20 & 50) | Trend direction | Short & long-term averages |
| RSI (14) | Momentum / Overbought-Oversold | 30/70 thresholds |
| MACD (12,26,9) | Trend strength & momentum | Fast, slow, signal |

**Signal Logic**

| Indicator | Bullish | Bearish |
|-----------|---------|---------|
| Moving Averages | Price > SMA-50 | Price < SMA-50 |
| MACD | MACD > Signal | MACD < Signal |
| RSI | < 30 (Oversold) | > 70 (Overbought) |

**Performance Metrics Calculated**
- Total return & annualized volatility
- Sharpe ratio (risk-adjusted return)
- Maximum drawdown


## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/meronsisay/news-sentiment-analysis.git
   cd news-sentiment-analysis
2. Create venv: `python -m venv venv`
3. Activate venv:
   - Windows (Git Bash): `source venv/Scripts/activate`
   - Linux/Mac: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
