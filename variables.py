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