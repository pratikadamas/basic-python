print("Enter the array Size")

n=int(input())

l1=list()
l2=list()
print("Enter the array elements")
for i in range(n):
    0
    print(" element at index ",i)
    l1.append(int(input()))


val=int(input("Enter the val"))

for i in range(n):
    if(l1[i]!=val):
        l2.append(l1[i])

print("size",len(l2))
print(l2)
