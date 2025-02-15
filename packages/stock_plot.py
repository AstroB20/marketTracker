import matplotlib.pyplot as plt
import streamlit as st

def plot_stock_data(data, ticker):
    fig, ax = plt.subplots()
    ax.plot(data.index, data['Close'], label=f'{ticker} Close', color='blue')
    ax.set_title(f'{ticker} Stock Price (Last Month)')
    ax.set_xlabel('Date')
    ax.set_ylabel('Closing Price (USD)')
    ax.grid(True)
    ax.legend()
    st.pyplot(fig)
