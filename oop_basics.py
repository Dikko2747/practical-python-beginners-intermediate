class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Invalid amount")
        self.balance += amount


if __name__ == "__main__":
    acct = BankAccount("Zainab", 5000)
    acct.deposit(2500)
    print(acct.owner, acct.balance)
