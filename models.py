class BankAccount:
    def __init__(self,holder_name,initial_balance):
        self.holder_name = holder_name
        self.__balance = initial_balance

    # Deposite Function in TK
    def deposite(self,amount):
        if amount > 0:
            self.__balance += amount
            print(f"Your deposite is succesfull : {amount}")
        else:
            print("Please...deposite your positive number")

    # Withdrawal Function 
    def Withdraw(self,amount):
        if 0 < amount < self.__balance:
            self.__balance -= amount
            print(f"Success {amount} has been withdrawn.")
        else:
            print(f"Sorry! Insufficient balance or incorrect amount.")

    # Balance viewing function (as the balance is private, it must be viewed using this method)
    def check_balance(self):
        print(f"{self.holder_name} is your current balance : {self.__balance}")

