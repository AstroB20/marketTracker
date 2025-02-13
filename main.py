import streamlit as st
import matplotlib.pyplot as plt
import get_stock_data
import get_market_cap
import get_current_price

def plot_stock_data(data, ticker):
    fig, ax = plt.subplots()
    ax.plot(data.index, data['Close'], label=f'{ticker} Close', color='blue')
    ax.set_title(f'{ticker} Stock Price (Last Month)')
    ax.set_xlabel('Date')
    ax.set_ylabel('Closing Price (USD)')
    ax.grid(True)
    ax.legend()
    st.pyplot(fig)

def main():
    st.title('Stock Price Tracker')
    ticker = st.text_input("Enter the stock ticker (e.g., AAPL, TSLA):", 'AAPL')
    
    if ticker:
        curPrice = get_current_price(ticker)
        st.write(f"Current Stock Price is : {curPrice:.2f}")
        st.write(f"Market cap is : {get_market_cap(ticker)/1_000_000_000:.2f}B")
        st.write(f"Fetching data for {ticker}...")
        data = get_stock_data(ticker)
        if data.empty:
            st.error("Invalid ticker or no data found. Please try again.")
        else:
            plot_stock_data(data, ticker)

# Run the Streamlit app
if __name__ == "__main__":
    main()
