# AdvancedLists
l = [1, 2, 3]

# Append - add an item to a list
l.append(4)

# Count - returns how many times an element occurs in a list
print(l.count(10))
print(l.count(1))

# Extend - extends a list to the original list
x = [1, 2, 3]
x.append([4, 5])
print(x)
x = [1, 2, 3]
x.extend([4, 5])
print(x)

# Index - returns the index of the element passed in
# Will return a ValueError if you try to find the index
# of something that doesn't exist in list
print(l.index(2))

# Insert - Takes an index and element
# places object at the index supplied
l.insert(2, 'inserted')
print(l)

# Pop - pop off the last element of the list (by default)
# that element is returned
print(l.pop())
print(l)
# You can pass an index into pop to remove that index
print(l.pop(0))
print(l)

# Remove - Removes the first occurrence of a value
l.remove('inserted')
print(l)
l = [1, 2, 3, 4, 3]
l.remove(3)
print(l)

# Reverse - Will reverse the list, occurs in place
l.reverse()
print(l)

# Sort - Will sort the list, occurs in place
l.sort()
print(l)
