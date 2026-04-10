class BankAccounttld:
    def __init__(self, account_name, balance):
        self.account_name = account_name
        self.balance = balance
    
    def deposittld(self, amount):
        self.balance += amount
        print("Deposit successful")
    
    def withdrawtld(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal successful")
        else:
            print("Insufficient balance")
    
    def display_balancetld(self):
        print("Balance:", self.balance)

accounttld = BankAccounttld("Juan", 5000)
accounttld.deposittld(1000)
accounttld.withdrawtld(2000)
accounttld.display_balancetld()
