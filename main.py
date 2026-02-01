l=(1,2,3)
print(list(l))
a = [1, 2, 3,3,0,-5,1]
b = a.copy()
print(a+b) # concatinate two list

b.append(4)
# a.clear()

print(a)  # [1, 2, 3]
print(b)  # [1, 2, 3, 4]
print(a.pop(2))
l2=['a','s','d','f']
print("".join(l2))

# last index
print(b.index(1))

# b.remove(100)

# How can you remove all occurrences of a specific element from a list?
newlist =[ x for x in b if x!=1]
print(newlist)
print()

