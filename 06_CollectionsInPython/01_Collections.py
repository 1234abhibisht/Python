# counter is a dictionary subclass that store iterable object's elements as keys, count their frequency in object and store them as values
# Note -> we can pass string, tuple, list, set in Counter subclass
#         but as it is a dictionary subclass, we can't use mutable objects as keys like -> a = ([1,2], [3,4], [1,2])
from collections import Counter
a1 = ['a','b','a','c','a'] 
a1_counter = Counter(a1)
print(a1_counter)  # -> Counter({'a': 3, 'b': 1, 'c': 1})
a2 = "Hello"
a2_counter = Counter(a2)
print(a2_counter)  # -> Counter({'l': 2, 'H': 1, 'e': 1, 'o': 1})
# Note -> as a1_counter and a2_counter are dictionaries, we can use all dictionary methods in them
# .most_common method in counter - return a list of key:value pairs as tuple having key with most occurances 
a3 = "abcaaba"
a3_counter = Counter(a3)
print(a3_counter.most_common(1))  # return list having only one most occurance key
print(a3_counter.most_common(2))