# counter ->
# counter is a dictionary subclass that store iterable object's elements as keys, count their frequency in object and store them as values
# Note -> we can pass string, tuple, list, set in Counter subclass
#         but as it is a dictionary subclass, we can't use mutable objects as keys 
#         so if we are using list as iterable to pass in Counter, we can't use nested list, set and any other mutable objects inside that list
#         ex -> [1,2,"hello",(1,2)]  - valid
#            -> (1,'a', [1,2,3])  - invalid, gives error
from collections import Counter
a1 = ['a','b','a','c','a'] 
a1_counter = Counter(a1)
print(a1_counter)  # -> Counter({'a': 3, 'b': 1, 'c': 1})
a2 = "Hello"
a2_counter = Counter(a2)
print(a2_counter)  # -> Counter({'l': 2, 'H': 1, 'e': 1, 'o': 1})
# Note -> as a1_counter and a2_counter are dictionaries, we can use all dictionary methods in them
# .most_common method in counter - return a list of key:value pairs as tuple having key with most occurances, returns output same as .items method in dictionary

# namedtuple ->
# namedTuple is a lightweight, immutable data structure from Python's collections module that creates tuple-like objects with named fields. 
# It combines the memory efficiency of tuples with the readability of classes
# characteristics of namedtuple: 
# Immutable - values cannot be changed after creation
# Accessible by name or index - fields can be accessed using dot notation or numeric indices
# Memory efficient - uses less memory than regular classes
# Self-documenting - field names make code more readable
# Note -> we pass two parameters to namedtuple, first is name of namedtuple and second is
from collections import namedtuple
employee = namedtuple("employee", ["id", "name", "department"])  # created a namedtuple employee having name "employee"
rec1 = employee(123, "abc", "IT")  # creating instances
rec2 = employee(456, "def", "server") 
print(rec1)  # -> employee(id=123, name='abc', department='IT')
print(rec1.name)  # -> abc, accessing element from namedtuple using field name
print(rec1[1])  # -> abc, accessing element from namedtuple using index
print(rec2.id)  # -> 456 
print(rec1[0])  # -> 123

