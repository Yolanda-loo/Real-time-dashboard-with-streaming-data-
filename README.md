# 📊 Real-Time Sales Dashboard

![Status](https://img.shields.io/badge/Project-Active-brightgreen)
![Tool](https://img.shields.io/badge/Python-Streamlit%20%7C%20Pandas%20%7C%20Matplotlib%20%7C%20Seaborn-blue)
![Focus](https://img.shields.io/badge/Domain-Streaming%20Analytics%20%7C%20Operational%20Monitoring-orange)

## 🚀 Objective
Build a real-time dashboard that ingests live sales transactions, processes them into KPIs, and visualizes performance across products and regions.  
This project demonstrates how **streaming data pipelines and interactive dashboards** can support live decision-making.

---

## 🛠️ Workflow
1. **Data Simulation**  
   - Script: `simulate_stream.py` generates live transactions (TransactionID, Timestamp, Product, Region, Revenue).  
   - Streams data with delays to mimic real-time ingestion.

2. **Data Processing**  
   - Script: `process_stream.py` aggregates KPIs: total revenue, revenue by region, top products.  
   - Produces static charts for exploratory analysis.

3. **Dashboard Visualization**  
   - Script: `update_dashboard.py` builds a **Streamlit dashboard**.  
   - Auto-refreshes every 5 seconds to update KPIs and charts.  
   - Displays:  
     - Total revenue, top product, top region.  
     - Revenue by region (bar chart).  
     - Top products (bar chart).  
     - Revenue over time (line chart).

---

## 📂 Deliverables
- `/data` → Simulated streaming sales dataset (`streamed_sales.csv`).  
- `/scripts` → Streaming, processing, and dashboard scripts.  
- `/dashboard` → Streamlit app for real-time monitoring.  
- `/visuals` → Charts of KPIs and trends.  
- `/insights` → Markdown file summarizing findings and recommendations.  
- `README.md` → Documentation (this file).  

---

## 🔍 Business Value
- **Operational Monitoring** → Track sales performance in real time.  
- **Revenue Insights** → Identify top products and regions instantly.  
- **Decision Support** → Enable managers to act quickly on live data.  

---

## 📸 Example Visualizations
*(Insert screenshots of Streamlit dashboard: KPIs, bar charts, line chart)*

---

## 🧭 Next Steps
- Integrate with Kafka or Azure Event Hub for true streaming ingestion.  
- Add anomaly detection for unusual sales patterns.  
- Deploy dashboard to cloud for enterprise access.
