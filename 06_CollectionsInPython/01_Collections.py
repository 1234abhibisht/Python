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
# Note -> normal touple methods also work in namedtuple along with some special methods

# ordereddict - ordereddict is a dictionary subclass from python collection module, it is mutable and is same as dictionary
#               as dictionary, ordered dictionary also maintain the ordered in which key:value pairs are inserted
# key characteristics:
# Remembers insertion order - items are iterated in the order they were added
# Equality is order-sensitive - two OrderedDicts are only equal if they have the same key-value pairs in the same order
# Provides reordering methods - can move items to beginning or end
# Backward compatible - useful for Python versions before 3.7 where dicts weren't ordered
# difference between regular dictionary and ordred dictionary :
# -> regular dictionary maintains insertion order in python 3 versions but ordered dictionary maintains insertion order in previous versions also
# -> for two regular dictionary to be equal order doesn't matter but for two ordered dictionary to be equal order matters along with same key:value pairs
# -> in ordered dictionary we can move key:value pair to end or beginning which we can't do in regular dictionary
from collections import OrderedDict
dict1 = OrderedDict({"name" : "abc", "age" : 12})
print(dict1)  # -> OrderedDict({'name': 'abc', 'age': 12})
# Note -> regular dictionary methods also work in ordered dictionary along with some special methods
print(list(dict1.values()))
dict2 = OrderedDict({})
dict2["hobby"] = "running"
dict2.update({"class" : 5})
print(dict2)  # -> OrderedDict({'hobby': 'running', 'class': 5})
# Note -> Use regular dict by default. Python dictionaries now maintain insertion order, making OrderedDict mostly unnecessary for everyday use as both has almost same memory efficiency. 
#         Save OrderedDict for specialized cases where you need its extra functionality

# defaultdict - it is a dictionary subclass from python collections module, it is mutable and is same as dictionary
#               if we define a key in default dictionary without assigning its value, default dictinoary will automatically assign default value to it
#               it automatically returns a default value for missing keys, if a key is not present in dictionary instead of raising error it returns a default value
from collections import defaultdict
# different factory functions
dd_int = defaultdict(int)        # Default value: 0
dd_list = defaultdict(list)      # Default value: []
dd_set = defaultdict(set)        # Default value: set()
dd_str = defaultdict(str)        # Default value: ''
dd_dict = defaultdict(dict)      # Default value: {}
dd_bool = defaultdict(bool)      # Default value: False
# creating a default dictionary
def_dic1 = defaultdict(int)
def_dic1['a'] = 1
def_dic1['b'] = 2
print(def_dic1['a'])  # -> 1
print(def_dic1['c'])  # -> 0, as key 'c' is not present in def_dic1 default dictionary, instead of raising error it will return a default value of integer which is 0
def_dict2 = defaultdict(list)
def_dict2["key"]  # we didn't assing value to key "key" but default dictionary will assign default value of list automatically to it
print(def_dict2["key"])  # -> []
# Note -> we can use regular dictionary methods in default dictionary
# common use cases of default dictionary:
# -> grouping items
words = ['apple', 'apricot', 'banana', 'blueberry', 'cherry', 'coconut']  # we want to group these words according to first letter in a dictionary
grouping = defaultdict(list)
for i in words :
    grouping[i[0]].append(i)  # we didn't assign value to this key so default dictionary will automatically assign deafult value of list [] to it -> key:[]
print(grouping)  # -> defaultdict(<class 'list'>, {'a': ['apple', 'apricot'], 'b': ['banana', 'blueberry'], 'c': ['cherry', 'coconut']})
# -> counting items(alternative counter collection)
# -> building complex data structures
# -> used in graph datastructres(for adjacency lists)

# dequeue - dequeue means double ended queue, it is a datastructure from python collections module
#           it is a dynamic datastructure used to fast insertion and deletion from both the ends with time complexity of O(1)

from collections import deque
# empty dequeue
dq1 = deque()
# initializing dequeue
dq2 = deque([1,2,3,4,5])
print(dq2)  # -> deque([1, 2, 3, 4, 5])
# bounded dequeue - it is a dequeue with fixed size
dq3 = deque([1,2,3,4,5], maxlen=5)  