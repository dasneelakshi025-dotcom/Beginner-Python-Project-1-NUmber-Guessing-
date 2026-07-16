import random

def number_guessing_game():
    print("🎮 Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100.")

    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("📉 Too Low! Try again.\n")

        elif guess > secret_number:
            print("📈 Too High! Try again.\n")

        else:
            print(f"\n🎉 Congratulations!")
            print(f"You guessed the correct number in {attempts} attempts.")
            break

number_guessing_game()