# Note - as dictionary is mutable, dictionary methods transform original dictionary

# .clear - clears whole dictionary

# .copy - copy dictionary and returns copied ditinoary
a1 = {
    "name" : "abc",
    "age" : 12,
}
a2 = a1.copy()
print(a2)

# .get - return value of specific keys
# Note -> .get will return None if key is not present in dictionary
b = {
    "name" : "abc",
    "age" : 12,
}
print(b.get("name"))

# .keys - return a list containing keys of dictinary
# Note -> .keys method returns output as adict_keys() view object instead of actual list 
#         the output dict_keys([...]) is the string representation of this view object
#         to get list output, we need to typecast the output
d = {
    "name" : "abc",
    "age" : 12,
    "hobby" : "running"
}
print(d.keys())  # return string representation of view object 
print(list(d.keys()))  # list representaion of output -> ["abc", 12, "running"]

# .values - return a list containing values of dictinary
# Note -> .values also give string representation output of dict_values([...]) view object 
#         to get list output, we need to typecast the output
print(d.values())

# .items - return a list containing tuple of key:value pairs
# Note -> .items also give string representation output of dict_items([...]) view object
#         to get list output, we need to typecast the output
c = {
    "name" : "abc",
    "age" : 12,
    "hobby" : "running"
}
print(c.items())  # -> [("name", "abc"), ("age", 12), ("hobby", "running")]
print(c.items()[0])  # -> [("name", "abc")], 0 indexed element of returned list
print(c.items()[0][0])  # -> "name"

# why dictionary provides output of .keys, .values and .items methods as view object:
# -> because it provides dynamic and memory efficient reference to dictionary's keys
# -> this view object automatically reflects changes to underlying dictionary wihtout creating a static copy which improves performance
# -> In Python 2, these methods returned lists (static copies). If the dictionary changed after the list was created, the list would become outdated, leading to potential inconsistencies.

# .fromkeys - it creates a new dictionary using keys from a given iterable object(list, tuple, set) and give same default values to all
# Note -> .fromkeys method is used with dict class -> d = dict.fromkeys(iterable object, default value)
d1 = dict.fromkeys(['a', 'b', 'c'])  
print(d1) # -> {'a' : none, 'b' : none, 'c' : none}
d2 = dict.fromkeys((1, 2, 3), 'x')  
print(d2) # -> {1 : 'x', 2 : 'x', 3 : 'x'}, each key has same value 'x'
# if we give mutable object as default value ->
d3 = dict.fromkeys({'a', 'b', 'c'}, [])  # default value for each keys is an empty list which is mutable object
#                                            -> {'a' : [], 'b' : [], 'c' : []}
d3['a'].append(1)  # we are updating value of only 'a' key by appending 1 to its list
print(d3)  # -> {'a' : [1], 'b' : [1], 'c' : [1]}, but despite of updating value of only 'a', values of 'b' and 'c' also get updated automatically

# .pop - removes the element(key:value pair) with specefic key
# Note - if argument key is not present in dictionary, it will give error
e = {
    "name" : "abc",
    "age" : 12,
    "hobby" : "running"
}
e.pop("hobby")
print(e)

# .popitem - removes last inserted key value pair
# Note - using .popitem method in empty dictionary gives error
f = {
    "name" : "abc",
    "age" : 12,
    "hobby" : "running"
}
f.popitem()
print(f)  # -> {"name" : "abc", "age" : 12,}

# .setdefault - return the value of specific key, but if key is not present in dictionary insert the key:value pair
# Note - in .setdefault method we pass two argument, first one for key and second one for value
g1 = {
    "name" : "abc",
    "age" : 12,
    "hobby" : "running"
}
val = g1.setdefault("hobby", "reading") # as key "hobby" is already present in dictionary g1 it will return its value -> "running"
g2 = {
    "name" : "abc",
    "age" : 12,
}
g2.setdefault("hobby", "reading")  # as key "hobby" is not present in dictionary g2, it will create a new key:value pair of "hobby":"reading"
print(g2)

# .update - used to update value for a particular key or to insert a new key:value pair
h1 = {
    "name" : "abc",
    "age" : 12,
}
h1.update({"name" : "def"})  # as key "name" is present in dictionary, the value of key "name" will update to "gef"
print(h1)  # -> {"name" : "def", "age" : 12,}
h1.update({"hobby" : "running"})  # as key "hobby" is not present in dictionary, it will create a new key value pair
print(h1) # -> {"name" : "def", "age" : 12, "hobby" : "running"}
h2a = {
    "name" : "abc",
    "age" : 12,
}
h2b = {
    "maths" : 91,
    "physics" : 90,
    "chemistry" : 89,
}
h2a.update({"marks" : h2b})
print(h2a)  # -> {'name': 'abc', 'age': 12, 'marks': {'maths': 91, 'physics': 90, 'chemistry': 89}}