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
global-landslide-analytics/
├── data/
│ ├── landslide.csv # Raw NASA landslide dataset
│ └── landslide_cleaned.csv # Cleaned dataset (output of analysis)
├── notebooks/
│ ├── analysis_clean.py # Cleaned EDA script (final version)
│ ├── predictive_model_clean.py # Cleaned modeling script (final version)
│ ├── dashboard.py # Streamlit interactive dashboard
│ └── landslide_map.html # Exported interactive Folium map
├── outputs/ # Generated charts (see below)
├── requirements.txt
└── README.md
