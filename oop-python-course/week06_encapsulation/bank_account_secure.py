class BankAccount_TLD:
    def __init__(self_TLD, balance_TLD):
        self_TLD.__balance_TLD = balance_TLD

    def deposit_TLD(self_TLD, amount_TLD):
        self_TLD.__balance_TLD += amount_TLD

    def withdraw_TLD(self_TLD, amount_TLD):
        if amount_TLD <= self_TLD.__balance_TLD:
            self_TLD.__balance_TLD -= amount_TLD
        else:
            print("Insufficient funds")

    def get_balance_TLD(self_TLD):
        return self_TLD.__balance_TLD

account_TLD = BankAccount_TLD(5000)
account_TLD.deposit_TLD(1000)
account_TLD.withdraw_TLD(2000)
print("Balance:", account_TLD.get_balance_TLD())