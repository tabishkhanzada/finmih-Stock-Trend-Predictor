# app.py
import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# ------------------------------
# Streamlit App Config
# ------------------------------
st.set_page_config(
    page_title="Stock Trend Predictor",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Stock Trend Predictor")
st.write("Enter a stock ticker symbol to get historical data and visualize the closing price trend.")

# ------------------------------
# User Input
# ------------------------------
user_input = st.text_input("Enter Stock Ticker", "AAPL")
start = st.date_input("Start Date", pd.to_datetime("2010-01-01"))
end = st.date_input("End Date", pd.to_datetime("today"))

# ------------------------------
# Fetch Data Safely
# ------------------------------
if user_input:
    try:
        # Download historical stock data
        df = yf.download(user_input.strip().upper(), start=start, end=end)

        # Check if data was returned
        if df.empty:
            st.error("❌ No data found for this ticker. Please check the symbol or date range.")
        else:
            st.success(f"✅ Data loaded for {user_input.strip().upper()}")
            
            # Show raw data
            st.subheader("Historical Data")
            st.dataframe(df)

            # Plot Closing Price
            st.subheader("Closing Price Chart")
            st.line_chart(df['Close'])

            # Optional: Show volume
            st.subheader("Volume Chart")
            st.line_chart(df['Volume'])

    except ValueError as ve:
        st.error(f"Value Error: {ve}")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")