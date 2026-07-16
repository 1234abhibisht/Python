# Note -> all string methods copies the original string transform it and return a new string, original string is unaffected, as strings are immutable
# -> in order to modify original string, we need to update original string with new string
#    ex - str = "hello"
#         str = str.capitalize(),  this will modify original string with new returned string

str = "hello"

# .capitalize - makes first letter of string capital
print(str.capitalize())

# .replace - replace string or letter of string with another string or another word 
print(str.replace("h","i"))

# .find - returns index of first occurence of an element from left in a string
# Note -> return -1 if element is not found in string
a = "banana"
print(str.find("a"))  # -> 1
print(str.find("s"))  # -> -1, as s is not found in "banana"
 
# .rfind - returns the index of first occurence from right of an element in a string
# Note -> return -1 if element is not found in string
print(a.rindex("a"))  # -> 5

# .index - returns index of first occurence of an element from left in a string
# Note -> throws an error if element not found in string
print(a.index("a"))  # -> 1
print(a.index("n",2,5))  # searches between index 2 to 5

# .rindex - returns the index of first occurence from right of an element in a string
# Note -> throws an error if element not found in string
print(a.rindex("a"))  # -> 5

# .endswith - return true if string ends with the argument passed otherwise false
print(str.endswith("lo"))

# .startswith - returns true if string starts with the argument passed otherwise false
print(str.startswith("h"))

# .upper - converts all lowercase elements of string to uppercase
print(str.upper())

# .lower - converts all uppercase elements of string to lowercase
print(str.lower())

# .swapcase - swaps upper case element and lower case elements in a string
print(str.swapcase())  # -> hELLO

# .casefold - also converts all uppercase elements of string to lowercase

# .count - count the occurence of the argument passed in the string\
b = "Pokemon Doraemon"
print(b.count("mon"))
print(b.count("hel"))

# .center - returns a new string having old string centered padded with characters(spaces by default) on both sides 
print(str.center(11,"*"))
# 11 is the total size of new string with padded characters
# "*" is the character padding the original string from left and right
# .center method also has an alternative using .format method or f string
# Note - .center will do nothing if argument passed is less than or equal to size of string
#        .center will create a copy of string do center padding and return a new string, original strig is unaffected

# .format - insert values in place of placeholders defined by {}
# positional arguments
print("hello how {} {}".format("are", "you"))
# indexed arguments
print("{1} {0}".format("good", "boy"))   # good will insert to 0, boy will insert to 1
# keyword arguments
print("{name} is {age} years old".format(name="abc", age="20"))
# format specifiers - control number precision and alignment
# we can do string truncation, number precision and alignment of string using : inside {} placeholder
# string truncation -> "{:.N}".format(), where N is number of elements of string to return
c = "Hello World"
print("{:.7}".format(c))  # first 7 elements of string will return
# Number precision -> "{:.Nf}".format()
pi = 3.14159
print("{:.2f}".format(pi)) # f is type(float), 2 is number of integers to print after decimal
# string alignment
print("{:<10}".format(str))  # pad string to left having total padded size 10 -> "Hello       "
print("{:>10}".format(str))  # pad string to right having total padded size 10 -> "     Hello"
print("{:^11}".format(str))  # pad string to centre having both side spaces with total padded string size 11
print("{:*^11}".format(str)) # pad string to centre having both side * with total padded string size 11
# Note -> .format method has replacement as f string introduced in python 3.6, which is faster and readable

# .format_map - it insert dictionary to the placeholders in a string
str1 = "My name is {name}, I am {age} years old"
print(str1.format_map({"name" : "abc", "age" : 13}))

# .isalnum - return true if all characters in string are alphanumeric
#            return false for empty string
# Note - alphanumeric characters consist of 26 alphabets (a to z) and numerical values (0 to 9)
d = "abc123"
print(d.isalnum())

# .isalpha() - return true if all characters of string are alphabet
#              return false for empty string
e = "hello"
print(e.isalpha())

# .isdigit() - return true if all characters of string are digits
#              return false for empty string
f = "1234"
print(f.isdigit())

# .isdecimal - return true if all characters of string are decimal

# .isnumeric - return true if all characters of string are numeric

