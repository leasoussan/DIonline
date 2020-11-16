
# Create a BankAccount class that contains the following attributes and methods:
# Owner
# Balance
# __init__ : initialize the two attributes
# deposit : accept the deposit only if it is positive
# withdraw : accept the withdraws if they don’t exceed the available balance (ie. the attribute)
class BankAccount():
    
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
         

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount should be positif ")
        self.balance += amount
        print(f"you account got debited {amount}")
        print(f"your balance is{self.balance}")
        
    
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError(f"Your balance is {self.balance} ")
        self.balance -= amount
        print(f"Your just withdrawn {amount}")


acct1 = BankAccount("loulou", 1000)



# EX missing parts to be bale to work 


# Create a class Owner.
# Each owner has a credit card number and a password. (ie. the attributes)
# Create a method check_owner_info that checks the credit card number and the password.
# The owner has 2 chances to get the right password.
# If he didn’t get it, inform him that the card has been eaten by the machine, and delete the credit card number
# Only if he gets the right credit card number and the right password, you can ask him if he wants to “deposit” or to “withdraw”.
# The deposit method only accept bills of $20, $50, $100$.
# Ask the user how many of each bill he wants to deposit. If it answers all the requirements, inform him of the sum he deposited.
# Continue asking him if he want to deposit more bills until he refuses.
# The withdraw method only give back bills from $20 to $50.
# Bonus:

# Create a class called Bank.
# The Bank class can have maximum 10 clients (so 10 bank accounts ie objects of the BankAccount class)
# Create a method to check how much money the bank has depending on the actions of its clients.
# Inform the Bank Manager of the amount, the number of bills and their values
