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

# dequeue ->
from collections import deque
# .append -> adds new element from last(right side)
dq1 = deque([1,2,3])
dq1.append(4)
print(dq1)  # -> dequeue([1,2,3,4])
# .appendleft -> adds new element from beginning(left side)
dq2 = deque([1,2,3])
dq2.appendleft(4)
print(dq2)  # -> dequeue([4,1,2,3])
# .extend -> adds new iterable object without braces from last, works same as in list 
dq3 = deque([1,2,3])
dq3.extend([4,5])
print(dq3)  # -> dequeue([1,2,3,4,5])
# .extendleft - adds new iterable object without braces from beginning
dq4 = deque([1,2,3])
dq4.extendleft([4,5])
print(dq4)  # -> dequeue([4,5,1,2,3])
# .remove - removes value of its first occurance from left in a dequeue, works same as in list
dq5 = deque([1,2,3,2,4])
dq5.remove(2)
print(dq5)  # -> dequeue([1,3,2,4])
# .pop - removes last element from dequeue, works same as in list
dq6 = deque([1,2,3,4])
dq6.pop()
print(dq6)  # -> dequeue([1,2,3])
# .popleft - removes first element from dequeue
dq7 = deque([1,2,3,4])
dq7.popleft()
print(dq7)  # -> dequeue([2,3,4])
# .clear - clear whole dequeue
# .index - return index of an element from dequeue, works same as in list
# Note -> .index will give error if element not found in dequeue
dq8 = [1,2,3,2]
print(dq8.index(2))  # -> 1
dq9 = ['a','b','c','d','e']
print(dq9.index('c',1,3))  # searches between index 1 to 3
# Note -> there is no .find method in dequeue
# .copy - copies a dequeue 
# .count -> count occurances of an element in a dequeue
# .reverse -> reverse the dequeue
# practical use cases of dequeue:
# -> queue implementation(FIFO)
# -> stack implementation(LIFO)
# -> sliding window algorithm