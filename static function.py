class MyClass:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def static_method_example(param1, param2):
        """
        This is a static method.
        It does not receive 'self' or 'cls' as its first argument.
        """
        return f"Static method called with: {param1} and {param2}"

    def instance_method_example(self):
        """
        This is an instance method.
        It receives 'self' as its first argument.
        """
        return f"Instance method called by {self.name}"

# Accessing a static method
print(MyClass.static_method_example("hello", 123))

# You can also call it via an instance, but it's less common
obj = MyClass("Alice")
print(obj.static_method_example("world", 456))

# Calling an instance method requires an instance
print(obj.instance_method_example())
# MyClass.instance_method_example() # This would raise a TypeError because it needs an instance