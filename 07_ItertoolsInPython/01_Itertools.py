# itertools is a python module that provide powerful memory efficient tools to work with iterators to make iterations more efficient
# Note -> itertools are implemented in c for performance
#         the code is written in c, its compiled into machine code and called by python functions

# Note -> itertool function returns iterator, to access this iterator we need to use iter() and next() functions or typecase the output to a list,tuple etc

# product - it is a combinatoric iterator from python itertools module that calculates cartesian product of two iterables
#           It's essentially a nested loop implemented in C for efficiency, generating all possible combinations by taking one element from each input iterable
# Note -> cartesian product of two sets A and B is the set of all ordered pairs (a, b) where a ∈ A and b ∈ B
# Note -> product returns the iterator
from itertools import product
a1 = [1,2,3]
a2 = ['a', 'b', 'c']
res1 = product(a1, a2)
print(list(res1))  # -> [(1, 'a'), (1, 'b'), (1, 'c'), (2, 'a'), (2, 'b'), (2, 'c'), (3, 'a'), (3, 'b'), (3, 'c')] -> cartesian product
# repeat parameter in product function ->
# repeat parameter allows to create cartesian product of iterable itself multiple times 
a3 = [1,2]
res2 = product(a3, repeat=2)
print(list(res2))  # -> [(1, 1), (1, 2), (2, 1), (2, 2)]
res3 = product(a3, repeat=3)
print(list(res3))  # -> [(1, 1, 1), (1, 1, 2), (1, 2, 1), (1, 2, 2), (2, 1, 1), (2, 1, 2), (2, 2, 1), (2, 2, 2)]

# permutations and combinations - these itertool creates all the arrangements of elements from an iterable
from itertools import permutations
from itertools import combinations
b1 = [1,2,3]
print(list(permutations(b1)))  # -> [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
# using r parameter in permutations function ->
# r parameter defines the length of each permutation tuple, or we can say it defines 
print(list(permutations(b1, r=2)))  # -> [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
b2 = ['A', 'B', 'B']  # iterable contains duplicates
print(list(permutations(b2)))  # -> [('A', 'B', 'B'), ('A', 'B', 'B'), ('B', 'A', 'B'), ('B', 'B', 'A'), ('B', 'A', 'B'), ('B', 'B', 'A')]
# Note -> elements of iterable are treated as unique based on their position not their value
#         If the input contains duplicates (e.g., ['A', 'B', 'B']), the output will contain duplicate tuples corresponding to the different positions of the identical values
b3 = [2,3,1]
print(list(combinations(b3, 3)))  # -> [(2, 3, 1)]
print(list(combinations(b3, 2)))  # -> [(2, 3), (2, 1), (3, 1)], as (3,2),(1,2),(1,3) are identical to output 
print(list(combinations(b3, 1)))  # -> [(2,), (3,), (1,)]

# difference between permutation and combination:
# -> both permutation and combination are the arrangements of elements of set or iterables
# -> in permutation order matters but in combination order doesn't matter
# -> in permutation (1,2,3),(2,1,3),(3,2,1) are different but in combination all three are same
# when to use permutaion or combination:
# Use Permutations if the order matters. If rearranging the selected items creates a different outcome or meaning, it is a permutation.
# Examples: Creating a password, ranking runners in a race (1st, 2nd, 3rd), assigning specific roles (President, VP, Secretary), or arranging books on a shelf.
# Logic: The sequence A-B-C is distinct from C-B-A
# Use Combinations if the order does not matter. If the group remains the same regardless of the sequence in which items were picked, it is a combination.
# Examples: Selecting a team of players, choosing toppings for a pizza, picking lottery numbers, or selecting committee members without specific titles.
# Logic: The group {A, B, C} is identical to {C, B, A}