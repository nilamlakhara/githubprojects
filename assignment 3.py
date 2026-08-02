from abc import ABC, abstractmethod
import functools
import logging

logging.basicConfig(level=logging.INFO, format="[LOG] %(message)s")


def log_transaction(func):
    @functools.wraps(func)
    def wrapper(self, amount: float, *args, **kwargs):
        logging.info(f"Initiating payment via {self.__class__.__name__}...")
        result = func(self, amount, *args, **kwargs)
        logging.info("Payment completed successfully.\n")
        return result

    return wrapper


class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float) -> bool:
        pass



class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number: str, holder: str):
        self.card_number = card_number
        self.holder = holder

    
    def pay(self, amount: float) -> bool:
        print(
            f"Paid ${amount:.2f} using Card ending in {self.card_number[-4:]}"
        )
        return True


class PayPalPayment(PaymentStrategy):
    def __init__(self, email: str):
        self.email = email

    @log_transaction
    def pay(self, amount: float) -> bool:
        print(f"Paid ${amount:.2f} using PayPal ({self.email})")
        return True


class UPIPayment(PaymentStrategy):
    def __init__(self, upi_id: str):
        self.upi_id = upi_id

    @log_transaction
    def pay(self, amount: float) -> bool:
        print(f"Paid ${amount:.2f} using UPI ({self.upi_id})")
        return True


class NetBankingPayment(PaymentStrategy):
    def __init__(self, bank_name: str, account_no: str):
        self.bank_name = bank_name
        self.account_no = account_no

    @log_transaction
    def pay(self, amount: float) -> bool:
        print(f"Paid ${amount:.2f} using Net Banking ({self.bank_name})")
        return True



class PaymentProcessor:
    _registry = {}

    def __init__(self, strategy: PaymentStrategy = None):
        self._strategy = strategy

    @classmethod
    def register_strategy(cls, name: str, strategy_cls):
        """Classmethod to register strategies into registry."""
        cls._registry[name.lower()] = strategy_cls

    @classmethod
    def create_strategy(cls, name: str, **kwargs) -> PaymentStrategy:
        """Factory method to instantiate registered strategies."""
        strategy_cls = cls._registry.get(name.lower())
        if not strategy_cls:
            raise ValueError(f"Strategy '{name}' not found.")
        return strategy_cls(**kwargs)

    def set_strategy(self, strategy: PaymentStrategy):
        """Switch strategy dynamically at runtime."""
        self._strategy = strategy

    def process_payment(self, amount: float):
        if not self._strategy:
            raise RuntimeError("No strategy set!")
        return self._strategy.pay(amount)



if __name__ == "__main__":
    # Register strategies
    PaymentProcessor.register_strategy("credit_card", CreditCardPayment)
    PaymentProcessor.register_strategy("paypal", PayPalPayment)
    PaymentProcessor.register_strategy("upi", UPIPayment)
    PaymentProcessor.register_strategy("net_banking", NetBankingPayment)

    processor = PaymentProcessor()

   
    upi = PaymentProcessor.create_strategy("upi", upi_id="user@upi")
    processor.set_strategy(upi)
    processor.process_payment(450.00)

   
    card = PaymentProcessor.create_strategy(
        "credit_card", card_number="1234567890123456", holder="Alex"
    )
    processor.set_strategy(card)
    processor.process_payment(1200.00)
