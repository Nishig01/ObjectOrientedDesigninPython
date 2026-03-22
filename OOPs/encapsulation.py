class BankAccount:
    def __init__(self, owner:str, balance:float=0):
        self._owner = owner
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance #getter controlled access

    @balance.setter
    def balance(self, amount:float):
        if amount <0:
            raise ValueError("Balance cannot be negative")
        self.__balance = amount #setter -with validation

    def deposit(self, amount: float):
        if amount < 0:
            raise ValueError("Deposit must be positive")
        self.__balance += amount

    def withdraw(self, amount: float):
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount

acc = BankAccount("Nishi", 10000)
print(acc.balance)
acc.deposit(100)
print(acc.balance)
acc.withdraw(200)
print(acc.balance) # (using property getter)

