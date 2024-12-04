firstTuple=("name", 'age', 'email')
print(firstTuple)
print(len(firstTuple))
# Note: Tuples are written with round brackets.
# Important: Tuple items are ordered, unchangeable, and allow duplicate values.
  # Ordered: It means that items have a defined order and it will not change
  # Unchangeable: Means that we cannot change add or remove after the tuple has been created
  # Allow Duplcates: Since tuples are orderd by index they can have item with same value

# Create tuple with one item
oneItemTuple=("Single-item")
print(oneItemTuple)
print(type(oneItemTuple)) # <class 'str'> - this single item tuple isn't considerd as tuple - To define a single item tuple you have to add , in the and of the item, just like we do for multile items

oneItemTupleCorrectWay=("Correct-single-tupple",)
print(oneItemTupleCorrectWay)
print(type(oneItemTupleCorrectWay))

# create tuple using constructor function
constructorTuple=tuple(('this', 'is', 'constructor', 'tuple'))
print(constructorTuple)

# Access tuple - we can access a tuple item just like we can access with list item
print(firstTuple[1])

# Update Tuple
# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

updateTuple=("Ashraf", "Chowdury")
updatedTuple=list(updateTuple)
print(type(updatedTuple))

updatedTuple[1]="Uddin"
updateTuple=tuple(updatedTuple)
print(type(updateTuple))
print(updateTuple)

# We can update tuple items after converting it to an list type and update the items after that convert it to tuple again. - Not a very effective way to do

# Unpacking a Tuple
fruits = ("apple", "banana", "cherry")
(fruit1, fruit2, fruit3)=fruits
print(fruit1, fruit2, fruit3)

# Note: The number of variables must match the number of tuple item, if not you have to use 'asterisk*' the collect the remaining valus as list
(fruit1, *rest)=fruits
print(fruit1) # type: string
print(rest) # type: list

# Join tuples
tupleOne=(1, 2, 3)
tupleTwo=(4, 5, 6)
print(tupleOne + tupleTwo)
# Multiply Tuples - it will multiply rhe content of a tuple items
print(tupleOne * 2)
