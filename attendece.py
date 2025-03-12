
student_roll = set()
present_stu_roll=set()

previous_input = None
for i in range(123,196,1):
    student_roll.add(str(i))


print(student_roll)
print("Enter present student roll")
for i in range(123,196,1):
    x = input()
    if(x=='0'):
        break
    present_stu_roll.add(x)

print(present_stu_roll)


absent_stu_roll = student_roll.difference(present_stu_roll)
print("----------------------absent student roll--------------------------")
print(absent_stu_roll)

