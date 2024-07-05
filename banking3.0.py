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
            self._transactions.append(["Deposit", f"${amount:,.2f}", f"${self._balance:,.2f}"])
            print(f"Deposit of ${amount:,.2f} made. New balance is ${self._balance:,.2f}")

    def withdraw(self, amount):
        if amount > 0 and self._balance >= amount:
            self._balance -= amount
            self._transactions.append(["Withdrawal", f"${amount:,.2f}", f"${self._balance:,.2f}"])
            print(f"Withdrawal of ${amount:,.2f} made. New balance is ${self._balance:,.2f}")
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
    secondAccount = BankAccount("12345", "Jane Doe", 50000)
    thirdAccount = BankAccount("67890", "John Smith", 20000)

    accounts = [myAccount, secondAccount, thirdAccount]

    for account in accounts:
        while True:
            action = input(f"Enter 'd' to deposit or 'w' to withdraw for account {account._accountNumber}: ")
            if action.lower() == 'd':
                amount = float(input("Enter deposit amount: "))
                account.deposit(amount)
            elif action.lower() == 'w':
                amount = float(input("Enter withdrawal amount: "))
                account.withdraw(amount)
            else:
                print("Invalid action. Please enter 'd' or 'w'.")

            continue_transaction = input("Enter 'y' to continue making transactions or 'n' to finish: ")
            if continue_transaction.lower() == 'n':
                break

        account.accountInfoDisplay()
        account.transactionHistory()