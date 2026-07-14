# strings are immutable objects, once declared they cannot be changed

# string declaration
a1 = "Hello"  # declared using " "(double quotes)
a2 = 'Hello'  # can also be declared using ' '(single quotes)
a3 = """Hello"""  # can also be declared using """ """(triple quotes)
print(a3)

# using single quotes inside double quote string
b = "Mother's name"
print(b)  # -> Mother's name

# using double quotes inside single quote string
c = 'Mother"s name'
print(c)  # -> Mother"s name
# Note - we can't do 'Mother's name', as second single quote will immediately close the string

# string concatenation
d1 = "Hello" + "World"
print(d1)  # -> HelloWorld
d2 = "Hello" + ' ' + "World"
print(d2)  # -> Hello World

# length of string
e = "Hello World"
print(len(e))  # -> 11
# Note - whitespace is also a character, so it will be counted in a string length

# escaping characters in a string -> / is used to escape the just next character from a string
f1 = "Mother\"s name"  # "Mother"s name" is invalid string representation, as second double quote will close string immediately
#                        but \ will escape the second double quote and make it a part of string
print(f1)  # -> Mother"s name
f2 = 'Father\'s name'
print(f2)  # -> Father's name