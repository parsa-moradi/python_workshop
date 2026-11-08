import random

MAX_ATTEMPTS = 5
LOW, HIGH = 1, 100
NEAR_LIMIT = 5      # difference up to 5: very close
MEDIUM_LIMIT = 15   # difference up to 15: medium

RANKS = {
    1: "Exemplary",
    2: "Excellent",
    3: "Good",
    4: "Acceptable",
    5: "You won by luck!",
}


def read_guess():
    """Return a valid integer between 1 and 100; invalid input costs no attempt."""
    while True:
        text = input(f"Enter your guess ({LOW} to {HIGH}): ").strip()
        try:
            value = int(text)
        except ValueError:
            print("Invalid input! Please enter a whole number.")
            continue
        if value < LOW or value > HIGH:
            print(f"The number must be between {LOW} and {HIGH}!")
            continue
        return value


def closeness_hint(diff):
    if diff <= NEAR_LIMIT:
        return "You're very close!"
    if diff <= MEDIUM_LIMIT:
        return "You're close, but still a bit far!"
    return "You're very far!"


def play_round():
    secret = random.randint(LOW, HIGH)
    attempt = 1

    while attempt <= MAX_ATTEMPTS:
        print(f"\nAttempt {attempt} of {MAX_ATTEMPTS}")
        print(f"Lives remaining: {MAX_ATTEMPTS - attempt + 1}")

        guess = read_guess()

        if guess == secret:
            print(f"\nWell done! You won! The secret number was {secret}.")
            print(f"Your rank: {RANKS[attempt]}")
            return

        direction = "Enter a larger number" if guess < secret else "Enter a smaller number"
        print(f"{direction} - {closeness_hint(abs(guess - secret))}")
        attempt += 1

    print("\nYou lost! You ran out of attempts.")
    print(f"The secret number was {secret}.")


def ask_play_again():
    while True:
        answer = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if answer in ("yes", "y"):
            return True
        if answer in ("no", "n"):
            return False
        print("Please enter only 'yes' or 'no'.")


def main():
    print("Welcome to the Number Guessing Game!")
    while True:
        play_round()
        if not ask_play_again():
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
