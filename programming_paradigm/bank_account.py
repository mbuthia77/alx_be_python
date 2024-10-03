class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance
    
    def deposit(self, amount):
        self.account_balance += amount
    
    def withdraw(self, amount):
        if self.account_balance >= amount: 
            self.account_balance -= amount
            return True
        else:
            return False
    
    
    def display_balance(self):
        print("Current Balance: $", {self.account_balance,'.2f'})

#Testing code
#Chege = BankAccount(100)
#Chege.deposit(200)
#Chege.withdraw(50)
#Chege.display_balance()
