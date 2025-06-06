



with open("demotxt.txt", "w") as file:
    file.write("Hello .I am pratik giri student of adamas university cse depertment")

with open("demotxt.txt", "r") as file:
    # for line in file:
    #     print(line)

    print(file.read())
with open("demotxt.txt","a") as file:
    file.write(" My dream is ai-ml engineer")
