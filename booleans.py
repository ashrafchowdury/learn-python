print(5 > 2)

x = 500
y = 800

if x > y:
    print('x is GT then y')
else:
    print('x is not GT then y')

print(bool("Hello"))  # true
print(bool("")) # false
print(bool(15)) # true
print(bool(0)) # false
print(bool(['name', 'age', 'work'])) # true - Any list, tuple, set, and dictionary are True, except empty ones.
print(bool([])) # false

print('---------------')
# These values will be false
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))
print('---------------')

# PY has many built in function that returns bool values like: isinstance() which can be used to determine if an object is of a certain data type
test_instence=300
print(isinstance(x, int))