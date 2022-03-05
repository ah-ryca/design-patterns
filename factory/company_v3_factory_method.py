class Invesment:
    def do_profit_sharing(self,):
        print('>> Profit Sharing with investment company...')

class Stockholding:
    def do_profit_sharing(self,):
        print('>> Profit Sharing with stockholding company...')

class CompanyFactory:
    def make_company(self,company_type):
        if company_type=='investment':
            investment = Invesment()
            return investment
        elif company_type =='stockholding':
            stockholding = Stockholding()
            return stockholding
    def do_profit_sharing(self, company_type):
        company = self.make_company(company_type)
        company.do_profit_sharing()

company = CompanyFactory()
company.do_profit_sharing('stockholding')

