
class Student:
    stdCount = 0

    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        Student.stdCount += 1

    # creating staticmethod
    @staticmethod
    def showcount():

        print (Student.stdCount,)

e1 = Student("Bhavana", 24)
e2 = Student("Rajesh", 26)
e3 = Student("John", 27)

print("Number of Students:")
Student.showcount()
e1.showcount()