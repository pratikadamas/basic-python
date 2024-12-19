a=10
def func():
    global x
    x=30
    #a+=10
    a=20
    print("Value inside the function:",a)
func()
print("Value Outside the function:",a)
x=89-a
print(x)