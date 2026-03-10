from trade import Trade

class Trader:

    def __init__(self):
        self.balance = 10000
        self.leverage = 100
        self.positions = []
        self.history = []

    def open_trade(self, price, lot, trade_type):
        margin = (lot * 1000) / self.leverage

        if self.balance >= margin:
            trade = Trade(price, lot, trade_type)
            self.positions.append(trade)
            self.balance -= margin
        else:
            print("Saldo tidak cukup untuk membuka posisi!")

    def close_trade(self, index, price):
     
        if 0 <= index < len(self.positions):
            
            trade = self.positions.pop(index)
            profit = trade.profit(price)

            margin_refund = (trade.lot * 1000 / self.leverage)
            self.balance += profit + margin_refund

            self.history.append({
                "type": trade.type,
                "entry": trade.entry_price,
                "exit": price,
                "lot": trade.lot,
                "profit": profit
            })
        else:
            
            print(f"Peringatan: Posisi dengan index {index} sudah tidak ada.")