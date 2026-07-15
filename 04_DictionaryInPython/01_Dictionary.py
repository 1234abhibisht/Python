# dictionary is a mutable object that contains elements in a key:value pair, we can add or remove any key:value pair
# addition, removal and updation of key value pair happens in orignal dictionary due to its mutability
# keys in dictionary are unique

# Note -> before python 3.7 key:value pairs in dictionary were unordered collections, means they can change between runs
#         but from python 3.7, key:value pairs maintain the insertion order in every run

# keys of dictionary must be immutable objects or datatypes such as integer, float, bool, character, string, tuple
# Note -> mutable objects such as list, set can't be keys of dictionary because dictionary uses hash value from keys to find memory block where is value is stored
#         if a key could change after being added to the dictionary, its hash value would change, causing the dictionary to lose track of the associated value. 
# values can be of any object and datatype including mutable ones such as list and set

# empty dictionary
dict = {}
# Note -> we can add elements(key:value pairs) to empty dictionary using .update method

# dictionary of datatypes
a = {
    1 : 2,
    1.2 : 2.3,
    'A' : 'a',
    "abc" : True
}

# dictionary of objects
b = {
    'a' : [1,2,3],
    'b' : (4,5,6),
    'c' : {1,3,4},
    'd' : "abc",
    (1,2) : "ab",
}
print(b)

# output of values from a dictionary
c = {
    "name" : "abc",
    "age" : 12,
}
print(c["name"])  # -> abc
print(c["age"])  # -> 12
# Note -> we can also take output of values from a dictionary using .get method
#         this method will give error if key is not present in dictionary but .get method will give None if key is not present in dictionary

# updation of values in a dictionary
# Note -> if a key is already present in a dictionary with a value, then inserting a key:value pair with same key but different value will update previous value
d = {
    "name" : "abc",
    "age" : 12,
    "marks" : [90, 91, 88]
}
d["name"] = "def" # now value of key "name" is updated to "def"
d["age"] = 15
print(d)

# inserting new key:value painr in a dictionary
e = {
    "name" : "abc",
    "age" : 12,
}
e["hobby"] = "running"  # a new key value pair ("hobby" : "running") will be created in dictionary e
print(e)

# Note -> we can update a key:value pair or insert new key:value pair using .update method also

# equality condition for two dictionaries
# two dictionaries are equal only if both have same key:value pairs, order doesn't matter
dict1 = {
    "maths" : 91,
    "physics" : 90,
}
dict2 = {
    "physics" : 90,
    "maths" : 91,
}
print(dict1 == dict2)  # True, as order doesn't matter

# nested dictionary
f = {
    "name" : "abc",
    "age" : 12,
    "marks" : {
        "maths" : 90,
        "physics" : 91,
        "chemistry" : 88,
    }
}
print(f["marks"]["maths"])  # -> 90
print(f["marks"]["physics"])  # -> 91

# taking output of only one key:value pair from a dictionary
c = {
    "name" : "abc",
    "age" : 12,
    "hobby" : "running"
}
pair = list(c.items())  # returns list of key value pairs as tuple
print(pair[0])  # prints first element or tuple of key value pair from the list