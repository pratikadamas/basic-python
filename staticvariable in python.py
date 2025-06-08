class MyClass:
    # This is a class variable (static variable)
    class_variable = "I am a class variable"

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

# Accessing the class variable
print(MyClass.class_variable)

# Creating instances
obj1 = MyClass("Instance 1 data")
obj2 = MyClass("Instance 2 data")

# Both instances share the same class variable
print(obj1.class_variable)
print(obj2.class_variable)

# Modifying the class variable through the class
MyClass.class_variable = "Class variable modified"

print(obj1.class_variable)
print(obj2.class_variable)

# If you try to modify it through an instance, it creates an instance variable with the same name,
# rather than modifying the class variable.
obj1.class_variable = "This is now an instance variable for obj1"
print(obj1.class_variable) # This prints the instance variable
print(MyClass.class_variable) # The class variable remains unchanged