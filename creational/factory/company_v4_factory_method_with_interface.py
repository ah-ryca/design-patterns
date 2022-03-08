from abc import ABC, abstractmethod

class Company(ABC):
    @abstractmethod
    def share_profit(self,):
        pass

class Investment(Company):
    def share_profit(self,):
        print('>>> Profit Sharing of the investment company')

class StockHolding(Company):  
    def share_profit(self,):
        print('>>> Profit Sharing of the stock holding company')

class Company1(Company):  
    def share_profit(self,):
        print('>>> Profit Sharing of the company 1')

class CompanyFactory(ABC):

    @abstractmethod
    def make_company(self): 
        pass

    def share_profit(self):
        company = self.make_company()
        company.share_profit()
    
class InvestmentFactory(CompanyFactory):
    def make_company(self):
        investment = Investment()
        return investment

    
class StockHoldingFactory(CompanyFactory):
    def make_company(self):
        stockholding = StockHolding()
        return stockholding

    
class Company1Factory(CompanyFactory):
    def make_company(self):
        company1 = Company1()
        return company1

investment = InvestmentFactory()
investment.share_profit()


stockholding = StockHoldingFactory()
stockholding.share_profit()


company1 = Company1Factory()
company1.share_profit()
