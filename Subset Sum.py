from itertools import combinations, permutations
def CombinationSum(nums):
    if len(nums) == 0:
        return -1
    l=list()

    for i in range (len(nums)):
        l2=list(combinations(nums,i))
        for j in l2:
            l3=list(j)
         # print(l2)
            l.append(sum(l3))
    return l



ar=[1,2,3]
print (sum(ar))
print(CombinationSum(ar))