class Trade:

    def __init__(self, entry_price, lot, trade_type):

        self.entry_price = entry_price
        self.lot = lot
        self.type = trade_type

    def profit(self, current_price):

        if self.type == "buy":

            return (current_price - self.entry_price) * self.lot * 100

        else:

            return (self.entry_price - current_price) * self.lot * 100