# for loop is used for iterating overa sequence like: tuple, list, dict, set, even string as well

# Looping through a list
listOfNames = ["Ashraf", "Chowdury", "Luffy", "Zoro", "Shanks", "Croco boy"]

for names in listOfNames:
    print(names)

# Looping through a string
name = "Ashraf"
for myName in name:
    print(myName)

# the break statement we can stop the loop before it has looped through all the items:
for names in listOfNames:
    if names == "Zoro":
        break
    print(names)

# the continue statement we can stop the current iteration of the loop, and continue with the next:
for names in listOfNames:
    if names == 'Zoro': # it will stop the iteration for the Zoro and then will continue for others
        continue
    print(names)

# range() function - To loop through a set of code a specified number of times, we can use the range() function
for num in range(5):
    print(num)
# The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6)
for num in range(2, 5):
    print(num)
# The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3)
# first pera is: starting index number, second is interator number, thrid is incement value by that number
# Default: first: is not added then in it take 0 index as strting num, second is: interator number which required to add, thrid is: if avoided then it will by default increment by 1
for num in range(4, 30, 3): 
    print(num)

# The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
for names in listOfNames:
    print(names)
else:
    print("Loop finished")
# Note: else block will NOT be executed if the loop is stopped by a break statement.

# pass Statement
for x in [0, 1, 2]:
  pass