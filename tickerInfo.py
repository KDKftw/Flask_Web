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
        print("ticker_name= " + self.name, "|| ", "buy_date= " + str(self.buyDate), "|| " , "amount_of_shares= " + str(self.amount), "|| " , "total= " + str(self.total), "|| " , "fee= " + str(self.fee),"|| "
              , "total_paid= " + str(self.total_paid()), "|| ", "stonks_days_left= " + str(self.stonksDateDayCount()) )

    def stonksDate(self):
        stonksDate = self.buyDate.replace(self.buyDate.year + 3)
        return stonksDate

    def stonksDateDayCount(self):
        d0 = date.today()
        ##d0 = d0.strftime("%Y-%m-%d")
        ##d0 = int(d0)
        ##d0 = date(d0)
        d1 = self.stonksDate()
        dayCount = d1 - d0
        return dayCount

nakup0 = Trade("MMT", date(2021, 10, 5), 93, 605.01, 7.95)
nakup1 = Trade("LTC", date(2021, 9, 30), 34, 1085.41, 7.95)
nakup2 = Trade("DX", date(2021, 9, 28), 40, 707.95, 7.95)
nakup3 = Trade("PSEC", date(2021, 9, 28), 70, 557.45, 7.95)
nakup4 = Trade("ARR", date(2021, 9, 28), 90, 985.35, 7.95)


nakup0.print_values()
nakup1.print_values()
nakup2.print_values()
nakup3.print_values()
nakup4.print_values()






#print(nakup0.fee)
#print(nakup0.buyDate)
#print(nakup0.stonksDate())
#print(nakup0.stonksDateDayCount())