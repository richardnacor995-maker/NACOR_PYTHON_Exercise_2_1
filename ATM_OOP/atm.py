# atm.py

class ATM:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def check_balance(self):
        print("\nCurrent Balance\t\t: ₱ {:,.2f}".format(self.balance))

    def deposit(self):
        while True:
            try:
                amount = float(input("\nEnter Deposit Amount\t: ₱ "))

                if amount <= 0:
                    print("Deposit amount must be greater than ₱ 0.00.")
                else:
                    self.balance += amount
                    print("Deposit Successfully!")
                    break

            except ValueError:
                print("Invalid input! Please enter a valid amount.")

    def withdraw(self):
        while True:
            try:
                amount = float(input("\nEnter Withdrawal Amount\t: ₱ "))

                if amount <= 0:
                    print("Withdrawal amount must be greater than ₱ 0.00.")

                elif amount > self.balance:
                    print("Insufficient balance!")

                else:
                    self.balance -= amount
                    print("Withdraw Successfully!")
                    break

            except ValueError:
                print("Invalid input! Please enter a valid amount.")

    def display_menu(self):

        while True:

            print("\n")
            print("      * * * A T M * * *")
            print("       Bank Operation:")
            print()
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")

            choice = input("\nChoose Operation: ")

            if choice == "1":
                self.check_balance()

            elif choice == "2":
                self.deposit()

            elif choice == "3":
                self.withdraw()

            elif choice == "4":
                print("\nThank you for choosing our bank!")
                print("Have a nice day!")
                break

            else:
                print("\nInvalid operation! Please choose between 1 and 4.")