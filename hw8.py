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

class Bank_account():

    def __init__(self, name, balance = 0):

        self.name = name
        self.balance = float(balance)

    def adds_deposit(self, deposit):
        self.balance = float(deposit) + self.balance
        return self.balance

    def subtracts_withdrawals(self, withdrawal):
        self.balance = self.balance - float(withdrawal)
        if self.balance > 0:
            return self.balance
        else:
            self.balance = (self.balance + withdrawal)
            print("You can not withdraw ${:.2f}, you have insufficient funds, with your current balance of ${:.2f}. \n".format(withdrawal, self.balance))
            # return (self.balance)


#error checking for balance < 0
# assign a name to Banking
#name = input("What is the name of your account?\n")
#acct1 = Bank_account(name)

acct1 = Bank_account("Helen")
print("Your account name is {}, and your balance is {:.2f}. \n".format(acct1.name, acct1.balance))

# Track deposits
acct1_deposit = acct1.adds_deposit(250.00)
print("The amount of your deposit is ${:.2f} and your new balance is {:.2f} \n".format(acct1_deposit, acct1.balance))

# Print balance
# print("$", acct1.balance, "is your account balance. \n")

# Track withdrawals
acct1_withdrawal = acct1.subtracts_withdrawals(200.00)
print("The amount of your withdrawal ia ${:.2f} and your new balance is ${:.2f} \n".format(acct1_withdrawal, acct1.balance))

# Print balance
# print(acct1.balance, "is your account balance. \n")

# Another withdrawal that is greater than balance
acct1.subtracts_withdrawals(60.00)

# Print balance
print(acct1.balance, "is your account balance. \n")


