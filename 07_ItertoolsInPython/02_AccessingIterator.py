# itertools functions return iterator, to access this iterator we can use two methods:
# -> using iter() and next() functions
# -> typecasting iterator output to a iterable object

# iter() and next() functions are used to manually control iterations in an iterable
# Note -> iter() function convert iterables such as list, tuple, set to an iterator object
#         Purpose: It initializes the iteration process and returns an object that keeps track of the current position in the sequence. 
#         Mechanism: Internally, it calls the object's __iter__() method. 
#         Usage: You must call this once to get the iterator before you can start retrieving items

from itertools import product
a = [1,2]
b = [3,4]
res = (product(a,b))  # -> (1,3),(1,4),(2,3),(2,4)
print(next(res))
print(next(res))