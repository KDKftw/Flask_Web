from datetime import date

class Trade():
    instances = []
    def __init__(self, name, buyDate, amount, price, total, fee):
        self.name = name
        self.buyDate = buyDate
        self.amount = amount
        self.price = price
        self.total = total
        self.fee = fee
        self.__class__.instances.append(self)

    def total_paid(self):
        total_paid = self.total + self.fee
        return(total_paid)

    def print_values(self):
        print("ticker_name= " + self.name, "|| ", "buy_date= " + str(self.buyDate), "|| " , "amount_of_shares= " + str(self.amount),  "price_bought= " + str(self.price), "|| " , "total= " + str(self.total), "|| " , "fee= " + str(self.fee),"|| "
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
    def returnValuesInList(self):

        return ([self.name, self.buyDate, self.amount, self.price, self.total, self.fee])

    #diviList = []
    def dividends(self, cleanDivi):
        self.diviList = [cleanDivi]
        self.diviList.append(cleanDivi)
        return(self.diviList)

    def dividendsList(self):
        self.diviList

nakup0 = Trade("MMT", date(2021, 10, 5), 93, 6.42, 605.01, 7.95)
nakup1 = Trade("LTC", date(2021, 9, 30), 34, 31.69, 1085.41, 7.95)
nakup2 = Trade("DX", date(2021, 9, 28), 40, 17.50, 707.95, 7.95)
nakup3 = Trade("PSEC", date(2021, 9, 28), 70, 7.85, 557.45, 7.95)
nakup4 = Trade("ARR", date(2021, 9, 28), 90, 10.86, 985.35, 7.95)

bigDeal = [nakup0, nakup1, nakup2, nakup3, nakup4]

nakup5 = Trade("O", date(2021, 9, 24), 11, 66.58, 740.33, 7.95)
nakup6 = Trade("ORC", date(2021, 8, 20), 100, 4.9, 497.95, 7.95)
nakup7 = Trade("HRZN", date(2021, 10, 20), 73, 17.10, 1256.25, 7.95)

allDeals = [nakup0, nakup1, nakup2, nakup3, nakup4, nakup5, nakup6, nakup7]

nakup0.print_values()
nakup1.print_values()
nakup2.print_values()
nakup3.print_values()
nakup4.print_values()
nakup5.print_values()
nakup6.print_values()
nakup7.print_values()

#print(Trade.instances[x].returnValuesInList())

#print(nakup0.fee)
#print(nakup0.buyDate)
#print(nakup0.stonksDate())
#print(nakup0.stonksDateDayCount())

TradeInst = Trade.instances
def returnActualValues(x):
    x = 0

    for _ in TradeInst:
        return(Trade.instances[x].returnValuesInList())
        print(Trade.instances[x].returnValuesInList())
        x = x + 1

print(Trade.instances[0].returnValuesInList())
returnActualValues(0)


nakup0.dividends(40)
nakup0.dividends(13)
nakup1.dividends(2)
print(nakup1.diviList)
print(nakup0.diviList)
