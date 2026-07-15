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
# ._asdict method - return namedtuple as an ordered dictionary having field name as key and that field vale as value of key
print(rec1._asdict())
# ._fields - return field names as a tuple
print(rec1._fields)
# ._replace - create new instance with changed field values
rec2 = rec1._replace(name="def", department="server")  # we can replace as many field values using .replace method
print(rec2)  # -> employee(id=123, name='def', department='server')
# ._make - create a new instance from iterables
li = [456, "john", "backend"]
rec3 = employee._make(li)
print(rec3)  # -> employee(id=456, name='john', department='backend')

# ordereddict ->
from collections import OrderedDict
dict1 = OrderedDict({"name" : "abc", "age" : 12, "hobby" : "running"})
# .move_to_end - moves key:value pair to end
dict1.move_to_end("hobby")
print(dict1)  # -> OrderedDict({'name': 'abc', 'age': 12, 'hobby': 'running'})
# .move_to_end(key argument, last=False) - moves key:value pair to beginning
dict2 = OrderedDict({"maths" : 91, "physics" : 90, "chemistry" : 88})
dict2.move_to_end("chemistry", last=False)
print(dict2)  # -> OrderedDict({'chemistry': 88, 'maths': 91, 'physics': 90})
# .popitem - removes last inserted key:value pair, same as regular dictionary
#            but in ordered dictionary we can remove first inserted key:value pair using .popitem method which we can't do in regular dictionary
dict3 = OrderedDict({"maths" : 91, "physics" : 90, "chemistry" : 88})
dict3.popitem(last=False)  # removes "maths":91 key:value pair
print(dict3)  # -> OrderedDict({'physics': 90, 'chemistry': 88})

