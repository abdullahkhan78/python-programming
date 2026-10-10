import random

print("#================ ** Welcome to Rock-Paper-Scissors 🎮 ** ================#")
print("Enter 0 for Rock, 1 for Paper, 2 for Scissors")

user_choice = int(input("Enter your choice: "))

# Check for valid input first
if user_choice < 0 or user_choice > 2:
    print("Invalid choice! Please enter 0, 1, or 2.")
else:
    computer_choice = random.randint(0, 2)
    print("Computer chose:", computer_choice)

    if computer_choice == user_choice:
        print("Game draw! 😎")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose 😢")
    elif user_choice == 0 and computer_choice == 2:
        print("You win 🎉")
    elif computer_choice > user_choice:
        print("You lose 😢")
    elif computer_choice < user_choice:
        print("You win 🎉")
