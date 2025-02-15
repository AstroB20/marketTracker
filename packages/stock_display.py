import streamlit as st
import matplotlib.pyplot as plt

def display_stock_info(ticker, cur_price, market_cap, data):
    st.title('Stock Price Tracker')
    st.write(f"Fetching data for {ticker}...")
    
    if cur_price is not None:
        st.write(f"Current Stock Price is: {cur_price:.2f}")

    if market_cap is not None:
        st.write(f"Market Cap is: {market_cap / 1_000_000_000:.2f}B")

    if data.empty:
        st.error("Invalid ticker or no data found. Please try again.")
    else:
        plot_stock_data(data, ticker)

def plot_stock_data(data, ticker):
    fig, ax = plt.subplots()
    ax.plot(data.index, data['Close'], label=f'{ticker} Close', color='blue')
    ax.set_title(f'{ticker} Stock Price (Last Month)')
    ax.set_xlabel('Date')
    ax.set_ylabel('Closing Price (USD)')
    ax.grid(True)
    ax.legend()
    st.pyplot(fig)
