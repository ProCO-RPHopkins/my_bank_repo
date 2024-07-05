from tabulate import tabulate

class BankAccount:
    def __init__(self, accountNumber, accountHolder, initialBalance):
        self._accountNumber = accountNumber
        self._accountHolder = accountHolder
        self._balance = initialBalance
        self._transactions = [
            ["Initial Balance", "", f"${self._balance:,.2f}"]
        ]
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self._transactions.append(["Deposit", f"${amount:,}", f"${self._balance:,.2f}"])
            print(f"Deposit of ${amount:,} made. New balance is ${self._balance:,}")

    def withdraw(self, amount):
        if amount > 0 and self._balance >= amount:
            self._balance -= amount
            self._transactions.append(["Withdrawal", f"${amount:,}", f"${self._balance:,.2f}"])
            print(f"Withdrawal of ${amount:,} made. New balance is ${self._balance:,}")
        else:
            print("Insufficient funds")
    
    def getBalance(self):
        return self._balance
    
    def accountInfoDisplay(self):
        print(f"Account: {self._accountNumber} ({self._accountHolder})")
        print(f"Initial Balance: ${self._balance:,.2f}")

    def transactionHistory(self):
        transactions = [
            ["Account Holder", self._accountHolder, ""],
            ["Account Number", self._accountNumber, ""],
            ["Action", "Amount", "Balance"]
        ] + self._transactions

        print(tabulate(transactions, tablefmt="grid"))

if __name__ == "__main__":
    myAccount = BankAccount("47483", "Ryan Hopkins", 40000)
    myAccount.deposit(100)
    myAccount.withdraw(500)
    myAccount.withdraw(1000)
    myAccount.accountInfoDisplay()
    myAccount.transactionHistory()
    print()
    
    secondAccount = BankAccount("12345", "Jane Doe", 50000)
    secondAccount.deposit(2000)
    secondAccount.withdraw(1000)
    secondAccount.accountInfoDisplay()
    secondAccount.transactionHistory()