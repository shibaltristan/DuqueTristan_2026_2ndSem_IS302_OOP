class Payment_TLD:
    def pay_TLD(self_TLD):
        print("Processing payment")

class CashPayment_TLD(Payment_TLD):
    def pay_TLD(self_TLD):
        print("Payment made using cash")

class CardPayment_TLD(Payment_TLD):
    def pay_TLD(self_TLD):
        print("Payment made using credit card")

payments_TLD = [CashPayment_TLD(), CardPayment_TLD()]
for p_TLD in payments_TLD:
    p_TLD.pay_TLD()