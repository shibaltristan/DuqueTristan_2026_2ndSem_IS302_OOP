class BankAccounttld:
    def __init__(self, balancetld):
        self.__balancetld = balancetld

    def deposittld(self, amounttld):
        self.__balancetld += amounttld

    def withdrawtld(self, amounttld):
        if amounttld <= self.__balancetld:
            self.__balancetld -= amounttld
        else:
            print("Insufficient funds")

    def get_balancetld(self):
        return self.__balancetld

accounttld = BankAccounttld(5000)
accounttld.deposittld(1000)
accounttld.withdrawtld(2000)
print("Balance:", accounttld.get_balancetld())