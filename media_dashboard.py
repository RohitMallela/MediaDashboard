import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta

# Initialize Streamlit app
st.set_page_config(page_title="2025 Media Performance Dashboard", layout="wide")
st.title("📊 2025 Media Performance Dashboard")

# Sample Data for Tracking Performance Metrics
media_data = pd.DataFrame({
    "Channel": ["TV", "CTV", "YouTube", "Social Media", "Search", "Influencer Marketing", "Retail Media", "Programmatic", "Emerging Media"],
    "Budget Allocated (Billion IDR)": [15, 10, 8, 7, 4, 3, 2, 1, 1],
    "CPM (Cost per 1000 Impressions)": [20000, 15000, 12000, 10000, 8000, 6000, 7000, 5000, 9000],
    "CPA (Cost per Acquisition)": [300000, 250000, 200000, 180000, 150000, 120000, 110000, 90000, 95000],
    "ROAS (Return on Ad Spend)": [1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.2, 4.5, 4.8],
})

# Simulated Monthly Performance Data
date_range = [datetime.today() - timedelta(days=x*30) for x in range(12)]
performance_trends = pd.DataFrame({
    "Month": date_range[::-1],
    "Total Spend (Billion IDR)": [4, 4.2, 4.5, 4.8, 5, 5.3, 5.5, 6, 6.5, 7, 7.5, 8],
    "Total ROAS": [2.0, 2.1, 2.3, 2.5, 2.7, 2.8, 3.0, 3.2, 3.3, 3.5, 3.7, 4.0]
})

# Filters
st.sidebar.header("🔍 Filter Options")
selected_channel = st.sidebar.selectbox("Select Media Channel:", ["All"] + list(media_data["Channel"]))

# Filtered Data
if selected_channel != "All":
    filtered_data = media_data[media_data["Channel"] == selected_channel]
else:
    filtered_data = media_data

# Display Data Table
st.write("### Media Performance Overview")
st.dataframe(filtered_data)

# Visualization - Budget Allocation
fig_budget = px.pie(media_data, values="Budget Allocated (Billion IDR)", names="Channel", title="Budget Allocation by Channel")
st.plotly_chart(fig_budget)

# Visualization - ROAS Comparison
fig_roas = px.bar(media_data, x="Channel", y="ROAS", color="ROAS", title="Return on Ad Spend (ROAS) by Channel")
st.plotly_chart(fig_roas)

# Visualization - CPM & CPA Analysis
fig_cpm_cpa = px.scatter(media_data, x="CPM (Cost per 1000 Impressions)", y="CPA (Cost per Acquisition)", size="Budget Allocated (Billion IDR)", color="Channel", hover_name="Channel", title="CPM vs. CPA Analysis")
st.plotly_chart(fig_cpm_cpa)

# Visualization - Monthly Performance Trends
fig_trend = go.Figure()
fig_trend.add_trace(go.Scatter(x=performance_trends["Month"], y=performance_trends["Total Spend (Billion IDR)"], mode='lines+markers', name="Total Spend"))
fig_trend.add_trace(go.Scatter(x=performance_trends["Month"], y=performance_trends["Total ROAS"], mode='lines+markers', name="Total ROAS", yaxis="y2"))
fig_trend.update_layout(title="Monthly Media Performance Trends", xaxis_title="Month", yaxis_title="Total Spend (Billion IDR)", yaxis2=dict(title="Total ROAS", overlaying="y", side="right"))
st.plotly_chart(fig_trend)

# Prediction for Next Quarter
future_months = [datetime.today() + timedelta(days=x*30) for x in range(1, 4)]
predicted_spend = [performance_trends["Total Spend (Billion IDR)"].iloc[-1] * (1.05**x) for x in range(1, 4)]
predicted_roas = [performance_trends["Total ROAS"].iloc[-1] * (1.03**x) for x in range(1, 4)]
prediction_df = pd.DataFrame({"Month": future_months, "Predicted Spend (Billion IDR)": predicted_spend, "Predicted ROAS": predicted_roas})

fig_prediction = px.line(prediction_df, x="Month", y=["Predicted Spend (Billion IDR)", "Predicted ROAS"], markers=True, title="Predicted Performance for Next Quarter")
st.plotly_chart(fig_prediction)

# Conclusion
st.write("💡 **Key Insights & Next Steps:**")
st.write("- Optimize underperforming channels by reallocating budget.")
st.write("- Enhance AI-powered media buying for better cost efficiency.")
st.write("- Track performance monthly and adjust budget dynamically.")
st.write("- Predictive modeling suggests a 5% increase in spend and 3% improvement in ROAS next quarter.")
