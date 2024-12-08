name="Ashraf"
num1=5
num2=3

if name:
    print(name)

if num1 > num2:
    print(num1)

if num1 == num2:
    print(num1)
else:
    print("num 1 doesn't == num2")

# if condition 'else if' conditon and else return
if num1 < num2:
    print('if condition passed')
elif num1 > num2:
    print('else if condition passed')
else:
    print('else condition passed')

# Short hand version of the if conditon
if num1 > num2: print('Short hand version of the if condition')

# Short hand version of the if else conditon
print('Short hand version of the if else condition') if num1 == num2 else print('Short hand version of the if else condition')

# And js(&&) oprator
if num1 and num2: print('and oprator')

# OR js(||) operetor
if num1 == num2 or name:
    print("Or operetor")

# Not js(!) operetor
if not num2 > num1: print("not operetor")

# pass - if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
if num1 > num2:
    pass

