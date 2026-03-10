from flask import Flask, render_template, request
from trader import Trader
from market import Market

app = Flask(__name__)

trader = Trader()
market = Market()

@app.route("/")
def home():
    times, o, h, l, c = market.get_data()
    
    raw_price = c[-1]
    raw_val = float(raw_price[0]) if isinstance(raw_price, list) else float(raw_price)
    price = round(raw_val, 2)

    profits = []
    for p in trader.positions:
        profits.append(p.profit(price))

    return render_template(
        "index.html",
        times=list(times),
        close=list(c),
        price=price,
        balance=trader.balance,
        positions=trader.positions,
        profits=profits,
        history=trader.history
    )

@app.route("/trade", methods=["POST"])
def trade():
    price_str = request.form["price"].replace("[","").replace("]","")
    trader.open_trade(float(price_str), float(request.form["lot"]), request.form["type"])
    return home()

@app.route("/close", methods=["POST"])
def close():
    trader.close_trade(int(request.form["index"]), float(request.form["price"]))
    return home()

@app.route("/reset", methods=["POST"])
def reset():
    global trader
    trader = Trader() 
    return home()

if __name__ == "__main__":
    app.run(debug=True)