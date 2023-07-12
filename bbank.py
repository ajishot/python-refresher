class Bank:
    def __init__(self, balance, name, number):
        self.balance = balance
        self.name = name
        self.number = number
    
    def withdraw(self, w):
        if w > self.balance:
            raise ValueError('Withdrawal is greater than balance')
        else:
            self.balance -= w

    def deposit(self, d):
        self.balance += d

    def balance(self):
        print(self.balance)