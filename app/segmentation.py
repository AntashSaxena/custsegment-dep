import streamlit as st
import pandas as pd
import numpy as np
import joblib

kmeans = joblib.load("models/kmeans_model.pkl")
scaler = joblib.load("models/scaler.pkl")

st.title("Customer Segmentation App")
st.write("Enter Customer details to predict the segment.")

age = st.number_input("Age", min_value=18, max_value=100, value=35)
income = st.number_input("Income", min_value=0, max_value=2000000, value=50000)
total_spending = st.number_input("Total_Spending (Sum of Purchases)", min_value=0, max_value=200000, value=10000)
numwebpurchases = st.number_input("Number of web purchase", min_value=0, max_value=100, value=10)
numstorepurchases = st.number_input("Number of Store purchase", min_value=0, max_value=1000, value=10)	 
numwebvisitsmonth = st.number_input("Number of Web Visits per month", min_value=0, max_value=100, value=10)
recency = st.number_input("Recency days Since Last Purchase", min_value=0, max_value=365, value=30)
	
input_data = pd.DataFrame({
    "Age": [age],
    "Income": [income],
    "Total_Spending": [total_spending],	
    "NumWebPurchases": [numwebpurchases],
    "NumStorePurchases": [numstorepurchases],	
    "NumWebVisitsMonth": [numwebvisitsmonth],
    "Recency": [recency]
})
input_scaled = scaler.transform(input_data)

if st.button("Predict Segment"):
    cluster = kmeans.predict(input_scaled)[0]
    st.success(f"Predicted Segment: Cluster {cluster}")
	
    st.write(""" 
                Cluster 0: High income High spending -> premium customer"""'\n\n'
                """Cluster 1: High spending"""'\n\n'
                """Cluster 2: High web purchases low store purchases -> Digital Buyers"""'\n\n'
                """Cluster 3: High income, Low spending -> Potential Customers"""'\n\n'
                """Cluster 4: Low income, High Spending -> Bargain Hunters"""'\n\n'   
                """Cluster 5: Low recency inactive -> Dormant Customers"""'\n\n'
                """Cluster 6: Low income, Low Spending -> Budget Customers"""'\n\n'
               )