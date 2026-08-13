class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Invalid amount")
        self.balance += amount


class SavingsAccount(BankAccount):
    def __init__(self, owner, rate=0.05):
        super().__init__(owner)
        self.rate = rate

    def add_interest(self):
        self.balance *= 1 + self.rate

    def __str__(self):
        return f"{self.owner}: ₦{self.balance:,.0f}"


if __name__ == "__main__":
    print(SavingsAccount("Kande"))