# difference between .isdecimal .isdigit .isnumeric
# -> String   Character Type	.isdecimal()	.isdigit()	.isnumeric()
# "123"	     Standard Digits	   True	           True	        True
# "²"	     Superscript	       False	       True	        True
# "₃"	     Subscript	           False	       True	        True
# "½"	     Fraction	           False	       False	    True
# "Ⅳ"	    Roman Numeral	      False	          False	       True
# "-5"	     Negative Sign	       False	       False	    False
# "3.14"	 Decimal Point	       False	       False	    False

# .isascii() - return true if all characters of string are ascii characters
g1 = "Hello World"
print(g1.isascii())  # -> True
g2 = " "
print(g2.isascii())  # -> True, as " "(space) is also an ascii character with ascii number 32
g3 = ""
print(g3.isascii())  # -> True, also returns true if string is empty
g4 = "Hello\tWorld"
print(g4.isascii())  # -> True, as \t is also an ascii character, even \r \b \n also have ascii value
# Escape Sequence	  Name	            ascii Value
#   \b	          Backspace	               8	
#   \t	          Horizontal Tab	       9	
#   \n	          Line Feed (Newline)	   10	
#   \r	          Carriage Return	       13	
           
# .isidentifier() - return true if string is identifier
#                   return false for empty string, as variable name can't be empty
# Note - Identifier string is a string that follows rules of variable naming
#        -> string should start from alphabet or _
#        -> string must have no special character other than _
#        -> string can have digit at any position except starting 
h = "abc_12"
print(h.isidentifier())

# .islower, .isupper - return true if string has all characters lower case or upper case respectively

# .istitle - return true if string follows title rule
#            return false for empty string
# Note - title rule is a rule in which if a string contains words, then their first alphabet must be upper case
i1 = "My Name Is Abc"
print(i1.istitle())  # -> True
i2 = "My Name Is 123"
print(i2.istitle())  # -> True
i3 = "My name Is Abc"  # -> False, as first alphabet of 'name' is lower case
print(i3.istitle())
i4 = "123"
print(i4.istitle())  # False, as it doesn't have any word so it breaks title rule

# .isspace - return true if all characters of string are whitespaces
j = " "
print(j.isspace())

#.isprintable() - return true if all characters of string are printable
#            return true for empty string
# Note - printable characters are digits, letters, special characters(@, #, $), space(' ')
#        non printable characters are \n, \t, \r, \b
k1 = "ABC123$"
print(k1.isprintable())  # -> True
k2 = "\n"
print(k2.isprintable())  # -> False

# .join - converts elements of an iterable to a string
l = ("Hello", "how", "are", "you")
print("*".join(l))  # -> Hello*how*are*you

# .ljust and .rjust - do left and right alignment padding of string respectively
# these are alternatives of padding and alignment using .format or f string
print(str.ljust(10))  # pad string to left having total padded size 10 -> "Hello       "
print(str.rjust(10))  # pad string to right having total padded size 10 -> "     Hello"
print(str.ljust(10,"*"))  # -> "Hello*****"
print(str.rjust(10,"*"))  # -> "*****Hello"
# Note - .ljust and .rjust will do nothing if argument passed is less than or equal to size of string
#        .ljust and .rjust will create a copy of string do alignments and return a new string, original strig is unaffected


# .split - splits the string at all occurence of a specefic seperator and returns a list
m1 = "Hello how are you"
print(m1.split())  # -> ["Hello", "how", "are", "you"]
m2 = "Hello*how are you"
print(m2.split())  # -> ["Hello*how", "are", "you"]
m3 = "Hello"
print(m3.split())  # -> ["Hello"]
m4 = "Hello*how are you"
print(m4.split("*"))  # -> ["Hello", "how are you"]

# .splitlines - split the string at line breaks and return a list
n = "Hello how are you\nI am fine"  
print(n.splitlines())   

# .strip - returns the trimmed version of string
# Note - by default .strip removes whitespaces, tabs(\t), non printable characters(\n, \r, \b) from starting and end of string
o1 = "  Hello world  "
print(o1.strip())  # -> "Hello World"
o2 = "\nHello World"
print(o2.strip())  # -> " Hello World"
o3 = "xxHello Worldxx"
print(o3.strip("x"))  # -> Hello World
o4 = "...Hello-World..."
print(o4.strip("."))  # -> Hello-World

