from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def connect(self): pass
    @abstractmethod
    def query(self, sql:str): pass
    @abstractmethod
    def close(self): pass

    #Template method (concrete method using abstract ones)
    def execute(self, sql:str):
        self.connect()
        result = self.query(sql)
        self.close()
        return result


class MYSQLDB(Database):
    def connect(self):
        print("Connecting to MySQL database")

    def query(self, sql:str):
        print(f"MySQL executing: {sql}")
        return []

    def close(self):
        print("Closing MySQL database")

db = MYSQLDB()
db.execute("SELECT * FROM users")