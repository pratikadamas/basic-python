a=10
b=a

print(id(a))
print(id(b))
b=12

print(id(b))
print(id(a))
print(a)
print(b)
