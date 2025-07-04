import streamlit as st
import pandas as pd
from modules import data_aggregation, risk_calculation, correlation_analysis, stress_testing

st.title("Insurance Portfolio Risk Management Dashboard")

# Load data
data = pd.read_csv("data/sample_policy_data.csv")

# Aggregate data
aggregated_data = data_aggregation.aggregate(data)

# Calculate risk
risk_metrics = risk_calculation.calculate(aggregated_data)

# Analyze correlations
correlations = correlation_analysis.analyze(aggregated_data)

# Stress test
stress_results = stress_testing.run(aggregated_data)

# Display
st.subheader("Risk Metrics")
st.write(risk_metrics)

st.subheader("Correlation Matrix")
st.write(correlations)

st.subheader("Stress Test Results")
st.write(stress_results)
