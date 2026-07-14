# '-' is alternative operator for .difference method
# Note -> returns a new set
a1 = {5,4,3}
a2 = {1,2,3}
print(a1 - a2)

# '-=' is alternative operator for .difference_update method
# Note -> do not return new set, modifies original set
b1 = {5,4,3}
b2 = {1,2,3}
b1 -= b2  # modifies b1 and inserts difference of b1-b2 to it
print(b1)

# '^' is alternative operator for .symmetric_difference method
# Note -> returns a new set
c1 = {5,4,3}
c2 = {1,2,3}
print(c1 ^ c2)  # -> {1,2,4,5}

# '^=' is alternative operator for .symmetric_difference_update method
# Note -> do not return new set, modifies original set
d1 = {5,4,3}
d2 = {1,2,3}
d2 ^= d1  # modifies d2 and insert symmetric difference of d1 and d2 to it
print(d2)  # -> {1,2,4,5}

# '&' is alternative operator for .intersection method
# Note -> returns a new set
e1 = {5,4,3}
e2 = {5,2,3}
print(e1 & e2)  # -> {3,5}

# '&=' is alternative operator for .intersection_update method
# Note -> do not return new set, modifies original set
f1 = {5,4,3}
f2 = {5,2,3}
f1 &= f2  # modifies f1 and insert intersection of f1 and f2 to it
print(f1)  # -> {3,5}

# '|' is alternative operator for .union method
# Note -> returns a new set
g1 = {5,4,3}
g2 = {5,2,3}
print(g1 | g2)  # -> {2,3,4,5}

# '|=' is alternative operator for .update method
# Note -> do not return new set, modifies original set
g1 = {5,4,3}
g2 = {5,2,3}
g1 |= g2  # modifies g1 and insert union of g1 and g2 to it
print(g1)  # -> {2,3,4,5}