from abc import ABC, abstractmethod

class Payment(ABC):
  @abstractmethod
  def payment():
    pass

# Below payment classes implements the above abstract class.
# These classes overrides the "payment" method of the abstract class. This is called method overriding.



class CreditCard(Payment):
  def payment(self):
    print("Paying via credit card")

class InternetBanking(Payment):
  def payment(self):
    print("Paying via internet banking")

# If we need to extend the payment method to UPI just implement UPI class
# Here we are extending payment methods without modifying the existing classes.
# The makePayment class implements the "payment" method

class UPI(Payment):
  def payment(self):
    print("Paying via UPI")


if __name__=="__main__":
  def makePayment(paymentMethod: Payment):
    paymentMethod.payment()

  upi = UPI()
  makePayment(upi)
