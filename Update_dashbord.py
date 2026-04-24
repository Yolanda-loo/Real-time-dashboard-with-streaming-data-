import streamlit as st
import pandas as pd
import time
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Real-Time Sales Dashboard", layout="wide")

st.title("📊 Real-Time Sales Dashboard")

# Function to load and refresh data
@st.cache_data(ttl=5)
def load_data():
    return pd.read_csv("data/streamed_sales.csv")

# Auto-refresh every few seconds
placeholder = st.empty()

while True:
    df = load_data()

    # KPIs
    total_revenue = df["Revenue"].sum()
    top_product = df.groupby("Product")["Revenue"].sum().idxmax()
    top_region = df.groupby("Region")["Revenue"].sum().idxmax()

    with placeholder.container():
        st.subheader("Key Performance Indicators")
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Revenue", f"${total_revenue:,.2f}")
        col2.metric("Top Product", top_product)
        col3.metric("Top Region", top_region)

        # Revenue by region
        st.subheader("Revenue by Region")
        fig1, ax1 = plt.subplots(figsize=(6,4))
        sns.barplot(x="Region", y="Revenue", data=df.groupby("Region")["Revenue"].sum().reset_index(), ax=ax1, palette="Blues_d")
        st.pyplot(fig1)

        # Top products
        st.subheader("Top Products by Revenue")
        fig2, ax2 = plt.subplots(figsize=(6,4))
        sns.barplot(x="Product", y="Revenue", data=df.groupby("Product")["Revenue"].sum().reset_index().sort_values(by="Revenue", ascending=False), ax=ax2, palette="Greens_d")
        st.pyplot(fig2)

        # Revenue over time
        st.subheader("Revenue Over Time")
        df["Timestamp"] = pd.to_datetime(df["Timestamp"])
        time_revenue = df.groupby("Timestamp")["Revenue"].sum().reset_index()
        fig3, ax3 = plt.subplots(figsize=(10,5))
        ax3.plot(time_revenue["Timestamp"], time_revenue["Revenue"], marker="o")
        ax3.set_title("Revenue Over Time")
        ax3.set_xlabel("Timestamp")
        ax3.set_ylabel("Revenue")
        plt.xticks(rotation=45)
        st.pyplot(fig3)

    time.sleep(5)  # refresh every 5 seconds
