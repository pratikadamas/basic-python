

try:
    1/0

except NameError as e:
    print("NameError")

except Exception as e:
    print(" Due to Exception class!!")
