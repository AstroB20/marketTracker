import streamlit as st
from packages.stock_price import get_current_price, get_market_cap
from packages.stock_data import get_stock_data
from packages.stock_display import display_stock_info

def main():
    ticker = st.text_input("Enter the stock ticker (e.g., AAPL, TSLA):", 'AAPL')
    if ticker:
        cur_price = get_current_price(ticker)
        market_cap = get_market_cap(ticker)
        data = get_stock_data(ticker)

        display_stock_info(ticker, cur_price, market_cap, data)

if __name__ == '__main__':
    main()
