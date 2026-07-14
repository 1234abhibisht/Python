# syntax -> newlist = [expression for_item_in_iterable if condition == True]

# key rules -> Order Matters: The for clauses are written in the same order as they would appear in nested loops (outer first, inner last). 
# Readability: If the comprehension requires more than two loops or complex logic, it is often better to use standard for loops to maintain code readability. 
# Scope: Variables defined in the outer loop (e.g., row) are accessible to the inner loop (e.g., for num in row).

# creating a list of square of odd numbers from 1 to 10
a = [i for i in range(1,11) if i % 2 != 0]
print(a)

# squares of even numbers from 0 to 9
b = [i**2 for i in range(0,10) if i % 2 == 0]
print(b)

# if else conditions in list comprehension
# newlist = [value_if_true if_condition else value_if_false for_item_in_iterable]
num = [1,2,3,4,5]
result = ["True" if i % 2 == 0 else "False" for i in num]
print(result)

# Note -> list comprehension doesn't support elif conditonal statment

# creating a 3*3 nested list
c = [[j for j in range(1,4)]for i in range(3)]
print(c)  # -> [[1,2,3],[1,2,3],[1,2,3]]

# nested loop in a list
d = [1,2,3,3,4,5]
# duplicate =
# print(duplicate)

# flatten a nested list 
e = [[1,2,3],[4,5,6]]
e_res = [j for i in e for j in i]
print(e_res)  # -> [1,2,3,4,5,6]

# adding conditions in flattering of nested list
# returning only even numbers from nested list ->
f1 = [[1,2,3], [4,5,6], [7,8,9]]
f1_res = [j for i in f1 for j in i if j % 2 == 0]
print(f1_res)  # -> [2,4,6,7]

# returning rows with sum greater than 10 from nested list 
g = [[1,2,3], [4,5,6], [7,8,9]]
g_res1 = [i for i in g if sum(i) > 10]
print(g_res1)  # -> [[4,5,6], [7,8,9]]
# returning rows with sum greater than 10 from nested list and doing flattering of those rows
g_res2 = [j for i in g if sum(i) > 10 for j in i]
print(g_res2) # -> [4,5,6,7,8,9]