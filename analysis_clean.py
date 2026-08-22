"""
Global Landslide Data Analytics
---------------------------------
Cleans NASA Global Landslide Catalog data and produces exploratory
visualizations: yearly/monthly trends, top countries, triggers, and size
distribution.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

# -----------------------------
# 1. LOAD DATA
# -----------------------------
df = pd.read_csv("../data/landslide.csv")
print("Raw shape:", df.shape)

# -----------------------------
# 2. CLEAN DATA
# -----------------------------

# Parse dates, extract year/month
df["event_date"] = pd.to_datetime(df["event_date"], errors="coerce")
df["year"] = df["event_date"].dt.year
df["month"] = df["event_date"].dt.month

# Drop columns that are mostly empty or not useful for analysis
drop_cols = [
    "event_time", "notes", "storm_name", "photo_link",
    "gazeteer_closest_point", "gazeteer_distance",
    "event_import_source", "event_import_id", "admin_division_population",
    "source_link", "submitted_date", "created_date", "last_edited_date"
]
df = df.drop(columns=[c for c in drop_cols if c in df.columns])

# Fill missing values sensibly
df["injury_count"] = df["injury_count"].fillna(0)
df["fatality_count"] = df["fatality_count"].fillna(0)
for col in ["admin_division_name", "country_code", "country_name",
            "event_description", "location_description",
            "landslide_setting", "landslide_trigger", "landslide_size",
            "location_accuracy", "landslide_category"]:
    if col in df.columns:
        df[col] = df[col].fillna("Unknown")

print("Missing values after cleaning:", df.isnull().sum().sum())
df.to_csv("../data/landslide_cleaned.csv", index=False)

# -----------------------------
# 3. EDA VISUALIZATIONS
# -----------------------------

# --- Year-wise trend ---
plt.figure(figsize=(12, 6))
df["year"].value_counts().sort_index().plot(kind="bar", color="steelblue")
plt.title("Year-wise Landslide Events")
plt.xlabel("Year")
plt.ylabel("Number of Events")
plt.tight_layout()
plt.savefig("../outputs/chart_yearly_trend.png", dpi=150)
plt.close()

# --- Month-wise trend ---
plt.figure(figsize=(10, 5))
month_names = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
monthly_counts = df["month"].value_counts().sort_index()
plt.bar(monthly_counts.index, monthly_counts.values, color="skyblue", edgecolor="black")
plt.title("Month-wise Landslide Events")
plt.xlabel("Month")
plt.ylabel("Number of Events")
plt.xticks(range(1, 13), month_names)
plt.tight_layout()
plt.savefig("../outputs/chart_monthly_trend.png", dpi=150)
plt.close()

# --- Top 10 countries ---
plt.figure(figsize=(12, 6))
df["country_name"].value_counts().head(10).plot(kind="bar", color="coral")
plt.title("Top 10 Countries by Landslide Events")
plt.xlabel("Country")
plt.ylabel("Number of Events")
plt.tight_layout()
plt.savefig("../outputs/chart_top_countries.png", dpi=150)
plt.close()

# --- Top triggers ---
plt.figure(figsize=(12, 6))
df["landslide_trigger"].value_counts().head(10).plot(kind="bar", color="mediumseagreen")
plt.title("Top Triggers of Landslides")
plt.xlabel("Trigger")
plt.ylabel("Number of Events")
plt.tight_layout()
plt.savefig("../outputs/chart_top_triggers.png", dpi=150)
plt.close()

# --- Size distribution ---
plt.figure(figsize=(10, 6))
df["landslide_size"].value_counts().plot(kind="bar", color="mediumpurple")
plt.title("Distribution of Landslide Sizes")
plt.xlabel("Size Category")
plt.ylabel("Number of Events")
plt.tight_layout()
plt.savefig("../outputs/chart_size_distribution.png", dpi=150)
plt.close()

# -----------------------------
# 4. KEY STATS SUMMARY (printed for README)
# -----------------------------
print("\n--- Key Stats ---")
print("Date range:", int(df["year"].min()), "-", int(df["year"].max()))
print("Total events:", len(df))
print("Top country:", df["country_name"].value_counts().idxmax(),
      "(", df["country_name"].value_counts().max(), "events )")
print("Top trigger:", df["landslide_trigger"].value_counts().idxmax(),
      "(", df["landslide_trigger"].value_counts().max(), "events )")
print("Total fatalities recorded:", int(df["fatality_count"].sum()))

print("\nAll charts saved to ../outputs/. EDA complete.")
