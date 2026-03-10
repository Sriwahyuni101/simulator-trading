import yfinance as yf

class Market:

    def get_data(self):

        data = yf.download("GC=F", period="1d", interval="5m")

        times = data.index.strftime("%H:%M").tolist()

        open_price = data["Open"].values.tolist()
        high = data["High"].values.tolist()
        low = data["Low"].values.tolist()
        close = data["Close"].values.tolist()

        return times, open_price, high, low, close