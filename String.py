s="Adamas University"
print(s)

l=len(s)
print("length of the string :",l)

print("DISPLAY STRING USING FOR LOOP:")
for n in range(l):
    print(s[n],end=" ")

print(" \nAll character in lowercae:--",s.lower())
print("All character in uppercase:---",s.upper())
print("1st letter of the word is uppercase:--",s.capitalize())
