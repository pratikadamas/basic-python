


#find() --->returnindex no. [first letter]  if string nit present it return (-1)

str="Adamas University"
print(str.find('a'))
print(str.find('kni'))
print(str.find("s",7))

#index()--->return index value when the first string encounter// if string not present it return error
print(str.find('v'))

#isalpha()---> if a string only contain srting it return true else false
print(" My roll no :" ,end="")
str2="UG/02/BTCSE/2023/126"
print("My roll no only contain srting: ",str2.isalpha())
print("My roll no only contain digit: ",str2.isdigit())
print("My roll no only contain alphanumeric : ",str2.isalnum())

print(" Enter a number ")
a=int(input())

print(chr(a))
print("a character")
a=input()
print(ord(a))

