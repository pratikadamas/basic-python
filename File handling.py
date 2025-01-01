# with open("test.txt","w+") as file:
file = open("test.txt","r")
# file.write("                                HAPPY NEW YEAR                                \n  \n")
# file.write('''      Wishing you a year filled with happiness, success, and unforgettable moments.
#            May 2024 bring you joy, good health, and endless opportunities.
#            Cheers to a fresh start and exciting new adventures ahead! ''')
content = file.read()

print(content)

