class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Double underscore 'mangles' the name

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Invalid deposit amount!")

    @property
    def balance(self):
        """Getter for balance"""
        return self.__balance

# Usage
account = BankAccount(1000)
account.deposit(500)
# print(account.__balance)  # This would throw an AttributeError
print(account.balance)      # Correct way to access via the @property getter
