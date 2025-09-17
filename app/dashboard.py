import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("data/Bakery_sales.csv")
    df["DateTime"] = pd.to_datetime(df["DateTime"])
    df["Hour"] = df["DateTime"].dt.hour
    df["Weekday"] = df["DateTime"].dt.day_name()
    df["Month"] = df["DateTime"].dt.month_name()
    return df

df = load_data() 

st.title("🍞 Bakery Sales Dashboard")

# Top Selling Items
st.subheader("Top 10 Best-Selling Items")
top_items = df["Items"].value_counts().head(10).reset_index()
top_items.columns = ["Item", "Count"]
fig1 = px.bar(top_items, x="Item", y="Count", text="Count", color="Item")
st.plotly_chart(fig1)

# Sales Over Time
st.subheader("Sales Over Time")
daily_sales = df.groupby(df["DateTime"].dt.date).size().reset_index(name="Sales")
fig2 = px.line(daily_sales, x="DateTime", y="Sales", title="Daily Sales Trend")
st.plotly_chart(fig2)

# Sales by Day of Week
st.subheader("Sales by Day of the Week")
weekday_sales = df["Weekday"].value_counts().reset_index()
weekday_sales.columns = ["Weekday", "Count"]
fig3 = px.bar(weekday_sales, x="Weekday", y="Count", color="Weekday")
st.plotly_chart(fig3)

# Sales by Hour
st.subheader("Sales by Hour")
hourly_sales = df["Hour"].value_counts().sort_index().reset_index()
hourly_sales.columns = ["Hour", "Count"]
fig4 = px.bar(hourly_sales, x="Hour", y="Count")
st.plotly_chart(fig4)

