import itertools

def power_set(input_set):
    power_set = []
    x=0
    for i in range(len(input_set)+1):
        for subset in itertools.combinations(input_set, i):
            power_set.append(set(subset))
            x+=1
    print("Total number of all possible combination :",x)
    return power_set


my_set = {1,2,3,4,5,6}
result = power_set(my_set)
print(result)
# Expected output: [set(), {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}]