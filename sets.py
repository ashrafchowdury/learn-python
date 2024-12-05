# Set are used to store multiple items in a single variable
# A set is a collection which is unordered, unchangeable, and unindexed

# Note: Set items are unchageable but wee can remove and then add new items

thisisset={"this", 'is', 'a', 'set'}
print(thisisset)
print(type(thisisset))
# Very important: Sets are unordered, so you cannot be sure in which order the items will appear.

# Duplicates Not Allowed
testDuplicateSet={"Ashraf", "chowdury", 'Ashraf'}
print(testDuplicateSet) # it will auto remove the duplicate item

# Note 😑: The values True and 1 are considered the same value in sets, and are treated as duplicates
# Samw way: The values False and 0 are considered the same value in sets, and are treated as duplicates
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset) # it will remove either True or 1

# The set() Constructor
constructorSet = set(("apple", "banana", "cherry"))
print(constructorSet)

# Access Set Items
for x in constructorSet:
  print(x)
print("banana" in constructorSet)
print("apple" not in thisset)

# Add set items
listOfNumbers={1, 2, 3, 4, 5}
print(listOfNumbers)
listOfNumbers.add(6) # Add new items
print(listOfNumbers)
anotherListOfSet={9, 10}
print(anotherListOfSet)
listOfNumbers.update(anotherListOfSet) # update with another rset -he object in the update() method does not have to be a set, it can be any iterable object tuple list set dic
print(listOfNumbers)

# Remove set items
listOfNames={"Ashraf", "Suraf", "Jhon", "Tom", "Thomas", "Tony", "Chopper", "Zoro"}
print(listOfNames)
listOfNames.remove("Jhon")
print(listOfNames)
#listOfNames.remove("Chowdury") - This name is not present in the set - this will raise an error
listOfNames.discard("Suraf")
print(listOfNames)
listOfNames.discard("Chowdury") # This name is not present in the set - this will not raise an error
print(listOfNames)
# We can also use pop() - but the problem with pop is it will remove a random item from the set we will not know which one - reason because set is unorderd
listOfNames.pop()
print(listOfNames)
# clear will remove all the items from set but ot the entire set
listOfNames.clear()
print(listOfNames)
# del keyword will delte the set ccompletely
del listOfNames
# print(listOfNames) - this will raise an error because the set doesn't existt anymore



