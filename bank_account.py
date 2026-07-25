class BankAccount:
    """Represents a customer's bank account."""

    def __init__(self, name, balance):
        """Initializes the account holder's name and starting balance."""
        self.name = name
        self.balance = balance


    def deposit(self, amount):
        """Adds money to the account balance."""

        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")

        self.balance += amount
        print(f"GHS {amount:.2f} deposited successfully.")



    def withdraw(self, amount):
        """Removes money from the account balance."""

        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")

        if amount > self.balance:
            raise ValueError("Insufficient balance.")

        self.balance -= amount
        print(f"GHS {amount:.2f} withdrawn successfully.")

    def get_balance(self):
        """Returns the current account balance."""
        return self.balance

    def __str__(self):
        """Returns a readable description of the account."""
        return f"Account[{self.name}] | Balance: GHS {self.balance:.2f}"