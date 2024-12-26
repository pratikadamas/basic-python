
print("         EMAIL VERIFICATION          ")
email_id = input("Enter your Mail-id : ",)

mail=False

while  not mail :

    if('@'in email_id and '.' in email_id) :
        mail=True
        print("Your Mail-id is valid:")

    else:
        print("Your mail is not valid ,Try again!!")
        email_id = input("Enter your Mail-id : ", )
