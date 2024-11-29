# List are used to store multiple items in a variable. Just like Array in javascript

detailesList = ['name', 'age', 'work', 'platform']

print(detailesList)
print(len(detailesList))
print(type(detailesList))

# list constructor
constructorList = list(("name", 'age', 'email')) # list(()) is a constructor which we can use to create list
print(constructorList)


# There are four colletion data types in PY: 
# List - is a collection which is ordered and changeable. Allows duplicate members.
# Tuple - is a collection which is ordered and unchangeable. Allows duplicate members.
# Set - is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary -  is a collection which is ordered** and changeable. No duplicate members.

# Range of index - access list by defining range
# Note: The search will start at index 1 (included) and end at index 3 (not included).
print(detailesList[1:3])

# By leaving out the start value, the range will start at the first item
print(detailesList[:3])
print(detailesList[1:])

# Check if item exist
if 'age' in detailesList:
    print("Yes age does exist on the list")

# Change list item
detailesList[2] = 'email'
print(detailesList)

# Change a Range of Item Values
rangeList=['c', 'c++', 'c#', 'javascript', 'typescript']
rangeList[0:3] = ['rust', 'python']

print(rangeList)

# Inset Items - To insert a new list item, without replacing any of the existing values, we can use the insert() method.
rangeList.insert(0, 'fundamentals')

print(rangeList)

# Append items - To add an item to the end of the list, use the append() method:
rangeList.append("framworks")
print(rangeList)

# Extend list - To append elements from another list to the current list, use the extend() method.
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# Remove items
langList=['c', 'c++', 'c#', 'javascript', 'typescript']
langList.remove("c#")
print(langList)
# Note: If there are more than one item with the specified value, the remove() method removes the first occurrence

# reomve specific index
# Note: If you do not specify the index, the pop() method removes the last item.
langList.pop(1)
print(langList)

# remove using the del kwyword
del langList[0]
print(langList)
# del langList  - this will remove the entire list

# Clear list - clear() method empties the list. The list still remains, but it has no content.
langList.clear()
print(langList)