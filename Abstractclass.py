from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> bool:
        pass

    @abstractmethod
    def refund(self, transaction_id: str) -> bool:
        pass

class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        # Call Stripe / Razorpay / etc.
        print(f"Charging ₹{amount} via Credit Card")
        return True

    def refund(self, transaction_id):
        print(f"Refunding {transaction_id}")
        return True

class UPIProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Collecting ₹{amount} via UPI")
        return True

    def refund(self, transaction_id):
        # UPI refund logic
        return True