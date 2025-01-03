# When you use a with statement to open a file,
# the file is automatically closed at the end of the block,
# even if an error occurs within the block.

with open("test.txt","w+") as file:
    content = file.read()

print(content)

print("!!file closed!!!")
