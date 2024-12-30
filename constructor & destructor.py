

class Employee:
    # constructor
    def __init__(self,name,salary,project):
        self.neme=name
        self.salary=salary
        self.project=project

    def showdetails(self):
        print("Employee name :",self.neme,"\nSalary : ",self.salary,"\nWork on :",self.project,"project")

    # deconsrtuctor

    def __del__(self):

        print("Object is destroyed")
        print("---Employee not present in our company---")



emp1 = Employee('Pratik Giri',30000,'DEEP Learning')
emp1.showdetails()