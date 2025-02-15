import streamlit as st
from packages.stock_price import get_current_price, get_market_cap
from packages.stock_data import get_stock_data
from packages.stock_display import display_stock_info, plot_stock_data, select_period

def main():
    st.title('Stock Price Tracker')

    ticker = st.text_input("Enter the stock ticker (e.g., AAPL, TSLA):", 'AAPL')
    period = select_period()

    if ticker:
        cur_price = get_current_price(ticker)
        market_cap = get_market_cap(ticker)
        data = get_stock_data(ticker, period)

        if cur_price and market_cap:
            display_stock_info(ticker, cur_price, market_cap)

        if not data.empty:
            plot_stock_data(data, ticker, period)
        else:
            st.error("Invalid ticker or no data found. Please try again.")

if __name__ == '__main__':
    main()
