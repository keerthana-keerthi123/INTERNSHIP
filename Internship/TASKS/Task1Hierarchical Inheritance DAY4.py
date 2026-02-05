# Parent class
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.account_holder} deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{self.account_holder} withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient balance!")

    def display_balance(self):
        print(f"Account Holder: {self.account_holder}, Balance: {self.balance}")


# Child class: SavingsAccount
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=0, interest_rate=0.05):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest of {interest} added. New balance: {self.balance}")


# Child class: CurrentAccount
class CurrentAccount(BankAccount):
    def __init__(self, account_holder, balance=0, overdraft_limit=5000):
        super().__init__(account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw_with_overdraft(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"{self.account_holder} withdrew {amount} with overdraft. New balance: {self.balance}")
        else:
            print("Overdraft limit exceeded!")


# Testing
print("=== Savings Account Test ===")
savings = SavingsAccount("Keerthana", 1000, 0.10)
savings.deposit(500)
savings.add_interest()
savings.withdraw(300)
savings.display_balance()

print("\n=== Current Account Test ===")
current = CurrentAccount("Keerthana", 2000, 3000)
current.deposit(1000)
current.withdraw_with_overdraft(4500)
current.display_balance()
