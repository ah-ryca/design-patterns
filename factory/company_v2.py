class Investment:
    def share_profit(self,):
        print('>>> Profit Sharing of the investment company')

class StockHolding:
    def share_profit(self,):
        print('>>> Profit Sharing of the stock holding company')

class Company:
    def share_profit(self, company_type):
        if company_type == 'investment':
            investment = Investment()
            investment.share_profit()
        elif company_type == 'stockholding':
            stockholding = StockHolding()
            stockholding.share_profit()


company = Company()
company.share_profit('investment')
