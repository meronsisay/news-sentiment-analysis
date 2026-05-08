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