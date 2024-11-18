
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned Qualtrics data
data_path = 'Cleaned_Qualtrics_Survey_Data.csv'
data = pd.read_csv(data_path)

# Sidebar filters
st.sidebar.header("Filters")
finished_filter = st.sidebar.selectbox("Filter by Finished Responses", ["All", "Finished Only", "Not Finished"])

if finished_filter == "Finished Only":
    data = data[data['Finished'] == "TRUE"]
elif finished_filter == "Not Finished":
    data = data[data['Finished'] != "TRUE"]

# Title
st.title("Qualtrics Survey Data Insights")

# Key metrics
total_responses = len(data)
avg_duration = data["Duration (in seconds)"].astype(float).mean()
completion_rate = (data["Finished"] == "TRUE").mean() * 100

st.header("Key Metrics")
st.metric("Total Responses", total_responses)
st.metric("Average Duration (Seconds)", round(avg_duration, 2))
st.metric("Completion Rate (%)", round(completion_rate, 2))

# Visualization: Response Count and Average Duration
st.header("Survey Overview")
fig1, ax1 = plt.subplots()
ax1.bar(["Total Responses", "Average Duration (s)"], [total_responses, avg_duration])
ax1.set_ylabel("Count")
ax1.set_title("Survey Overview")
st.pyplot(fig1)

# Visualization: Completion Rate
st.header("Completion Rate")
fig2, ax2 = plt.subplots()
ax2.bar(["Completion Rate (%)"], [completion_rate], color='green')
ax2.set_ylabel("Percentage")
ax2.set_title("Completion Rate")
st.pyplot(fig2)

# Data Table
st.header("Survey Data")
st.dataframe(data)
