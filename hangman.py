import random

# Word list
words = ("apple", "banana", "cherry", "jackfruit", "rose", "lion", "tiger")

# Hangman art
hangman_art = {
    0: ("   ",
        "   ",
        "   "),
    1: ("  o ",
        "   ",
        "   "),
    2: ("  o ",
        " | ",
        "   "),
    3: ("  o ",
        "/| ",
        "   "),
    4: ("  o ",
        "/|\\",
        "   "),
    5: ("  o ",
        "/|\\",
        "/  "),
    6: ("  o ",
        "/|\\",
        "/ \\")
}


# Function to display hangman
def display_hangman(wrong_guesses):
    print("************")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("************")


# Function to display the hint
def display_hint(hint):
    print(" ".join(hint))


# Main function
def main():
    answer = random.choice(words)  # Select a random word
    hint = ["_"] * len(answer)  # Create a hint with underscores
    wrong_guesses = 0
    guessed_letters = set()  # Keep track of guessed letters
    max_wrong_guesses = len(hangman_art) - 1
    is_running = True

    print("Welcome to Hangman!")

    while is_running:
        display_hangman(wrong_guesses)
        display_hint(hint)

        # Input a guess
        guess = input("Enter a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("INVALID INPUT. Please enter a single alphabet.")
            continue

        if guess in guessed_letters:
            print(f"'{guess}' is already guessed. Try a different letter.")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            # Update the hint for correct guesses
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1

        # Check for win
        if "_" not in hint:
            display_hangman(wrong_guesses)
            display_hint(hint)
            print("YOU WIN!!!")
            is_running = False

        # Check for loss
        elif wrong_guesses > max_wrong_guesses:
            display_hangman(wrong_guesses)
            print(f"YOU LOSE! The correct word was '{answer}'.")
            is_running = False


if __name__ == "__main__":
    main()
