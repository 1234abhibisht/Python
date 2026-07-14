# list is a mutable object
# Note -> list is heterogeneous, it can hold any datatype such as integer, float, boolean, string, character
#         list can also hold any other python object inside it like another list(nested), tuple, dictionary, set
#         list can also hold special objects such as None, functions, classes

# difference between list and array
# -> list can store elements of different datatypes but array can store elements of single datatype
# -> list can store integers, floats, strings together but an array of integers can store only integers and array of character can store only characters

# difference between list and string
# -> list is mutable object while string is an immutable object
# -> list can store elements of different datatypes while string can store only character elements

# time complexity - inesertion and deletion take O(n) time complexity due to contiguous memory
#                   as internal structure of list is dynamic array, so to inserting or removing element requires shifting

# empty list 
li = []
# Note -> we can add elements to an empty list using .append or .insert methods

# list of integers
a = [1,2,3,4]

# list of floats
b = [1.1, 1.2, 1.3]

# list of characters
c = ['A', 'b', 'C', 'd']

# list of strings
d = ["Hello", "world"]

# list of boolean
e = ["True", "False"]

# list of all datatype combined
abcde = [1, 1.1, 'A', "Hello", "True"]

# list of list(nested)
f = [1,[2,3],[4,5]]
print(f[1])  # -> [2,3]
print(f[2][1])  # -> 5

# list of tuples
g = [(1,2),(3,4),(5,6)]
print(g[0])  # -> (1,2)
print(g[1][0])  # -> 3

# list of sets
h = [{1,2},{3},{4,5}]

# list of dictionary 
i = [{1 : 12, 2 :13}, {'A' : 'a', 'B' : 'b'}, {"abc" : 1, "def" : 2}]

# list of all objects combined
fghi = [[1,2], (3,4), {5,6}, {"abc" : 1}]

# joining two lists(list concatenation)
l1 = [1,2,3]
l2 = [4,5]
print(l1 + l2)  # -> [1,2,3,4,5]

# list slicing (same as string slicing)
j = [1,2,3,4,5]
print(j[0:2])  # -> [1,2]
print(j[:4])  # -> [1,2,3,4]