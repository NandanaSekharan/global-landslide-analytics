# 🌍 Global Landslide Data Analytics & Predictive Insights

Analysis of NASA's Global Landslide Catalog (2007-2017, 11,000+ recorded
events) to identify trends, triggers, and geographic patterns behind
landslide events, plus a machine learning model predicting fatal outcomes.

---

## 🚀 Features
- Data cleaning of a real-world, messy NASA dataset (31 raw columns, mixed
  date formats, heavy missing data)
- Exploratory Data Analysis — yearly/monthly trends, top countries, top
  triggers, size distribution
- Geospatial visualization — interactive world map of landslide events
  (Folium, clustered + heatmap views)
- Predictive modeling — Random Forest & Logistic Regression classifiers
  predicting whether an event was fatal
- Interactive Streamlit dashboard with filters (year, country, trigger,
  fatality status)

---

## 📊 Tech Stack
- **Languages:** Python
- **Libraries:** Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn, Folium,
  Plotly, Streamlit
- **Version Control:** Git, GitHub

---

## 📂 Project Structure
```
global-landslide-analytics/
├── data/
│   ├── landslide.csv              # Raw NASA landslide dataset
│   └── landslide_cleaned.csv      # Cleaned dataset (output of analysis)
├── notebooks/
│   ├── analysis.ipynb             # Original exploratory notebook
│   ├── analysis_clean.py          # Cleaned EDA script (final version)
│   ├── predictive_model.ipynb     # Original modeling notebook
│   ├── predictive_model_clean.py  # Cleaned modeling script (final version)
│   ├── dashboard.py               # Streamlit interactive dashboard
│   └── landslide_map.html         # Exported interactive Folium map
├── outputs/                       # Generated charts (see below)
├── requirements.txt
└── README.md
```

---

## 🖼 Key Visualizations
| Chart | Insight |
|---|---|
| `outputs/chart_yearly_trend.png` | Landslide events recorded by year (1988-2017) |
| `outputs/chart_monthly_trend.png` | Seasonal pattern — monsoon months peak |
| `outputs/chart_top_countries.png` | Countries with most recorded events |
| `outputs/chart_top_triggers.png` | Most common landslide triggers |
| `outputs/chart_size_distribution.png` | Distribution of landslide sizes |
| `outputs/chart_confusion_matrix.png` | Random Forest fatal-prediction results |
| `outputs/chart_feature_importance.png` | Which features drive fatality predictions |

---

## 🔑 Key Findings
- Dataset spans **1988–2017**, with **11,033 recorded events**.
- **United States** recorded the most landslide events (2,992), largely due
  to denser reporting infrastructure.
- **Downpour/rainfall** is the dominant trigger (4,680 events), consistent
  with monsoon-driven landslide risk.
- Total recorded fatalities across all events: **31,061**.
- **Logistic Regression achieved 78.75% accuracy** predicting fatal vs.
  non-fatal events; **Random Forest achieved 72.5% accuracy** but with
  better recall on the minority (fatal) class (80% recall vs. 7% for
  Logistic Regression) — showing the classic precision/recall trade-off
  on an imbalanced dataset.
- Landslide trigger and country were the most important predictive features
  for fatality risk.

---

## ⚠️ Notes & Limitations
- Reporting is uneven across countries (some regions likely under-reported),
  which biases the "top countries" ranking toward better-monitored regions.
- Fatality prediction accuracy is moderate — class imbalance (only ~22% of
  events are fatal) makes this a hard classification problem; further work
  with SMOTE and additional features (population density, terrain slope)
  could improve results.

---

## 🔮 Future Scope
- Real-time landslide risk monitoring using live weather API integration
- Deploy the dashboard publicly (Streamlit Community Cloud)
- Incorporate terrain/elevation and population density as model features

---

## ▶️ Running Locally
```bash
pip install -r requirements.txt
cd notebooks
python analysis_clean.py         # runs EDA, generates charts
python predictive_model_clean.py # trains models, generates model charts
streamlit run dashboard.py       # launches interactive dashboard
```

---

## 📜 License
This project is open-source under the MIT License.
