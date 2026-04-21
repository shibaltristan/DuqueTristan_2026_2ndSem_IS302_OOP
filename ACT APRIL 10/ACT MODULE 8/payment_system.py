class Paymenttld:
    def pay(self):
        print("Processing payment")

class CashPaymenttld(Paymenttld):
    def pay(self):
        print("Payment made using cash")

class CardPaymenttld(Paymenttld):
    def pay(self):
        print("Payment made using credit card")

paymentstld = [CashPaymenttld(), CardPaymenttld()]
for ptld in paymentstld:
    ptld.pay()