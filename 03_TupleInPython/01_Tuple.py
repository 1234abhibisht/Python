# tuples are immutable
# tuples are heterogeneous, we can store any datatype(integer, float, boolean, string) and any objects(list, dictionary, set, nested tuple) inside it
# tuples can be used as keys in dictionary as they are immutable
# Note -> we can't add elements in an empty tuple as they are immutable

# as tuples are immutable they are hashable but only if all of its elements are hashable.

# declaration 
a = (1,2,3)

# Tuples are generally more performant and memory-efficient than lists:
# Memory Usage: Tuples consume less memory because Python allocates a fixed, contiguous block of memory for them at creation. Lists over-allocate memory to accommodate dynamic resizing. 
# Iteration Speed: Iterating over a tuple is slightly faster due to the lack of mutability checks and optimized internal storage. 
# Creation Time: Creating a tuple is faster than creating a list of the same size.

# Why to use tuple:
# Data Integrity: To ensure a collection of items remains constant throughout program execution. 
# Dictionary Keys: Since lists are mutable, they cannot be dictionary keys; tuples can be. 
# Function Returns: To return multiple values from a function efficiently.
# Performance: In large-scale data processing where iteration speed and memory efficiency are critical.