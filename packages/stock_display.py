import streamlit as st
import matplotlib.pyplot as plt

def display_stock_info(ticker, cur_price, market_cap):
    st.write(f"Current Stock Price: ${cur_price:.2f}")
    st.write(f"Market Cap: ${market_cap / 1_000_000_000:.2f}B")

def plot_stock_data(data, ticker, period):
    fig, ax = plt.subplots()
    ax.plot(data.index, data['Close'], label=f'{ticker} Close', color='blue')
    ax.set_title(f'{ticker} Stock Price - {period.capitalize()} View')
    ax.set_xlabel('Date')
    ax.set_ylabel('Closing Price (USD)')
    ax.grid(True)
    ax.legend()
    st.pyplot(fig)

def select_period():
    period_map = {
        "Day": "1d",
        "Week": "1wk",
        "Month": "1mo",
        "Year": "1y"
    }
    period = st.radio("Select Time Period", list(period_map.keys()), horizontal=True)
    return period_map[period]
