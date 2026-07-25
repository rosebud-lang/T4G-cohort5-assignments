from bank_account import BankAccount 

class SavingsAccount(BankAccount):
    """Represents a savings account that earns interest."""

    def __init__(self, name, balance, interest_rate):
        """Initializes the savings account."""
        super().__init__(name, balance)
        self.interest_rate = interest_rate


    def apply_interest(self):
        """Calculates interest and deposits it into the account."""

        interest = self.balance * (self.interest_rate / 100)
        self.deposit(interest)

        print(f"Interest of GHS {interest:.2f} applied.")