# .lstrip and .rstrinp - trim elements from left and right of string only respectively
p1 = "  Hello World  "
print(p1.lstrip())  # -> "Hello World  "
p2 = "  Hello World  "
print(p2.rstrip())  # -> "  Hello World"
p3 = "xxHello-Worldxxx"
print(p3.rstrip("x"))  # -> xxHello-World

# .partition - split the string at the first occurene of a specific seperator from left of string into three partions and return a tuple
# Note - tuple contains - (string before seperator, seperator itself, string after seperator)
q1 = "I*love*apple"
print(q1.partition("*"))  # -> ("I", "*", love*apple)

# .rpartition - split the string at the first occurene of a specific seperator from right of string into three partions and return a tuple
q2 = "I*love*apple"
print(q2.rpartition("*"))  # -> ("I*love", "*", apple)

# .maketrans and .translate 
# -> .maketrans method is used to generate a translation table
# -> .translate method is used to apply the translation table to the string and returns a new string, it do not change original string
# Note - A translation table is a mapping(typically a dictionary) that tells python how to transform individual characters in a string
#        Translation table -> {
#                                "a" : "b",
#                                "c" : None
#                            }  -> replace all occurance of 'a' to 'b' and removes all occurance of 'c' in string
#        we can make translation table using .maketrans method and use this as argument in .translate method
r = "Hello World"
# passing only one argument to .maketrans (we will pass a dictionary to it) ->
trans1 = r.maketrans({"l" : "i", "o" : None})  # This will replace all occurance of 'l'  in string with 'i' and remove all occurance of 'o'
print(r.translate(trans1))  # -> Heii Wrid
trans2 = r.maketrans({"l" : None, "o" : None})
print(r.translate(trans2))
# passing two arguments to .maketrans ->
trans3 = r.maketrans("l", "i")  # This will replace of occurance of 'l' with 'i'
print(r.translate(trans2))  # -> Heiio Worid
trans4 = r.maketrans("Hel", "abc")  # This will replace of occurance of 'H' with a, 'e' with 'b', 'l' with 'c'
print(r.translate(trans3))  # -> abcco Worcd
# passing three arguments to .maketrans
trans5 = r.maketrans("l", "i", "o")  # This will replace all occurance of 'l'  in string with 'i' and remove all occurance of 'o'
print(r.translate(trans4))

# .zfill - It is used to fill specific number of zeroes at the beginning of the string
s = "Hello"
print(s.zfill(10))  # It will fill zeroes at the beginning of the string till the size becomes 10 -> "00000Hello"
# Note - .zfill will do nothing if argument passed is less than or equal to size of string
#        .zfill will create a copy of string add 0's at beginning and return new string, original strig is unaffected


# .expandtabs - returns a new string where all occurances of \t in a string are replace by whitespaces
# Note -> By default .expandtab takes argument 8
#         .expandtab method works only on strings that contain \t character
t1 = "Name\tAge"
print(t1.expandtabs())  # -> "Name    Age", Name is of 4 characters and next tab stop is at 8, so \t is replaced by 4 whitespaces
t2 = "A\tB"
print(t2.expandtabs(4))  # -> "A   B", A is one character and next tab stop is at 4, so \t is replaced by 3 white spaces
t3 = "Hello\tWorld"
print(t3.expandtabs(10)) # -> "Hello     World", Hello is of 5 characters and next tab stop is at 10, so \t is replaced by 5 spaces
# Note - resetting on new line
t4 = "Hi\thow\nare\tyou"
print(t4.expandtabs(4)) # -> "Hi  how", \t will be replaced by 2 whitespaces
#                            "are you"  \t will be replaced by 1 whitespace
t5 = "Hello\tWorld"
print(t5.expandtabs(4))  # -> "Hello   World", \t will be replaced by 3 whitespaces
#                              as next tab stop is at 4, but 'Hello' is of 5 characters, then next tab stop will be at next multiple of 4 i.e 8
