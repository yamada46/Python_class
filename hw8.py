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
        self.balance = (self.balance - withdrawal)
        if self.balance > 0:
            return self.balance
        else:
            print("You can not withdraw ${:.2f}, you will be ${} overdrawn in your account, which would incur a penalty fee. \n".format(withdrawal, self.balance))
            return (self.balance + withdrawal)

        # else:
        #     # count = 0
        #     for count < 4:
        #         print("You can not withdraw ${:.2f}, you will be ${} overdrawn in your account, which would incur a penalty fee. \n".format(withdrawal, self.balance))
        #         withdrawal2 = input("Try another withdrawal amount: $\n")
        #     else:
        #         print("You have exceeded the number of withdrawal inputs. \n ")
        #         count = count + 1
        #         return error_message


#error checking for balance < 0
# assign a name to Banking
acct1 = Bank_account("Helen")
print(acct1.balance, "is your current account balance. \n")

acct1_deposit = acct1.adds_deposit(250.00)
print("${:.2f} is the amount of your deposit. \n".format(acct1_deposit))
print("$", acct1.balance, "is your new account balance. \n")

acct1.subtracts_withdrawals(200.00)

print(acct1.balance, "is your new account balance. \n")

acct2 = Bank_account("Lynne", balance = 350.0)
acct2.balance






