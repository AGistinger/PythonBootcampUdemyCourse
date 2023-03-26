# Advanced Dictionaries
d = {'k1': 1, 'k2': 2}

# Dictionary Comprehension
# Create a dictionary using dictionary comprehension
print({x: x**2 for x in range(10)})

# Iteration over keys/values/items
# iter methods, returns tuples of keys/values
for k in d.items():
    print(k)

# View Methods
print(d.values())
print(d.items())
print(d.keys())
