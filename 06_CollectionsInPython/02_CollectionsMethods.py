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
employee = namedtuple("employee", ["id", "name", "department"])  # created a namedtuple employee having name "employee"
rec1 = employee(123, "abc", "IT")
# ._asdict method - return namedtuple as an ordered dictionary having field name as key and field element as values
print(rec1._asdict())
# ._fields - return field names as a tuple
print(rec1._fields)
# ._replace - create new instance with changed field values
rec2 = rec1._replace(name="def")
print(rec2)  # -> employee(id=123, name='def', department='IT')
# ._make - create a new instance from iterables
li = [456, "john", "backend"]
rec3 = employee._make(li)
print(rec3)  # -> employee(id=456, name='john', department='backend')