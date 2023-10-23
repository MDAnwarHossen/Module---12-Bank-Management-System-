from User import User
from Admin import Admin
from Bank import Bank

admin = Admin()
user1 = User("Anwar", "anwar@gmail.com", "Mirpur", "savings")
user2 = User("Habib", "habib@gmail.com", "Dhanmondi", "current")
user3 = User("Rohim", "rohim@gmail.com", "Dhanmondi", "current")
while True:
    print("\n Options : ")
    print(f"1 : Admin")
    print(f"2 : User")
    type = int(input("\nWho are you? "))
    if type == 1:
        while True:
            print("\n Options : ")
            print(f"1 : All User Accounts List")
            print(f"2 : Delete a user account")
            print(f"3 : Total Bank Balance")
            print(f"4 : Total Loan Amount")
            print(f"5 : ON Loan Feature")
            print(f"6 : OFF Loan Feature")
            print(f"7 : Go Back previous page")
            opt = int(input("\nSelect an option? "))
            if opt == 1:
                admin.all_accounts()
            elif opt == 2:
                print("\n Options : ")
                if len(Bank.users) > 1:
                    acc_num = int(
                        input(f"Account Number ex-{Bank.users[1].account_number}: "))
                else:
                    acc_num = int(
                        input(f"Account Number: "))
                admin.delete_account(acc_num)
            elif opt == 3:
                admin.total_balance()
            elif opt == 4:
                admin.total_loan_amount()
            elif opt == 5:
                admin.loan_feature("On")
            elif opt == 6:
                admin.loan_feature("Off")
            elif opt == 7:
                break

    elif type == 2:
        while True:
            print("\n Options : ")
            print(f"1 : Deposit")
            print(f"2 : Withdraw")
            print(f"3 : Current Balance")
            print(f"4 : Transaction History")
            print(f"5 : Take Loan")
            print(f"6 : Transfer Balance")
            print(f"7 : Go Back previous page")
            opt = int(input("\nSelect an option? "))
            if opt == 1:
                print("\n Options : ")
                amount = int(input("\nAmount : "))
                user1.deposit(amount)
            elif opt == 2:
                print("\n Options : ")
                amount = int(input("\nAmount : "))
                user1.withdraw(amount)
            elif opt == 3:
                user1.available_balance()
            elif opt == 4:
                user1.print_transaction_history()
            elif opt == 5:
                print("\n Options : ")
                amount = int(input("\nAmount : "))
                user1.take_loan(amount)
            elif opt == 6:
                print(f"\n Options : ")
                if len(Bank.users) > 1:
                    acc_num = int(
                        input(f"Account Number ex-{Bank.users[1].account_number}: "))
                else:
                    acc_num = int(
                        input(f"Account Number: "))
                amount = int(input("Amount : "))
                user1.transfer(acc_num, amount)
            elif opt == 7:
                break
