class Invesment:
    def do_profit_sharing(self,):
        print('>> Profit Sharing with investment company')


class Company:
    def do_profit_sharing(self,):
        investment = Invesment()
        investment.do_profit_sharing()

company = Company()
company.do_profit_sharing()
