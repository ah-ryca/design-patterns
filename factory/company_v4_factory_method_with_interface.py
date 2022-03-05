from abc import ABC,abstractmethod

class BigCompany(ABC):
    @abstractmethod
    def do_profit_sharing(self,):
        pass

class Invesment(BigCompany):
    def do_profit_sharing(self,):
        print('>> Profit Sharing with investment company...')

class Stockholding(BigCompany):  
    def do_profit_sharing(self,):
        print('>> Profit Sharing with stockholding company...')

class Company1(BigCompany):  
    def do_profit_sharing(self,):
        print('>> Profit Sharing with Company1 company...')

class CompanyFactory(ABC):

        @abstractmethod
        def make_company(self): 
            pass

        def do_profit_sharing(self):
            company = self.make_company()
            company.do_profit_sharing()
    
class InvestmentFactory(CompanyFactory):
    def make_company(self):
        investment = Invesment()
        return investment

    
class StockholdingFactory(CompanyFactory):
    def make_company(self):
        stockholding = Stockholding()
        return stockholding

    
class Company1Factory(CompanyFactory):
    def make_company(self):
        company1 = Company1()
        return company1

investment = InvestmentFactory()
investment.do_profit_sharing()


stockholding = StockholdingFactory()
stockholding.do_profit_sharing()


company1 = Company1Factory()
company1.do_profit_sharing()
