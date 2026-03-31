
from itertools import permutations

def juspay(s, k):
    if(len(s)==1):
        return -1
    perms = [''.join(p) for p in permutations(s, k)]
    print(perms)
    perms.sort()
    print("All possible size k keys in sorted order ",perms)

    for p in perms:
        if p > s:
            return p
    return -1


def per(s):
    all_perms = []
    for p in range(1, len(s) + 1):
        for perm in permutations(sorted(s), p):  # sort input first
            all_perms.append(''.join(perm))

    for perm in sorted(all_perms):
        print(perm)


print(juspay("cba", 2))
print(per("cab"))
