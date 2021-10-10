from datetime import date

class Trade():
    def __init__(self, name, buyDate, amount, total, fee):
        self.name = name
        self.buyDate = buyDate
        self.amount = amount
        self.total = total
        self.fee = fee

    def total_paid(self):
        total_paid = self.total + self.fee
        return(total_paid)

    def print_values(self):
        print("ticker_name= " + self.name, "|| ", "buy_date= " + self.buyDate, "|| " , "amount_of_shares= " + str(self.amount), "|| " , "total= " + str(self.total), "|| " , "fee= " + str(self.fee),"|| "
              , "total_paid= " + str(self.total_paid()) )

    def tryKek(self):
        print("fee= " + str(self.fee))

    def getDate(self):
        getDate = date(int(self.buyDate))
        return getDate

nakup0 = Trade("MMT", "2021, 10, 5", 93, 605, 7.95)

print(nakup0)
nakup0.print_values()
print(nakup0.fee)
##nakup0.getDate()

datumtest= date(2021, 10, 5)
print(datumtest)
print(type(datumtest))