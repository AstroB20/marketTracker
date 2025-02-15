import yfinance as yf

def get_current_price(ticker):
    stock = yf.Ticker(ticker)
    current_price = stock.history(period="1d")['Close'].iloc[-1]
    return current_price

def get_market_cap(ticker):
    stock = yf.Ticker(ticker)
    return stock.info.get('marketCap', None)
