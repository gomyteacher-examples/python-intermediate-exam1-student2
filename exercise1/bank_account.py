class InsufficientFundsError(Exception):
    pass

class BankAccount:
    def __init__(self, name, initial_balance=0):
        self.name = name
        self._balance = initial_balance  # private balance
        self.transaction_log = []
    
    @property
    def balance(self):
        return self._balance
    
    def __str__(self):
        return f"Account holder: {self.name}, Balance: ${self.balance}"
    
    def __eq__(self, other):
        return self.balance == other.balance
    
    def __add__(self, amount):
        self._balance += amount
        self.transaction_log.append(f"Deposited ${amount}")
        return self
    
    def __sub__(self, amount):
        if self._balance < amount:
            print("Insufficient funds!")  # not sure how to do exceptions properly
            return self
        self._balance -= amount
        self.transaction_log.append(f"Withdrew ${amount}")
        return self
    
    def deposit(self, amount):
        self._balance += amount
    
    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
        else:
            print("Cannot withdraw - insufficient funds")

# test
if __name__ == "__main__":
    account = BankAccount("Alice", 1000)
    account += 500
    account -= 200
    print(account.balance)
    print(account)
