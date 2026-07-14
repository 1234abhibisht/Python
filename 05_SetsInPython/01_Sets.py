# sets are unordered, mutable collection of unique elements 
# unlike lists or tuples, sets automatically eliminate duplicate entries and do not maintain the order of insertion
# sets themselves are mutable, they can't be used as keys in dictionary

# Note -> as sets are mutble, but elements inside set must be immutable or hashable
#         we can add datatypes such as integers, float, boolean and itrable objects such as tuple, string only not list, dictionary

# unlike list internal structure of sets are hash table, so sets are unordered and do not has index like list or tuple for its elements

# empty set
st1 = set()
st2 = set([])  # it will also create an empty set

# declaration
a1 = {1,2,3,4}
print(a1)  # -> {1,2,3,4}, according to hash table
a2 = {111,100,232}
print(a2)  # -> {232, 100, 111}, unordered collection according to hash table

# set of tuple
b = {(1,2), (3,4)}

# set of string
c = {"abc", "def", "ghi"}
print(c)

# hasing mechanism in set
# Internally, a set is implemented as a hash table where each element acts strictly as a key with no associated value. 
# In a Dictionary: Python hashes the key to locate a specific memory slot where a value is stored. 
# In a Set: Python hashes the element itself to locate a memory slot.  If the slot contains that specific element, it exists in the set. If the slot is empty, the element is absent. 
# Essentially, a set is a dictionary where the keys are the values, and the "values" are merely placeholders indicating presence

# memory and performance
# Lookup Speed: Sets are the fastest data structure for membership testing (x in my_set). This is due to their underlying implementation using hash tables. 
# Insertion/Deletion: Adding or removing elements is generally O(1) on average.
# Memory Overhead: Sets consume significantly more memory than lists or tuples of the same size because they must allocate extra space for the hash table to handle collisions. 
# Iteration: Iterating over a set is generally slower than iterating over a tuple or list due to the lack of contiguous memory storage.

# how hasing enables speed O(1)
# When you perform operations like x in my_set or my_set.add(x):
# Hash Calculation: Python calls hash(x) to convert the element into a fixed-size integer. 
# Index Mapping: This integer determines the index in the internal array (hash table) via a modulo operation (index = hash(x) % table_size). 
# Direct Access: Python jumps directly to that memory index.
# Lookup: If the slot is empty, the element is not in the set. If occupied, Python verifies equality.
# Insertion: If the slot is empty, the element is placed there.
# Collision Handling: If two elements hash to the same index, Python uses probing (checking nearby slots) to find the correct location or an empty one. 
# This avoids iterating through the collection, providing average O(1) (constant time) performance, whereas lists require O(n) (linear time). 

# about hashable objects or values :
# hashable objects or values in python are the objects the have constant hash value throughout their lifetime
# for an object to be hashable, it should satisfy two condidions ->
# Implement __hash__(): It must return a fixed integer value. 
# Implement __eq__(): It must be comparable to other objects, where equal objects yield equal hash values.
# Note -> all datatypes such as integer, float, string, character and immutable objects such as tuple, frozenset and some other functions such as range and some user defined classes are hashable

# about hash function
# hash(x) returns an integer hash value of object x that acts as unique fingerprint for that object
# objects that compare equal (using ==) must have the same hash value.  For example, hash(1) and hash(1.0) return the same integer because 1 == 1.0.
print(hash(10))  # -> 10, as integers hash to themselves
print(hash("hello"))  # -> 801632708448556916, returns a large random integer
# Note -> for security reasons (hash randomization), the hash value of strings and bytes may differ between different runs of the Python interpreter, 
#         though it remains constant within a single session.
print(hash((1,2,3)))  # as tuples are immutable they are hashable but only if all of its elements are hashable.

# Note -> only immutable interable objects are hashable such as tuple, string, frozenset using hash function
#         we cant't hash set, but set uses a hash table for insertion, searching and deletion thats why elements of sets must be immutable
#         passing set in a hash function gives error as set itself is mutable