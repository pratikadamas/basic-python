

class Employee:
    # class attribute
    empcount = 0
    def __init__(self,name,salary):
        self.nam= name
        self.salary = salary
        # modify class attribute
        Employee.empcount +=1
    def display(self):
        print("Nme of the Employee is : ",self.nam," and salary is :",self.salary)
        # accessing class attribute
        print("Total employee is :",Employee.empcount)


emp1= Employee("Pratik Giri",25000)
emp1.display()
emp2 = Employee("Pritam mondal ",30000)
emp2.display()

print(emp2.empcount)