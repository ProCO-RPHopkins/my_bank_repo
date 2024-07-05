class BankAccount:
    def __init__(self, accountNumber, accountHolder, initialBalance):
        # instance variables
        # single underscores are used to indicate protected variables
        self._accountNumber = accountNumber
        self._accountHolder = accountHolder
        self._balance = initialBalance
    
    # Deposit method within the BankAccount class
    # If the amount is greater than 0, the amount is added to the current balance
    def deposit(self, amount):
        if amount > 0:
            # Encapsulation - modifies instance variable _balance within BankAccount class
            # Maintain data integrity - prevents unauthorized changes to balance
            self._balance += amount
            # Formatting displays deposit amount & new balance w/ thousands separators
            print(f"Deposit of ${amount:,} made. New balance is ${self._balance:,}")

    def withdraw(self, amount):
        if amount > 0 and self._balance >= amount:
            # Encapsulation - modifies instance variable _balance within BankAccount class
            # Maintain data integrity - prevents unauthorized changes to balance
            self._balance -= amount
            print(f"Withdrawal of ${amount:,} made. New balance is ${self._balance:,}")
        else:
            print("Insufficient funds")
    
    def getBalance(self):
        # Encapsulates instance variable _balance within BankAccount class
        # Provides secure method to retrieve balance within BankAccount class
        return self._balance
    
    def accountInfoDisplay(self):
        '''Encapsulates instances of _accountNumber, _accountHolder, 
        & _balance within BankAccount class ''' 
        print(f"Account: {self._accountNumber} ({self._accountHolder})")
        print(f"Current Balance: ${self._balance:,.2f}")

if __name__ == "__main__":
    # Instances of the BankAccount class
    myAccount = BankAccount("47483", "Ryan Hopkins", 40000)
    myAccount.deposit(100)
    myAccount.withdraw(500)
    myAccount.withdraw(1000)
    myAccount.accountInfoDisplay()


    
    