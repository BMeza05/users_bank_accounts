class User:
    def __init__(self, name, email, bank_name):
        self.name = name
        self.email = email
        self.bank_name = bank_name
        self.account = BankAccount(int_rate=.03, balance=0)
    def deposit(self):
        self.account.make_deposit(1)
    
    def withdraw(self):
        self.account.make_withdrawl(1)

    def display_user_balance(self):
        self.account.display_account_info
    

class BankAccount:
    def __init__(self, int_rate, balance):
        self.balance = balance
        self.int_rate = int_rate
        balance == 0
        int_rate = .03
    
    def make_deposit(self, amount):
        self.balance += amount

    def make_withdrawl(self, amount):
        self.balance -= amount

    def display_account_info(self):
        self.balance
        print(self.balance)

    def yield_interest(self, int_rate):
        self.balance // int_rate

