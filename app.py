import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import streamlit as st 
import yfinance as yf

# Date range
start = '2010-01-01'
end = '2019-12-31'

st.title('Stock Trend Analysis')

# User input
user_input = st.text_input("Enter stock ticker", 'AAPL')

# Download data
df = yf.download(user_input, start=start, end=end)

# Show data
st.subheader('Data from 2010-2019')
st.write(df.describe())

# Closing price chart
st.subheader('Closing price vs time chart')
fig = plt.figure(figsize=(12,6))
plt.plot(df.Close)
plt.xlabel('Time')
plt.ylabel('Price')
st.pyplot(fig)

# 100 MA
st.subheader('Closing price vs time chart with 100MA')
ma100 = df.Close.rolling(100).mean()

fig = plt.figure(figsize=(12,6))
plt.plot(df.Close, label='Closing Price')
plt.plot(ma100, label='100 MA')
plt.legend()
st.pyplot(fig)

# 100 MA + 200 MA
st.subheader('Closing price vs time chart with 100MA and 200MA')
ma200 = df.Close.rolling(200).mean()

fig = plt.figure(figsize=(12,6))
plt.plot(df.Close, label='Closing Price')
plt.plot(ma100, label='100 MA')
plt.plot(ma200, label='200 MA')
plt.legend()
st.pyplot(fig)

# Train-test split visualization
st.subheader("Train vs Test Data Visualization")

data_training = pd.DataFrame(df['Close'][0:int(len(df)*0.70)])
data_testing = pd.DataFrame(df['Close'][int(len(df)*0.70):])

fig = plt.figure(figsize=(12,6))
plt.plot(data_training, label='Training Data')
plt.plot(range(len(data_training), len(df)), data_testing, label='Testing Data')
plt.legend()
st.pyplot(fig)

st.success("App is running successfully without ML model 🚀")