import yfinance as yf
def get_current_price(ticker):
    stock = yf.Ticker(ticker)
    current_price = stock.history(period="1d")['Close'].iloc[-1]  # Get the most recent close price
    return current_price