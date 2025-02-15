import streamlit as st
from packages.stock_price import get_current_price, get_market_cap
from packages.stock_data import get_stock_data
from packages.stock_plot import plot_stock_data


def main():
    st.title('Stock Price Tracker')
    ticker = st.text_input("Enter the stock ticker (e.g., AAPL, TSLA):", 'AAPL')
    
    if ticker:
        cur_price = get_current_price(ticker)
        market_cap = get_market_cap(ticker)
        data = get_stock_data(ticker)
        
        if cur_price is not None:
            st.write(f"Current Stock Price is: {cur_price:.2f}")

        if market_cap is not None:
            st.write(f"Market Cap is: {market_cap / 1_000_000_000:.2f}B")

        if data.empty:
            st.error("Invalid ticker or no data found. Please try again.")
        else:
            plot_stock_data(data, ticker)

if __name__ == '__main__':
    main()
