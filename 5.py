class Account:

    def __init__(self,balance):
        self.__balance=balance

    def deposit(self,amount):
        self.__balance+=amount

    def getbalance(self):
        return self.__balance

bal=Account(30000)
bal.deposit(3000)
print(bal.getbalance())
