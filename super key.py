from itertools import combinations

def power_set(input_set):

    length = len(input_set)+1
    power_set =set()
    x=0
    for i in range(1,length):
        for subset in combinations(input_set, i):
            power_set.add(frozenset( subset))
            x+=1
    print("Total number of all possible combination :",x)

    return power_set



print("POSSIBLE SUPER KEYS :")
print(" No of attribute present in the Relation :")
attribute = int(input())
MY_SET=set()
print(type(MY_SET))
for i in range(attribute):
    element = (input("Enter the attribute value: "))
    MY_SET.add(element)

print("DISPLAY ALL  ATTRIBUTE :",MY_SET)
pw=power_set(MY_SET)
print("DISPLAY ALL POSSIBLE POWER SET OF ATTRIBUTE :",pw)
print(type(pw))


print("No of Candidate Keys present in the Relation:")
candidate_key = int(input())

CK_set = set()
for i in range(candidate_key):
    input_data = input(f"Enter the candidate key value {i+1} (comma-separated integers): ")
    element = tuple(map(int, input_data.split(',')))
    CK_set.add(frozenset(element))

print("DISPLAY ALL CANDIDATE KEYS:", CK_set)
print(type(CK_set))

power_set_list=list(pw)


CK_set_list=list(CK_set)


print(" 1 st type ",type(CK_set_list[0]))

super_key=0

super_key_list=[]

for i in range(len(CK_set_list)):

    k = set(CK_set_list[i])
    print("----------------------------------------\ncombination of :",k)
    for j in range(len(power_set_list)):
        fs_string = power_set_list[j]
        fs_int = frozenset({int(x) for x in fs_string})

        m = set(fs_int)
        print(m)

        if k.issubset(m):
            super_key += 1
            super_key_list.append(m)



print("total super keys=", len(super_key_list))
print(type(super_key_list))

unique_set ={frozenset(s) for s in super_key_list}
print(" DISPLAY ALL THE SUPER KEY",unique_set)
print("----------------------------------------------------------------------------\nTOTAL NUMBER OF SUPERKEY",len(unique_set))

data=unique_set

print(data)


print(len(data))

final_data=list()

for i in data:
   temp=list(i)
   temp.sort()
   final_data.append(temp)

final_data.sort()

print(final_data)