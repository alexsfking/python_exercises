'''
Estimated time
    30-60 minutes

Level of difficulty
    Medium

Objectives
    improving the student's skills in operating with the getter, setter, and deleter
    methods;
    improving the student's skills in creating their own exceptions.

Scenario
    Implement a class representing an account exception,
    Implement a class representing a single bank account,
    This class should control access to the account number and account balance
    attributes by implementing the properties:
        it should be possible to read the account number only, not change it. In case
        someone tries to change the account number, raise an alarm by raising an
        exception;
        it should not be possible to set a negative balance. In case someone tries to
        set a negative balance, raise an alarm by raising an exception;
        when the bank operation (deposit or withdrawal) is above 100,000, then
        additional message should be printed on the standard output (screen) for
        auditing purposes;
        it should not be possible to delete an account as long as the balance is not
        zero;
    test your class behavior by:
        setting the balance to 1000;
        trying to set the balance to -200;
        trying to set a new value for the account number;
        trying to deposit 1,000,000;
        trying to delete the account attribute containing a non-zero balance.
'''


class Account_Exception(Exception):
    pass

class Bank_Account:
    def __init__(self, account_number:int, balance:int) -> None:
        self.__account_number = account_number
        self.__account_balance = balance

    @property
    def account_number(self):
        return self.__account_number
    
    @property
    def account_balance(self):
        return self.__account_balance

    @account_balance.setter
    def account_balance(self, amount:int):
        if amount < 0 :
            raise Account_Exception("Account balance cannot be negative.")
        self.__account_balance = amount

    @account_balance.deleter
    def account_balance(self):
        if self.account_balance != 0:
            raise Account_Exception("Account balance cannot be deleted while it is not zero.")
        self.__account_balance = None

    def deposit(self, amount):
        if amount > 100000:
            print("An audit will occur due to the large deposit.")
        self.account_balance += amount

    def withdrawal(self, amount):
        if amount > 100000:
            print("An audit will occur due to the large withdrawal.")
        self.account_balance += self.account_balance - amount

    @account_balance.setter
    def account_number(self, new_number):
        raise Account_Exception("An account number cannot be changed.")
    
    @account_balance.deleter
    def account_number(self):
        raise Account_Exception("An account number cannot be deleted.")
    

account_number = 739849023
balance = 1
bank_account = Bank_Account(account_number, balance)
bank_account.account_balance = 1000
bank_account.account_balance = -200
bank_account.account_number = 23
bank_account.deposit(1000000)
del bank_account.account_balance
