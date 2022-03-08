class Investment:
    def share_profit(self,):
        print('>>> Profit Sharing of the investment company')


class Company:
    def share_profit(self,):
        investment = Investment()
        investment.share_profit()

company = Company()
company.share_profit()
