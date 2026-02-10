
class Payment:
    def pay(self):
        print("Processing payment...")
class GooglePay(Payment):
    def pay(self):
        print("Payment done using GooglePay.")
class PhonePe(Payment):
    def pay(self):
        print("Payment done using PhonePe.")
class CreditCard(Payment):
    def pay(self):
        print("Payment done using Credit Card.")
if __name__ == "__main__":
    p1 = GooglePay()
    p2 = PhonePe()
    p3 = CreditCard()
    p1.pay()
    p2.pay()
    p3.pay()
