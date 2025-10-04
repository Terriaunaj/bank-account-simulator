import random

class BankAccount:

    def __init__(self, account_number, owner_name, balance = 0.0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Deposit amount amount must be positive.")
    
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficent Funds")

    def get_balance(self):
        return self.balance
    
class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, owner_name):
        accNum = str(random.randint(1000, 9999))

        # To ensure every account number is unique
        while accNum in self.accounts:
            accNum = str(random.randint(1000, 9999))
        self.accounts[accNum] = BankAccount(accNum, owner_name, 0.0)
        return accNum
    # Uses get to get the key for accounts dictionary
    def get_account(self, accNum):
        return self.accounts.get(accNum)
    
def safeNum(option):
    while True:
        try:
            return float(input(option))
        except ValueError:
            print("Invalid number, please try again.")
    
def main():
    bank = Bank()

    print("Welcome to the Bank Simulator!")

    while True:
        optionNum = input("\nChoose an option:\n"
                            "1. Create Account\n"
                            "2. Deposit\n"
                            "3. Withdraw\n"
                            "4. Check Balance\n"
                            "5. Exit\n"
                            "Enter choice: ")

        if optionNum == "1":
            name = input("Input your name: ")
            accNum = bank.create_account(name)
            print(f"Your account was created! Your account number is {accNum}")
        
        elif optionNum == "2":
            accNum = input("Input account number: ")
            account = bank.get_account(accNum)
            if account is not None:
                depositAmount = safeNum("How much would you like to deposit? ")
                account.deposit(depositAmount)
                print("Deposit Sucessful!")
            else:
                print("Account not found.")
            
        elif optionNum == "3":
            accNum = input("Input account number: ")
            account = bank.get_account(accNum)
            if account is not None:
                withdrawAmount = safeNum("How much would you like to withdraw? ")
                account.withdraw(withdrawAmount)
                print(f"You withdraw {withdrawAmount}!")
            else:
                print("Account not found.")

        elif optionNum == "4":
            accNum = input("Input account number: ")
            account = bank.get_account(accNum)
            if account is not None:
                print(f"Balance: ${account.get_balance():.2f}")
            else:
                print("Account not found.")

        elif optionNum == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")
    

if __name__ == "__main__":
    main()