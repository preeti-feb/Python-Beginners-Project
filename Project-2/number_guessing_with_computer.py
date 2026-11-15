print("`"* 40)
print("Number Guessing Game with Computer")
print("`"* 40)

print("\nWelcome to Numeber Guessing Game")
print("You have only seven chances to win this game.")

import random
computer_guess = random.randint(1, 100)

tries = 0
total_chance = 7

while tries < total_chance:

    try:
        user_guess = int(input("\nGuess a number between 1 to 100: "))

    except ValueError:
        print("Invalid Input, Please enter a number.")
        continue

    if user_guess < 0 or user_guess > 100:
        print("Please enter a number between range(1-50).")
        continue


    tries += 1

    if user_guess > computer_guess:
        print(f"You guessed too high. Try lower one.")

    elif user_guess < computer_guess:
        print(f"You guessed too low. Try higher one.")


    else:
        print(f"\nThe computer guess {computer_guess} number.")
        print(f"🎉 Congratulations! You won this game in just {tries} attempts!")
        break


else:
    print(f"\nThe Game is Over. You used all your {tries} attempts. You lose this game.")
    print(f"The computer guess {computer_guess} number and win this game.")
