# Advanced Sets
# Does not allow duplicate items
s = set()

# Add
s.add(1)
s.add(2)
print(s)

# Clear - remove all elements from set
s.clear()
print(s)

# Copy - returns a copy of the set
# Changes to the original will not affect the copy
s = {1, 2, 3}
sc = s.copy()
print(sc)

# Difference - returns the difference of two or more sets
s.add(4)
s.difference(sc)

# Difference update - returns set 1 after removing elements from set 2
s.difference_update(sc)
print(s)

# Discard - removes an element from the set if its a member
s = {1, 2, 3, 4}
s.discard(2)
print(s)

# Intersection - returns the intersection of 2 or more sets as a new set
# an intersection is the elements that are common to all the sets
s1 = {1, 2, 3}
s2 = {1, 2, 4}
print(s1.intersection(s2))

# Intersection_update - will update a set with the intersection of itself and another
s1.intersection_update(s2)
print(s1)

# isdisjoint() - returns true if there is a null intersection
s1 = {1, 2}
s2 = {1, 2, 4}
s3 = {5}
print(s1.isdisjoint(s2))
print(s1.isdisjoint(s3))

# issubset() - returns whether one set contains another set
print(s1.issubset(s2))

# issuperset() - returns whether the set contains another set
print(s2.issuperset(s1))
print(s1.issuperset(s2))

# symmetric_difference() - returns the symmetric difference of the two sets
# All the elements that are exactly in one of the sets (opposite of intersection)
print(s1.symmetric_difference(s2))

# symmetric_difference_update() - updates the first set with the symmetric
# difference of the two sets
s1.symmetric_difference_update(s2)
print(s1)

# Union - returns a union of two sets
print(s1.union(s2))

# Update - updates a set with the union of itself and others
s1.update(s2)
print(s1)
