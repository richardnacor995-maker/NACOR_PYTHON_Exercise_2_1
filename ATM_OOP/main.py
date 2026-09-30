# main.py

from atm import ATM


print("================================")
print("          ATM MACHINE")
print("================================")

# Get user information
name = input("Enter Name\t: ")

while True:
    try:
        balance = float(input("Enter Balance\t: ₱ "))

        if balance < 0:
            print("Balance cannot be negative.")
        else:
            break

    except ValueError:
        print("Invalid input! Please enter a valid amount.")


# Create ATM object
my_atm = ATM(name, balance)

print("\nWelcome, {}!".format(my_atm.name))

# Run ATM
my_atm.display_menu()