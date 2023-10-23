from datetime import datetime
from Bank import Bank
import random


class User:
    def __init__(self, name, email, address, account_type) -> None:
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.account_number = random.randint(1000, 9999)
        self.balance = 0
        # self.loan_amount = 0
        self.loan_counter = 0
        self.transaction_history = []
        self.append_user()

    def append_user(self):
        Bank.users.append(self)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            Bank.balance += amount
            self.transaction_history.append(
                {"date": datetime.now().strftime("%d %b, %I:%M%p"), "description": "deposit", "balance": self.balance})
            print(f"Taka {amount} is deposited")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            Bank.balance -= amount
            self.transaction_history.append(
                {"date": datetime.now().strftime("%d %b, %I:%M%p"), "description": "withdrow", "balance": self.balance})
            print(f"Sucess. Your current balance is {self.balance}")
        else:
            print("Withdrawal amount exceeded")

    def available_balance(self):
        print(f"Your current balance is {self.balance}")

    def print_transaction_history(self):
        print("Date -----------> Description -----------> Balance")
        print("-------------------------------------------------")
        for transaction in self.transaction_history:
            print(
                f'{transaction["date"]}-> {transaction["description"]}----------------> {transaction["balance"]}')

    def take_loan(self, amount):
        if self.loan_counter < 2:
            if Bank.loan_feature:
                if Bank.balance >= amount:
                    Bank.loan_amount += amount
                    self.balance += amount
                    Bank.balance -= amount
                    self.loan_counter += 1
                    self.transaction_history.append(
                        {"date": datetime.now().strftime("%d %b, %I:%M%p"), "description": "Loan received", "balance": self.balance})
                    print(
                        f"Success. You can take loan {2-self.loan_counter} more times")
                else:
                    print("The bank does not have a sufficient balance right now.")
            else:
                print("The Bank is not providing any loan")
        else:
            print("You can't take loan more that 2 times")

    def transfer(self, account_number, amount):
        if self.balance >= amount:
            exists = True
            for user in Bank.users:
                if user.account_number == account_number:
                    exists = False
                    self.balance -= amount
                    user.balance += amount
                    self.transaction_history.append(
                        {"date": datetime.now().strftime("%d %b, %I:%M%p"), "description": "transfer", "balance": self.balance})
                    user.transaction_history.append(
                        {"date": datetime.now().strftime("%d %b, %I:%M%p"), "description": "transfer", "balance": user.balance})
                    print("Balance transfer successful")
                    break
            if exists:
                print("Account does not exist.")
        else:
            print("The bank is bankrupt!")


# user1 = User("Anwar", "anwar@gmail.com", "Habi jabi", "savings")
# user1.deposit(200)
# user1.deposit(200)
# user1.withdraw(100)
# user1.available_balance()
# user1.print_transaction_history()
# print(len(Bank.users))
# print(user1.account_number)
