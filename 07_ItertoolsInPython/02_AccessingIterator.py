# itertools functions return iterator, to access this iterator we can use two methods:
# -> using iter() and next() functions
# -> typecasting iterator output to a iterable object

# iter() and next() functions are used to manually control iterations in an iterable
# -> iter() function convert iterables such as list, tuple, set to an iterator object
#    it returns a new iterator object pointing its internal pointer to position just before first element of iterable, it do not modify original iterable
#    Purpose: It initializes the iteration process and returns an object that keeps track of the current position in the sequence. 
#    Mechanism: Internally, it calls the object's __iter__() method. 
#    Usage: You must call this once to get the iterator before you can start retrieving items
# Note -> when iter() is called on an iterable, the returned iterator object initializes its internal pointer to a position just before the first element
#         imagine an iterator over ['A', 'B', 'C'], at initial state the iterator's internal pointer is point before 'A'.

# -> The next() function retrieves the next item from the iterator created by iter(). 
#    Purpose: It advances the iterator and returns the current element. 
#    Mechanism: Internally, it calls the iterator's __next__() method. 
#    Behavior: Returns the next available item.
#              Raises a StopIteration exception if no items remain (unless a default value is provided)
#    next() performs two actions atomically:
#       Retrieves the value at the current position (which is the "next" item in the sequence relative to the previous call).
#       Advances the pointer to the subsequent item for the following call.
# Visualizing the working state of next() function:
# Imagine an iterator over ['A', 'B', 'C']:
# Initial State: iterator's internal pointer is before 'A'.
# "Next item" to be retrieved is 'A'.
# Call next():
# Returns 'A' (the current target).
# Moves cursor to before 'B'.
# Next Call:
# Now, the "next item" to be retrieved is 'B'.
# Note -> after the next() function returns the last element of an iterable, the iterator's internal pointer moves to a position just after the last element
#         if we call next() again, there are no more items to retrieve. Consequently, Python raises a StopIteration exception to signal that the sequence is complete

li = ['a', 'b', 'c']
res1 = iter(li)
print(next(res1))  # -> 'a'
print(next(res1))  # -> 'b', as next function updated iterator's internal pointer
print(next(res1))  # -> 'c'

from itertools import product
a = [1,2]
b = [3,4]
res = (product(a,b))  # -> (1,3),(1,4),(2,3),(2,4)
# Note -> we do not need to convert output of product to iterator object as it returns iterable object itself
print(next(res))
print(next(res))