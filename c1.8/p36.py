class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
    
    def display(self):
        print(f"Account Number: {self.account_number}, Balance: {self.balance}")
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}. New Balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: {amount}. New Balance: {self.balance}")
        else:
            print("Invalid withdrawal amount.")
    

a1 = Account("123456", 500)
a1.display()
a1.deposit(200)
a1.withdraw(100)