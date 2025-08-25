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
    
    @balance.setter
    def balance(self, value):
        # not sure if this is right but trying validation
        if value < 0:
            print("Warning: negative balance not allowed")
            return
        self._balance = value
    
    def __str__(self):
        return f"Account holder: {self.name}, Balance: ${self.balance}"
    
    def __repr__(self):
        # added this - think it should show more technical info
        return f"BankAccount(name='{self.name}', balance={self.balance})"
    
    def __eq__(self, other):
        # just compare balances for now
        return self.balance == other.balance
    
    def __add__(self, amount):
        # deposit money
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
    
    # context manager stuff - had to look this up
    def __enter__(self):
        print(f"Starting transaction session for {self.name}")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Transaction session ended for {self.name}")
        if self.transaction_log:
            print("Transactions:")
            for transaction in self.transaction_log:
                print(f"  {transaction}")
        # not sure what to return here
    
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
