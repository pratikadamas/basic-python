def my_decorator(func):
    def wrapper():
        print("Before the function runs")
        func()
        print("After the function runs")
    return wrapper

def say_hello():
    print("Hello!")

say_hello = my_decorator(say_hello)
say_hello()