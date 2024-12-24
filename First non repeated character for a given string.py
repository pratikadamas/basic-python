
str = input(" Enter a string : " )

for char in str:
    if str.count(char) == 1:
        print(" The character is :" ,char)
        break