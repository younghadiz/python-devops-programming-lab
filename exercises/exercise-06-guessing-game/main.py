"""Exercise 6: Number guessing game."""

import random


def main() -> None:
    target_number = random.randint(1, 9)

    print("Guess the number between 1 and 9.")

    while True:
        user_input = input("Your guess: ").strip()

        try:
            guess = int(user_input)
        except ValueError:
            print("Invalid input. Enter a whole number from 1 to 9.")
            continue

        if not 1 <= guess <= 9:
            print("Your guess must be between 1 and 9.")
            continue

        if guess < target_number:
            print("Too low.")
        elif guess > target_number:
            print("Too high.")
        else:
            print("YOU WON!")
            break


if __name__ == "__main__":
    main()