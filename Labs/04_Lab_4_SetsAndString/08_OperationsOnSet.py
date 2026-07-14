#     8. Take two sets and apply various set operations on them :
# S1 = {1, 2, 3, 4}
# S2 = {5, 4, 3}

S1 = {1, 2, 3, 4}
S2 = {5, 4, 3}

# uinon
unionSet = S1 | S2
print(unionSet)

# intersection
intersectionSet = S1 & S2
print(intersectionSet)

# not common elements
notCommon = S1 ^ S2
print(notCommon)

# elements in S1 but not in S2
ans = S1 - S2
print(ans)

# elements in S2 but not in S1
ans = S2 - S1
print(ans)