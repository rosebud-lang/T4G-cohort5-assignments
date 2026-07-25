from bank_account import BankAccount 

class SavingsAccount(BankAccount):
    """Represents a savings account that earns interest."""

    def __init__(self, name, balance, interest_rate):
        """Initializes the savings account."""
        super().__init__(name, balance)
        self.interest_rate = interest_rate