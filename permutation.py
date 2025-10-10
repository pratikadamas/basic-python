from itertools import permutations

per = permutations([1,2,3,4],3)
# print((per))

li=list()
for i in per:
    li.append(i),
    print(i)


for i in range(len(li)):
    if (2,3,1)==li[i]:
        print ("Next permutation is ",li[i+1])
        break