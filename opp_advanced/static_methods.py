class Bank_Account:
    def __init__(self, iban) -> None:
        print("__init__ called")
        self.iban = iban

    @staticmethod
    def validate(iban):
        if len(iban) == 20:
             return True
        else:
            return False
        
account_numbers = ['8' * 20, '7' * 4, '2222']

for element in account_numbers:
    if Bank_Account.validate(element):
        print("we can use", element, "to create a bank account")
    else:
        print("the account number", element, "is invalid")
