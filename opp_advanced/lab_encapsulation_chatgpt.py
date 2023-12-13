class AccountException(Exception):
    pass


class BankAccount:
    def __init__(self, account_number, balance=0):
        self._account_number = account_number
        self._balance = balance

    @property
    def account_number(self):
        return self._account_number

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, new_balance):
        if new_balance < 0:
            raise AccountException("Cannot set a negative balance.")
        self._balance = new_balance

    @account_number.setter
    def account_number(self, new_account_number):
        raise AccountException("Cannot change the account number.")

    @balance.deleter
    def balance(self):
        if self._balance != 0:
            raise AccountException("Cannot delete the account as long as the balance is not zero.")
        del self._balance

    def deposit(self, amount):
        self._balance += amount
        if amount > 100000:
            print("Audit: Large deposit detected.")

    def withdraw(self, amount):
        if self._balance - amount < 0:
            raise AccountException("Insufficient funds for withdrawal.")
        self._balance -= amount
        if amount > 100000:
            print("Audit: Large withdrawal detected.")


# Test the class behavior
try:
    account = BankAccount(account_number="12345", balance=1000)

    print("Initial Account Number:", account.account_number)
    print("Initial Balance:", account.balance)

    # Test trying to set a negative balance
    try:
        account.balance = -200
    except AccountException as e:
        print("Error:", e)

    # Test trying to set a new value for the account number
    try:
        account.account_number = "54321"
    except AccountException as e:
        print("Error:", e)

    # Test trying to deposit 1,000,000
    account.deposit(1000000)

    # Test trying to delete the account attribute containing a non-zero balance
    try:
        del account.balance
    except AccountException as e:
        print("Error:", e)

    print("Final Account Number:", account.account_number)
    print("Final Balance:", account.balance)

except AccountException as e:
    print("Error during account creation:", e)
