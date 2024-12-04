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