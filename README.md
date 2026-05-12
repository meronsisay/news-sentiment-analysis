# Predicting Price Moves with News Sentiment

A comprehensive analytical pipeline that combines NLP sentiment analysis of financial news with technical indicators to predict stock price movements.

## Project Overview

This project addresses Nova Financial Solutions' goal of enhancing predictive analytics by separating signal from noise in financial news. The pipeline:

- Processes **1.4 million news headlines** (2009–2020) for **5 technology stocks**: AAPL, AMZN, GOOG, META, NVDA
- Computes **technical indicators** (SMA, EMA, RSI, MACD) for trend and momentum analysis
- Quantifies **sentiment scores** using VADER with custom financial lexicon (e.g., "surges", "crashes", "upgrade")
- Measures **Pearson correlation** between news sentiment and daily stock returns (same-day)

**Key Question:** Does financial news sentiment predict stock price movements?



## Repository Structure

```text
news-sentiment-analysis/
├── .github/workflows/
│ └── unittests.yml # CI/CD pipeline
├── data/raw/ # Raw dataset storage
├── notebooks/ # Jupyter notebooks for analysis
│ ├── eda_news_sentiment.ipynb
│ ├── technical_indicators.ipynb
│ └── sentiment_correlation.ipynb
├── src/ # Reusable Python modules
│ ├── stock_data_loader.py
│ ├── indicators.py
│ └── visualizations.py
├── tests/ # Unit tests
├── scripts/ # Utility scripts
├── .gitignore
├── requirements.txt
└── README.md
```
---


## Data Sources

- **Financial News**: 1.4M headlines (2009-2020) with publisher, date, and stock symbol metadata
- **Stock Prices**: Daily OHLCV data from Yahoo Finance

## Key Findings

| Metric | Result |
|--------|--------|
| **Overall Correlation** | r = 0.2246 (weak positive) |
| **Strongest Stock** | META (r = 0.49, p < 0.001) |
| **Most Reliable** | NVDA (1,143 days, r = 0.22) |
| **News Coverage** | 95.6% of trading days have news |
| **Publisher Concentration** | Top 5 publishers = 52.9% of articles |

---

## Notebooks

| Notebook | Description |
|----------|-------------|
| `eda_news_sentiment.ipynb` | EDA: headline stats, publisher analysis, topic modeling, time series |
| `technical_indicators.ipynb` | Technical analysis: SMA, EMA, RSI, MACD, Sharpe ratio |
| `sentiment_correlation.ipynb` | Sentiment scoring, date alignment, correlation, visualizations |

---

## Technologies Used

| Category | Tools |
|----------|-------|
| **Data Processing** | Pandas, NumPy |
| **NLP & Sentiment** | VADER, TextBlob |
| **Technical Indicators** | TA-Lib |
| **Visualization** | Matplotlib, Seaborn |
| **Statistical Analysis** | SciPy, Pearson correlation |
| **CI/CD** | GitHub Actions |

---

## Correlation Results

| Stock | Correlation | P-value | Significance | Days |
|-------|-------------|---------|--------------|------|
| META | 0.4921 | < 0.001 |  Significant | 74 |
| NVDA | 0.2240 | < 0.001 |  Significant | 1,143 |
| GOOG | 0.1884 | < 0.001 |  Significant | 353 |
| AAPL | 0.1697 | 0.191 |  Not significant | 61 |
| AMZN | 0.1030 | n < 30 |  Insufficient | 28 |
| **Overall** | **0.2246** | - | Weak positive | 1,659 |

---

## Limitations

| Limitation | Impact |
|------------|--------|
| **Data Imbalance** | NVDA = 69% of matched observations |
| **No Lag Analysis** | Same-day correlation only |
| **Confounding Factors** | Macro events not isolated |
| **Low Statistical Power** | AAPL (61 days), AMZN (28 days) |
| **Publisher Concentration** | Top 5 publishers = 52.9% of news |


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
