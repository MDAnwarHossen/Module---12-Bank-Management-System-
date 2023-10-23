from User import User
from Bank import Bank


class Admin:

    def create_account(self, name, email, address, account_type):
        user = User(name, email, address, account_type)
        Bank.users.append(user)

    def delete_account(self, account_number):
        for user in Bank.users:
            if user.account_number == account_number:
                Bank.users.remove(user)
                print(f"Account Number {user.account_number} has been deleted")
                break
            else:
                print("The account does not exist")

    def all_accounts(self):
        for user in Bank.users:
            print(f"Account Number: {user.account_number}, Name: {user.name}")

    def total_balance(self):
        print(f"Total Available Balance: {Bank.balance}")

    def total_loan_amount(self):
        print(f"Total Loan Amount: {Bank.loan_amount}")

    def loan_feature(self, state):
        if state == "On":
            Bank.loan_feature = True
            print("Loan feature has turned ON")
        elif state == "Off":
            Bank.loan_feature = False
            print("Loan feature has turned OFF")
