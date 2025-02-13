import yfinance as yf
def get_market_cap(ticker):
    stock = yf.Ticker(ticker)
    market_cap=stock.info['marketCap']
    return market_cap
