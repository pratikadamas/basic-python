

# This is a global variable
global_variable = "I am a global variable"

def display_global():
    # Accessing the global variable inside this function
    print(global_variable)

def modify_global():
    global global_variable  # Declare that we're using the global variable
    global_variable = "I've been modified"
    print(global_variable)

display_global()
modify_global()
display_global()