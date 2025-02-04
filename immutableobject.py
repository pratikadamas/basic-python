def testfunction(arg):
   print(var is arg)
   print ("ID inside the function:", id(arg))
   
   arg = arg + 1
   print ("new object after increment", arg, id(arg))

var=10
print ("ID before passing:", id(var))
testfunction(var)
print ("value after function call", var)
print ("ID outside the function:", id(var))