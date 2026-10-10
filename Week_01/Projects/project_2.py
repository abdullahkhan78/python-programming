# Simple ATM Simulator

# Predefined credentials
username = "Abdullah"
pin = "3452"
balance = 5000000.0  # initial balance

# Login system
input_username = input("Enter username: ")
input_pin = input("Enter PIN: ")

if input_username == username:
    if input_pin == pin:
        print("Login successful!\n")

        # ATM operations
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Exit")

        choice = int(input("Choose an option (1-3): "))

        if choice == 1:
            print(f"Your current balance is Rs.{balance:.2f}")

        elif choice == 2:
            amount = float(input("Enter amount to withdraw: "))
            if amount <= balance and amount > 0:
                balance -= amount
                print(f"Withdrawal successful! Remaining balance: Rs.{balance:.2f}")
            else:
                print("Invalid amount or insufficient balance.")

        elif choice == 3:
            print("Thank you for using the ATM!")

        else:
            print("Invalid option selected.")

    else:
        print("Incorrect PIN!")
else:
    print("Invalid username!")
