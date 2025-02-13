import yfinance as yf
def get_stock_data(ticker):
    stock = yf.Ticker(ticker)
    data = stock.history(period="1mo")  # Fetch 1 month of historical data
    return data
