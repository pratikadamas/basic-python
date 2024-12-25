

def outer_function(x):
    y = 10

    def inner_function(z):
        return x + y + z  # x and y are captured from the enclosing scope

    return inner_function

closure = outer_function(5)
result = closure(3)
print(result)