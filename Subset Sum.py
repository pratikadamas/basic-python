from itertools import combinations,permutations
def CombinationSum(nums):
    if len(nums) == 0:
        print("array length is zero so return ")
        return -1
    l=list()

    for i in range (0,len(nums)+1):
        l2=list(combinations(nums,i))
        # print(l2)
        for j in l2:
            l3=list(j)
         # print(l2)
            l.append(sum(l3))
    return l


def SupersetWithoutDuplicate(nums):
    if len(nums) == 0:
        print("array length is zero so return ")
        return -1
    l=list()

    for i in range (0,len(nums)+1):
        l2=list(combinations(nums,i))
        # print(l2)
        for j in l2:
            l3=list(j)
            if l3 not in l:
                l.append(l3)

    return l


ar=[1,2,3 ]
a2=[]
print (sum(ar))
print(CombinationSum(ar))
# print(CombinationSum(a2))
print(SupersetWithoutDuplicate(ar))