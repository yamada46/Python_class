'''
Create a Banking class that does the following:
Tracks an initial account balance
Tracks deposits in the account
Tracks withdrawals to the account
Prints out a current balance
Prints an error message if someone tries to withdraw more money than what is currently in the account
'''
class BankAccount:
    def __init__(self, name = "Unknown", balance = 0.0):
        self.balance = balance
        self.name = name

    def deposit(self, amount):
        pass

    def withdraw(self, amount):
        #throw an error if amount > balance
        pass

    def current_balance(self):
        return self.current_balance()

if __name__== "__main__"
