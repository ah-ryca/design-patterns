from abc import ABC, abstractmethod


class Builder(ABC):
    @abstractmethod
    def table(self, ): pass

    @abstractmethod
    def select(self, ): pass

    @abstractmethod
    def where(self, ): pass

    @property
    @abstractmethod
    def get_query(self,): pass

class Sqlite(Builder):
    def table(self):
        return self
    
    def select(self):
        return self
    
    def where(self):
        return self
    
    def get_query(self):
        print(">> Sqlite query")
        


class MySql(Builder):
    def table(self):
        return self
    
    def select(self):
        return self
    
    def where(self):
        return self
    
    def get_query(self):
        print(">> MySql query")


def client(builer: Sqlite):
    query = builer.table().select().where().get_query()


sqlite = Sqlite()
client(sqlite)

mysql = MySql()
client(mysql)
