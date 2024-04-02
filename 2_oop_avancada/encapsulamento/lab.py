class AccountError(Exception):
    pass


class Account:
    def __init__(self, number_account):
        self.__number_account = number_account
        self.__balance = 0

    @property
    def number_account(self):
        return self.__number_account

    @number_account.setter
    def number_account(self, number):
        raise AccountError("It not possible change the account number")

    @number_account.deleter
    def number_account(self):
        if self.__balance > 0:
            raise AccountError("It is not possible to delete an account with a balance")

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount >= 0:
            self.__balance = amount
            if amount > 100000:
                print("#### high value deposit ####")
            elif amount < -100000:
                print("high value withdrawal")
        else:
            raise AccountError("It is not possible to carry out the operation, the balance will be negative")


account = Account(12345)
print("Account number:", account.number_account)
print("Balance:", account.balance)
print("*" * 20)
print("Balance to 1000")
account.balance += 1000
print("Account number:", account.number_account)
print("Balance:", account.balance)
print("*" * 20)
print("Balance to -200")
try:
    account.balance = -200
except AccountError as e:
    print(e)
print("Account number:", account.number_account)
print("Balance:", account.balance)
print("*" * 20)
print("Account change number")
try:
    account.number_account = 56966
except AccountError as e:
    print(e)
print("Account number:", account.number_account)
print("Balance:", account.balance)
print("*" * 20)
print("deposit to 1.000.000")
account.balance += 1000000
print("Account number:", account.number_account)
print("Balance:", account.balance)
print("*" * 20)
print("Exclude Account with balance")
try:
    del account.number_account
except AccountError as e:
    print(e)
