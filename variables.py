# Python has no command for declaring a variable - A variable is created the moment you first assign a value to it.

x = "First"
y = "variable!"

print(x)
print(y)

# Py variable don't need to be an specific type it could chage it's type after declaring it

test_var_type = 5
test_var_type = "Changed the var type here!"

print(test_var_type)

# Type can be declared in a variable using 'casting'

test_var_type_with_casting = int(9)
# test_var_type_with_casting = str("Changed type here") - This will not throw error in this case

print(type(test_var_type_with_casting))

# Assign multiple variables in one line
# Note: Make sure the number of variables matches the number of values, or else you will get an error.
var_one, var_two, var_three = 'var one value', 'var two value', 'var three value'

print(var_one, var_two, var_three)

# Assign one value to multiple variables
var_one_value = var_two_value = var_three_value = "Multple value assignment"

print(var_one_value, var_two_value, var_three_value)


# Extract list values into variables - unpacking list values

list_val = ['value 1', 'value 2']

list_val_one, list_val_two = list_val

print(list_val_one, list_val_two)

# Global variables
# All of the above variables considered as global variables
global_var = "This is a global variable"

# Local vriables are declared under a function which can't be accesed outside of the function
def local_var_func():
    local_var = "this is a local variables"

local_var_func()
# print(local_var) - this will throw an error

# To make a local var to na global var use the keyword global with the variable name
def local_var_func_two():
    global local_var_two # the 'global' keyword here making this var global
    local_var_two = "this is a local variable but it will get global because it has the keyword global assigned to it"

local_var_func_two()
print(local_var_two)

# Also we can use the global keyword to change the global var inside a function
global_var_name = "ashraf"

def local_var_func_three():
    global global_var_name # the global var will ge changed because we are modifiyng it in the local enviroment using the global keyword
    global_var_name = "Bosedi"

local_var_func_three()
print(global_var_name)