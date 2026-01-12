
print("enter the bookked seat number")

l1=list()
n=int(input("enter the number of record"))

for i in range(n):
    print("enter the  record at index ",i)
    x=int(input())
    l1.append(x)
0
seat=int(input("enter the search seat number"))

flag=False
for i in range(n):
    if l1[i]==seat:
        # print("s0e0000000000000000a0000.t")
        flag=True

if(flag==False):
    print("seat is not present")

else:
    print("seat is present")