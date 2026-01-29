
from itertools import permutations

def juspay(s, k):
    if(len(s)==1):
        return -1
    perms = [''.join(p) for p in permutations(s, k)]
    perms.sort()
    print("All possible size k keys in sorted order ",perms)

    for p in perms:
        if p > s:
            return p
    return -1


print(juspay("abc", 2))
