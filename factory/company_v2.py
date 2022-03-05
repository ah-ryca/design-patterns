class Invesment:
    def do_profit_sharing(self,):
        print('>> Profit Sharing with investment company...')

class Stockholding:
    def do_profit_sharing(self,):
        print('>> Profit Sharing with stockholding company...')

class Company:
    def do_profit_sharing(self,company_type):
        if company_type=='investment':
            investment = Invesment()
            investment.do_profit_sharing()
        elif company_type =='stockholding':
            stockholding = Stockholding()
            stockholding.do_profit_sharing()


company = Company()
company.do_profit_sharing('investment')
