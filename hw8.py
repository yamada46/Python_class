'''

Create a Banking class that does the following:
Tracks an initial account balance
Tracks deposits in the account
Tracks withdrawals to the account
Prints out a current balance
Prints an error message if someone tries to withdraw more money than what is currently in the account
'''

'''
hw8.py
This script is tracking a banking account, deposits, withdrawals, resulting balance, and error messages if user is trying to withdraw more money than is in the
account
'''
#!/usr/bin/env python3

class Bank():
    Bank.account = 0
    def __init__(self, account):
        self.account = account

    def balance(self, balance):
        self.balance = float(balance)

    def deposit(self, deposit):
        self.deposit = float(deposit)

    def withdraw(self, withdrawal):
        self.withdrawal = float(withdrawal)

    def add(self, balance, deposit):
        adds = (self.balance + self.deposit)
        return float(adds)

#    def subtract(self, balance, withdrawal):
#       float(subtracts) = (self.balance - self.withdrawal)
#       if balance less than 0:
#           return subtracts
#       else:
#           input("You can not withdraw ${} amount, you only have ${} in your account. Try another withdrawal amount: $\n")

acct1 = Bank_account(Bob)

acct1.balance = 246.35

acct1.deposit = 250.00








