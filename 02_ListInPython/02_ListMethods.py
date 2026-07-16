# Note -> list methods transform original list, as lists are mutable

# .append - add element from rear of list
a1 = [1,2,3]
a1.append(4)
print(a1)  # -> [1,2,3,4]
a2 = [4,5,6]
a3 = [7,8]
a2.append(a3)
print(a2)  # -> [4,5,6,[7,8]], will create a nested list

# .clear - removes all element from list
b = [1,2,3]
b.clear()
print(b)

# .copy - returns a copy of list
c1 = [5,6,7]
c2 = c1.copy()
print(c2)

# .count - returns number of occurances of a value in a list
# Note -> returns 0 if value not found in list
d = [1,2,3,3,4,5,5]
print(d.count(3))  # -> 2
print(d.count(8))  # -> 0, as 8 is not present in list

# .extend - add elements of a list, tuple, set at the end of current list
# Note -> use .extend to add elements of a list to required list instead of append
e1 = [1,2,3]
e2 = [4,5,6]
e1.append(e2)
print(e1)  # -> [1,2,3,4,5,6]

# .index - returns index of first occurance of a value from left
# Note -> .index will give error if value not present in list
f1 = [1,2,3,2]
print(f1.index(2))  # -> 1
f2 = ['a','b','c','d','e']
print(f2.index('c',1,3))  # searches between index 1 to 3
# Note - in list there is no .rindex method, only strings have .rindex method

# Note - in list there is no .find method, only strings have .find method along with .rfind method

# .insert - inserts a value at a specific position
g1 = [1,2,3,4]
g1.insert(2,5)  # first argument is index at which value to be inserted, second argument is the value
print(g1)  # -> [1,2,5,3,4]
# Note - if we put index argument greater than the last index of list to insert value, then value will be inserted at last position
g2 = [1,2,3,4]
g2.insert(6,5)  # last index of g2 is 3, but we put argument index 6
print(g2)  # -> [1,2,3,4,5]

# .remove - removes value of its first occurence from left from a list
# Note -> give actual value as an argument to .remove method
#         .remove will give error if element not found in list
h = [1,2,3,2,4]
h.remove(2)
print(h)  # -> [1,3,2,4]

# .pop - removes a value from a specific index from a list
# Note - give index at which value want to remove as argument
#        if we give argument index greater than last index of list, it will give error
i1 = [1,2,3,2,4]
i1.pop(1)
print(i1)  # -> [1,3,2,4]
i2 = [1,2,3,4]
try : 
    i2.pop(5)
    print(i2)  # -> Error, as list l2 has maximum index 3
except : print(IndexError) 
# Note - if we use .pop method without passing any argument, it will pop last element of list 
#        but using .pop without argument in an empty list gives error, as there is no last element
i3 = [1,2,3,4]
i3.pop()
print(i3)  # -> [1,2,3]

# .reverse - reverse the order of list
j = [1,2,3,4]
j.reverse()
print(j)

# .sort - sorts the original list
# ascending order ->
k1 = [2,4,1,5,3]
k1.sort()
print(k1)  # -> [1,2,3,4,5]
# Note -> for list of strings, .sort method sorts list according to ascii value of first letter of string
#         if first character of strings are same, then sorts according to ascii value of second letter and so on
k2 = ["Ford", "BMW", "Volvo"]
k2.sort()  
print(k2)  # -> ["BMW", "Ford", "Volvo"]
k3 = ["Apple", "atom", "Ball"]
k3.sort()
print(k3)  # -> ["Apple", "Ball", "atom"], as ascii of A is 65, B is 66, a is 97
k4 = [4,2,[3,1],5]
k4[2].sort()  # only sort nested list k3[2]
print(k4)  # -> [4,2,[1,3],5]
# descending order (pass an argument reverse=True in .sort method) ->
k5 = [2,4,1,5,3]
k5.sort(reverse=True)
print(k5)
# using key parameter in .sort method
# Note - the function provided in key parameter is called exactly once for each element in list
#        and list is sorted according to the returned value in key not according to original list
#        this is helpful in sorting list in custom way, complex lists, dictionaries, case-insensitive sorting in a list
# sorting list according to length of each string ->
l1 = ["Apple", "Red", "Ball"]  
l1.sort(key=len)
print(l1)  # -> ["Red", "Ball", "Apple"]
# sorting list consist of case-insensitive strings ->
l2 = ["Apple", "atom", "Ball"]  
l2.sort(key=lambda x : x.lower())
print(l2)  # -> ["Apple", "atom", "Ball"]
# sorting list accoring of keys or values of dictionary ->
l3 = [{"name": "Alice", "grade": 88}, {"name": "Bob", "grade": 95}, {"name": "Charlie", "grade": 72}]
l3.sort(key=lambda x : x["grade"])  # list l3 will be sorted accoring to values of "grade" key
print(l3)  # -> [{'name': 'Charlie', 'grade': 72}, {'name': 'Alice', 'grade': 88}, {'name': 'Bob', 'grade': 95}]
l4 = [{"name": "Alice", "grade": 88}, {"name": "Bob", "grade": 95}, {"name": "Charlie", "grade": 72}]
l4.sort(key=lambda x : x["name"])  # list l3 will be sorted accoring to values of "name" key
print(l4)  # -> [{'name': 'Alice', 'grade': 88}, {'name': 'Bob', 'grade': 95}, {'name': 'Charlie', 'grade': 72}]
 