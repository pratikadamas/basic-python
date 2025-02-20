# Given frozenset containing string
import math

fs_string = frozenset({'1','2'})  # {'1'} is a string inside frozenset

# Convert string elements to integers
fs_int = frozenset({int(x) for x in fs_string})  # Now frozenset({1})

# Converting it to {frozenset({1, 2})}
result = {frozenset({1, 2})}  # Manually defining desired output

print("Converted:", fs_int)  # Output: {frozenset({1, 2})}
print(math.pow(2,9)*3)
