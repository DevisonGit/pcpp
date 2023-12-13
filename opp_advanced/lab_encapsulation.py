class AccountError(Exception):
    pass

class BankAccount:
    def __init__(self, number) -> None:
        self.__account_number = number
        self.__account_balance = 0

    @property
    def account_number(self):
        return self.__account_number
    
    @property
    def account_balance(self):
        return self.__account_balance
    
    @account_number.setter
    def account_number(self, number):
        raise AccountError("Not possible change account number")
    
    @account_balance.setter
    def account_balance(self, balance):
        if balance >= 0:
            if balance > 100000:
                print("above 100.000 for auditing purpose")
            self.__account_balance = balance
        else:
          raise AccountError("Not be possible to set a negative balance")
        
    @account_balance.deleter
    def account_balance(self):
        if self.__account_balance > 0:
            raise AccountError("Not be possible to delete an account as long the balance is not zero")
        self.__account_number = None
        self.__account_balance = None



our_account = BankAccount(1234)
print('Account number:', our_account.account_number)
print('Account balance:', our_account.account_balance)
print("="*30)

print("Setting the balance to 1000")
our_account.account_balance = 1000
print('Account number:', our_account.account_number)
print('Account balance:', our_account.account_balance)
print("="*30)


print("Trying to set the balance -200")
try:
    our_account.account_balance = -200
except AccountError as e:
    print("Result", e)
print('Account number:', our_account.account_number)
print('Account balance:', our_account.account_balance)
print("="*30)

print("Trying to set a new value for the account number")
try:
    our_account.account_number = 5678
except AccountError as e:
    print("Result", e)
print('Account number:', our_account.account_number)
print('Account balance:', our_account.account_balance)
print("="*30)

print("Setting the balance to 1000000")
our_account.account_balance = 1000000
print('Account number:', our_account.account_number)
print('Account balance:', our_account.account_balance)
print("="*30)


print("trying to delete the account attribute containg a non-zero balance")
try:
    del our_account.account_balance
except AccountError as e:
    print(e)
print('Account number:', our_account.account_number)
print('Account balance:', our_account.account_balance)
print("="*30)
