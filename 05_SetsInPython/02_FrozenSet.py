# frozen set is the immutable version of set, once declared can't be modified

# key characteristics of fronzenset
# Immutable: Unlike a standard set, you cannot change a frozenset after creation. Methods like .add(), .remove(), or .discard() are unavailable and will raise an AttributeError. 
# Hashable: Because its content is fixed, a frozenset has a stable hash value. This allows it to be used as a dictionary key or as an element inside another set. 
# Unordered: Like regular sets, frozenset does not maintain element order. 
# Unique Elements: It automatically removes duplicates upon creation, same as set.

# Note -> same as set we can insert immutable elements in a frozenset

# empty forzenset
fst = frozenset()

# declaration of frozenset
# from a list
a = frozenset([3,4,1,5,2])
print(a)  # -> frozenset({1,2,3,4,5}), unordered according to the hash table
# from a tuple
b = frozenset((1, 2, 3,'a','b'))  # -> frozenset({1, 2, 3, 'a', 'b'}), unordered according to the hash table
print(b)
# from a list
c = frozenset("Hello")
print(c)  # -> frozenset({'e', 'o', 'H', 'l'}), unordered according to the hash table
# from a set
d = frozenset({111,100,232})  # -> frozenset({232, 100, 111}), unordered according to the hash table
print(d)

# Note -> we can declare a frozenset from a list, tuple, string, set but elements inside these iterables mush be immutable
e = frozenset([(1,2), "abc"])  # this is a frozenset of list but contains only immutable objects inside it
print(e)  # -> frozenset({(1, 2), 'abc'})
f = frozenset({1,2,(3,4)})  # this is a frozenset of set but contains only immutable objects inside it
print(f)  # -> frozenset({1, 2, (3, 4)})
g = frozenset(("abc", [1,2], 'c'))  # this is a fronzenset of tuple but contains a list inside it, so it will give error while printing
print(g)  # -> error