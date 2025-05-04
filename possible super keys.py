from itertools import combinations

def power_set(input_set):

    length = len(input_set)+1
    power_set =set()
    x=0
    for i in range(1,length):
        for subset in combinations(input_set, i):
            power_set.add(frozenset(subset))
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



print("No of Candidate Key present in the Relation :")
candidate_key = int(input())
CK_set = set()
for i in range(candidate_key):
    element = set(input(f"Enter the candidate key value {i+1} :"))

    CK_set.add(frozenset(element))

print("DISPLAY ALL CANDIDATE KEYS :",CK_set)
print(type(CK_set))

# convet power set to a power list
power_set_list=list(pw)



# #prime attribute
# prime_attribute=list(CK_set)
# prime_attribute_set=set()
# no_of_prime_attribute=len(prime_attribute)
# for i in range(no_of_prime_attribute):
#     prime_attribute_set.add( set(prime_attribute[i]) )
#
#
# print("DISPLAY all prime attributes :",prime_attribute_set)


print("No of prime attributes present in the Relation :")
no_of_prime_attribute=int(input())
prime_attribute_set=set()
for i in range(no_of_prime_attribute):
    element = int(input(f"Enter the prime attribute {i+1} :"))
    prime_attribute_set.add(element)

print("DISPLAY ALL PRIME ATTRIBUTES",prime_attribute_set)


CK_set_list=list(CK_set)


print(" 1 st type ",type(CK_set_list[0]))

super_key=0


super_key_list=[]

for i in range(len(CK_set_list)):
    k = set(CK_set_list[i])
    print("combo of:",k)
    for j in range(len(power_set_list)):
        # k=set(CK_set_list[i])
        m = set(power_set_list[j])
        print(m)

        if k.issubset(m):
            super_key += 1
            super_key_list.append(m)



print("total super keys=", len(super_key_list))
print(type(super_key_list))
# merge_set =set.union(*super_key_list)
# print("total merge set=", len(merge_set))
unique_set ={frozenset(s) for s in super_key_list}
print(" DISPLAY ALL THE SUPER KEY",unique_set)
print("TOTAL NUMBER OF SUPERKEY",len(unique_set))

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