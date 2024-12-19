import random

words = ("aardvark", "alligator", "alpaca", "ant", "anteater", "antelope", "ape", "armadillo",
         "baboon", "badger", "bat", "bear", "beaver", "bee", "bison", "boar", "buffalo", "butterfly",
         "camel", "capybara", "caribou", "cat", "caterpillar", "cattle", "chamois", "cheetah",
         "chicken", "chimpanzee", "chinchilla", "chough", "clam", "cobra", "cockroach", "cod",
         "coyote", "crab", "crane", "crocodile", "crow", "curlew", "deer", "dinosaur", "dog",
         "dogfish", "dolphin", "donkey", "dormouse", "dotterel", "dove", "dragonfly", "duck",
         "dugong", "dunlin", "eagle", "echidna", "eel", "eland", "elephant",  "elk", "emu",
         "falcon", "ferret", "finch", "fish", "flamingo", "fly", "fox", "frog", "gaur",
         "gazelle", "gerbil", "giraffe", "gnat", "gnu", "goat", "goldfinch", "goldfish",
         "goose", "gorilla", "goshawk", "grasshopper", "grouse", "guanaco", "gull", "hamster",
         "hare", "hawk", "hedgehog", "heron", "herring", "hippopotamus", "hornet", "horse",
         "human", "hummingbird", "hyena", "ibex", "ibis", "jackal", "jaguar", "jay", "jellyfish",
         "kangaroo", "kingfisher", "koala", "kookabura", "kouprey", "kudu", "lapwing", "lark",
         "lemur", "leopard", "lion", "llama", "lobster", "locust", "loris", "louse", "lyrebird",
         "magpie", "mallard", "manatee", "mandrill", "mantis", "marten", "meerkat", "mink",
         "mole", "mongoose", "monkey", "moose", "mosquito", "mouse", "mule", "narwhal", "newt")


hangman_art = {     0: ("   ",
                                   "   ",
                                   "   "),
                             1: (" o ",
                                   "   ",
                                   "   "),
                             2: (" o ",
                                   " | ",
                                   "   "),
                             3: (" o ",
                                   "/| ",
                                   "   "),
                             4: (" o ",
                                  "/|\\",
                                   "   "),
                              5: (" o ",
                                   "/|\\",
                                   "/  "),
                              6: (" o ",
                                   "/|\\",
                                   "/ \\")}


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
    answer=random.choice(words)
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
        if len(guess)!=1 or not guess.isalpha():
            print("INVALID INPUT")
            continue

        if guess is guessed_letters:
            print(f"{guess} is already guessed")
            continue

        guessed_letters.add(guess)


        if guess in answer:
            for i in range(len(answer)):
                if answer[i]==guess:
                    hint[i]=guess

        else:
            wrong_guesses=+1

        if "_" not in hint:
            display_hangman(wrong_guesses)
            display_answer(answer)
            print(" YOU ARE WIN!!!")
            is_running=False

        elif wrong_guesses<=len(hangman_art)-1:
            display_hangman(wrong_guesses)
            display_answer(answer)
            print(" YOU LOSS!!")
            is_running=False

if __name__ == "__main__":
    main()

