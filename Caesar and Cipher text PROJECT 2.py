
# only for lowercase and Uppercase character and Digit
# Shift key can be positive or negative

alphabet=['','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','1','2','3','4','5','6','7','8','9','0']

def encryption(plaintext,shift):
    cipher_text=""
    for char in plaintext:
        position=alphabet.index(char)
        new_position=(position+shift)%62
        cipher_text=cipher_text+alphabet[new_position]
    print("After Encryption :-- ",end="")
    print(cipher_text)
def decryption(ciphertext,shift):
    original_text=""
    for char in ciphertext:
        position = alphabet.index(char)
        new_position = (position - shift)%62
        if(new_position<0):
            new_position+=62

        original_text+=alphabet[new_position]

    print(f"Your original text is:-- {original_text}")

What_to_do=input("For encryption type \"encrypt\" for Decryption type \"decrypt\"", )
text=input("Type your messageto encrypt: ",)
shift_key=int(input("Shift key : ", ))

if(What_to_do=="encrypt"):
    encryption(plaintext=text,shift=shift_key)  # function call by keyword

elif(What_to_do=="decrypt"):
    decryption(ciphertext=text,shift=shift_key)
else:
    print("-----------Wrong input---------")