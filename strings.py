# String can be assigned using both single and double qouates
name = 'Ashraf'
full_name = 'Ashraf Chowdury'

print(name)
print(type(name))

# Assign multiple lines of strings
multiples_lines_of_string = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

print(multiples_lines_of_string)

# Accessing a specific character in string in PY - Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
print(name[1]) # Output: s

# Looping Through a String
for new_name in name:
    print(new_name) 

# Get the length of a string using the len() function
print(len(name))

# Check String - To check if a certain phrase or character is present in a string, we can use the keyword in.
print(full_name in 'Chowdury')

# Check if not exist
print(full_name not in "Uddin")


# Slicing Strings

# By using the slice syntax we cann get a range of characters - Specify the start index and the end index, separated by a colon, to return a part of the string.
print(full_name[0:6])

# You ccan define the the first character using position 0 or just leaving it empty
print(full_name[:6])
# Same gose to end slice
print(full_name[7:])

# Note: We can use negative indexes to start the slice from the end of the string.


# Modify strings
# Make the stirng all uppercaase
print(name.upper())

# Make the stirng all lowercase
print(name.lower())

# Remove whitespace from start and the end of the string
unformatted_name=' Ashraf '
print(unformatted_name.strip())

# Replace string
print(name.replace('A', 'H'))

# Split string
print(full_name.split(' '))


# String Concatenation
first_name='Ashraf'
last_name='Chwodury'
print(first_name + " " + last_name)

# Tring format / Fstring
# we cannot combine strings and numbers like this: "My name is John, I am " + age

# F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.
# To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations. - f-string is similar to what we have in javscript `anything ${age}`
age = 22
header=f"My name is Ashraf and I'm {age} years old"
print(header)
