import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv(r"D:\disaster\world_landslide_project\data\landslide.csv")

# Convert dates
df["event_date"] = pd.to_datetime(df["event_date"], errors="coerce")
df["year"] = df["event_date"].dt.year

# Drop rows with no year
df = df.dropna(subset=["year"])
df["year"] = df["year"].astype(int)

# Sidebar filters
st.sidebar.header("Filters")

# Year range
min_year, max_year = int(df["year"].min()), int(df["year"].max())
year_range = st.sidebar.slider("Select Year Range", min_year, max_year, (min_year, max_year))
df = df[(df["year"] >= year_range[0]) & (df["year"] <= year_range[1])]

# Country filter
countries = sorted(df["country_name"].dropna().unique())
selected_country = st.sidebar.selectbox("Select Country", ["All"] + countries)
if selected_country != "All":
    df = df[df["country_name"] == selected_country]

# Trigger filter (multi-select)
triggers_list = sorted(df["landslide_trigger"].dropna().unique())
selected_triggers = st.sidebar.multiselect("Select Trigger(s)", ["All"] + triggers_list, default=["All"])
if "All" not in selected_triggers:
    df = df[df["landslide_trigger"].isin(selected_triggers)]

# Fatal vs Non-fatal toggle
fatal_toggle = st.sidebar.radio("Fatalities Filter", ["All", "Fatal only", "Non-fatal only"])
if fatal_toggle == "Fatal only":
    df = df[df["fatality_count"] > 0]
elif fatal_toggle == "Non-fatal only":
    df = df[df["fatality_count"] == 0]

# ====================================
# Dashboard checkboxes
# ====================================
st.sidebar.header("Show/Hide Visuals")
show_trend = st.sidebar.checkbox("📈 Landslides per Year", True)
show_trigger = st.sidebar.checkbox("🌋 Trigger Distribution", True)
show_fatalities = st.sidebar.checkbox("☠️ Fatalities per Year", True)
show_size = st.sidebar.checkbox("📊 Size Distribution", True)
show_map = st.sidebar.checkbox("🗺️ Landslide Map", True)

# Yearly trend
if show_trend:
    yearly = df.groupby("year").size().reset_index(name="count")
    fig1 = px.line(yearly, x="year", y="count", markers=True, title="Landslides per Year")
    st.plotly_chart(fig1)

# Triggers distribution
if show_trigger:
    triggers = df["landslide_trigger"].value_counts().reset_index()
    triggers.columns = ["Trigger", "Count"]
    fig2 = px.bar(triggers, x="Trigger", y="Count", title="Landslide Triggers")
    st.plotly_chart(fig2)

# Fatalities over time
if show_fatalities:
    fatalities = df.groupby("year")["fatality_count"].sum().reset_index()
    fig3 = px.bar(fatalities, x="year", y="fatality_count", title="Fatalities per Year")
    st.plotly_chart(fig3)

# Landslide size distribution
if show_size:
    size_dist = df["landslide_size"].value_counts().reset_index()
    size_dist.columns = ["Size", "Count"]
    fig5 = px.pie(size_dist, names="Size", values="Count", title="Landslide Size Distribution")
    st.plotly_chart(fig5)

# Map
if show_map:
    fig4 = px.scatter_mapbox(
        df, lat="latitude", lon="longitude", hover_name="event_title",
        hover_data=["country_name", "landslide_trigger", "fatality_count"],
        color="landslide_trigger", zoom=2, height=500
    )
    fig4.update_layout(mapbox_style="open-street-map")
    fig4.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    st.plotly_chart(fig4)
