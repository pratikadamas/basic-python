
class Employee:
    # constructor
    def __init__(self,name,salary,project):
        # public
        self.neme=name
        # private
        self.__salary=salary
        # protected
        self._project=project
    def showdetails(self):
        print("Employee name :",self.neme,"\nSalary : ",self.__salary,"\nWork on :",self._project,"project")

    # deconsrtuctor
    def __del__(self):

        print("Object is destroyed")
        print("---Employee not present in our company---")

emp1 = Employee('Pratik Giri',30000,'DEEP Learning')
emp1.showdetails()

#  error we are try to access private data member
# print(emp1.__salary)

# --------access private data using name mangling--------
print("Employee salary : ",emp1._Employee__salary)

