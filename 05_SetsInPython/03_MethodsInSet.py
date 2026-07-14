# .add - add element to set
# Note - elements are added in set using hash table
a = set()
a.add(1)

# .copy - copies the set

# .clear - removes all elements in a set

# .difference - returns a set containing difference between two or more specific sets
b1 = {5,4,3}
b2 = {1,2,3}
res = b1.difference(b2)  # removes elements of b2 from b1
print(res)  # -> {5,4}

# difference_update - removes element from a set that are also included in another set
# Note -> difference_update method does not return any set, it transform the original set
c1 = {"apple", "banana", "cherry"}
c2 = {"google", "microsoft", "apple"}
c1.difference_update(c2)  # modifies c1 and insert difference c1-c2 to it
print(c1)  # -> {"cherry", "banana"}, removes element from c1 that were also present in c2

# .symmetric_difference - returns a set in which common elements from two specific sets are removed
st1 = {1,2,3,4}
st2 = {1,5,3,6}
print(st1.symmetric_difference(st2))  # -> {2,4,5,6}

# symmetric_difference_update - removes elements from a set that are also present in another set
# Note -> symmetric_difference_update method does not return any set, it transform the original set
st3 = {1,2,3,4}
st4 = {1,5,3,6}
st3.symmetric_difference_update(st4)  # modifies st3 and insert symmetric difference st3-st4 to it
print(st3)  # -> {2,4,5,6}

# .intersection - returns a set which is intersection of two sets
# Note -> intersection of two sets means common element from both of the set
d1 = {1,2,3}
d2 = {1,5,3,4}
print(d1.intersection(d2))  # -> {1,3}

# intersection_update - removes element from a set that are not present in another set
# Note -> .intersection_update method does not return any set, it transform the original set
e1 = {"apple", "banana", "cherry"}
e2 = {"google", "microsoft", "apple"}
e1.intersection_update(e2)  # modifies e1 and insert intersection of e1 and e2 to it
print(e1)  # -> {"apple"}

# .union - returns a set that contains uninon of two specific sets
f1 = {1,2,3,4}
f2 = {2,3,5,6}
print(f1.union(f2))  # -> {1,2,3,4,5,6}

# .update - update the set with union of the set and another set
# Note -> .update method does not return any set, it transform the original set
st5 = {1,3,4}
st6 = {2,3,5}
st5.update(st6)  # modifies st5 and insert union of st5 and st6 to it
print(st5)  # -> {1,2,3,4,5}

# .isdisjoint - checks whether two sets are disjoint or not
# Note -> disjoint sets are two or more sets that have no elements in common
g1 = {1,2,3}
g2 = {4,5}
print(g1.isdisjoint(g2))  # -> True

# .issubset - checks whether the set is subset of a specific set
h1 = {1,2,3,4}
h2 = {1,2}
print(h2.issubset(h1))  # -> True
h3 = {1,2,3,4}
print(h3.issubset(h1))  # -> True, as a set is subset of itself

# .issuperset - checks whether the set is superset of a specific set
i1 = {1,2}
i2 = {4,1,2,5}
print(i2.issuperset(i1)) # -> True
i3 = {1,2}
print(i3.issuperset(i1))  # -> True, as each set is subset of superset of itself

# .remove - removes a specific element from a set
# Note -> .remove method gives error if element is not present in set
j = {1,2,3,4}
j.remove(2)
print(j)  # -> {1,3,4}

# .discard - removes a specific element from a set
# Note -> .discard method doesn't give error if element is not present in set, and set remains unchanged
k1 = {1,2,3,4}
k1.discard(2)
print(k1)  # -> {1,3,4}
k2 = {1,2,3,4}
k2.discard(5)
print(k2)  # -> {1,2,3,4}, as 5 is not present in set k2 so it is unchanged and no error shown

# .pop - removes random(arbitrary) element from set depends on internal hash table
# Note -> .pop method removes the arbitrary element, the element is determined by the internal order of hash table not by random number generator
#      ->  in sets of integer .pop generally removes the element in sorted order as integers hash to themselves
l1 = {2,3,1,4,5}
l1.pop()  # removes 1
print(l1)
l2 = {'a', 'b', 'c'}  # removes an arbitrary element
l2.pop()
print(l2)
# how this arbitrary number is selected to remove using .pop method :
# -> as we know how python creates a set using the hash table by using (hash(x)) to hash element and (hash(x) % hash_table_size) to determine its index in hash table
# -> so when we use .pop method, python scan whole hash table from index 0 and remove element from first occupied slot
# -> thats why elemetns are removed in sorted order in a set of integers as integers hash to themselves
# -> in case of set of strings a random string is removed in each new session of python interpretor, as python uses randomization for hash values of string for each new session