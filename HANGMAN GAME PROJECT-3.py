import random

words = ("apple","banana","cherry","jackfruit","rose","lion","tiger")


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



def display_hangman(wrong_guesses):
    print("************")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("**********")

def display_hint(hint):
    print(" ".join(hint))
def display_answer(answer):
    print(" ".join(answer))
def main():
    answer = random.choice(words)   # Select a random word
    hint=["_"]*len(answer)
    print(hint)
    wrong_guesses=0
    guessed_letters=set()
    is_running =True

    while(is_running):
        display_hangman(wrong_guesses)
        display_hint(hint)
        #display_answer(answer)
        guess=input("Enter a letter: ").lower()
        if len(guess) !=1 or not guess.isalpha():
            print("INVALID INPUT")
            continue

        if guess is guessed_letters:
            print(f"{guess} is already guessed")
            continue

        guessed_letters.add(guess)


        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess

        else:
            wrong_guesses += 1
            #check for win
        if "_" not in hint:
            display_hangman(wrong_guesses)
            display_answer(answer)
            print(" YOU ARE WIN!!!")
            is_running=False
             #check for loss
        elif wrong_guesses<=len(hangman_art)-1:
            display_hangman(wrong_guesses)
            display_answer(answer)
            print(" YOU LOSS!!")
            is_running = False

if __name__ == "__main__":
    main()

