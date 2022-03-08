class Investment:
    def share_profit(self,):
        print('>>> Profit Sharing of the investment company')

class StockHolding:
    def share_profit(self,):
        print('>>> Profit Sharing of the stock holding company')

class CompanyFactory:
    def make_company(self, company_type):
        if company_type == 'investment':
            investment = Invesment()
            return investment
        elif company_type =='stockholding':
            stockholding = StockHolding()
            return stockholding
        
    def share_profit(self, company_type):
        company = self.make_company(company_type)
        company.share_profit()

company = CompanyFactory()
company.share_profit('stockholding')

