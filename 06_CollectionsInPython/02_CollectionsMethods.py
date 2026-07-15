# counter -> 
from collections import Counter
a3 = "abcaaba"
a3_counter = Counter(a3)
print(a3_counter.most_common(1))  # -> [('a', 4)], top one key with most occurances in argument object
print(a3_counter.most_common(2))  # -> [('a', 4), ('b', 2)], top two keys with most occurances in argument object
# Note -> if no argument is passed in .most_common method it will return list of all key:value pairs as tuple
print(a3_counter.most_common())  # -> [('a', 4), ('b', 2), ('c', 1)]

# namedtuple ->
from collections import namedtuple
