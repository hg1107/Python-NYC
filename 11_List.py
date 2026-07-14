'''

Collection of multiple data types
list = []
Ordered
Indexed
Mutable
Duplications allowed

'''


list = [1, 'Hello', True, 2.5]
# Complete list
print(list)
print("\n")

# Indexing
print(list[1])
print("\n")

# Mutable
list[-1] = 3.14
print(list)
print("\n")

# Traversing (loops) on lists
a = [10, 20, 30, 40, 50]

# 1. Traversing on values:
for i in a:
    print(i, end = " ")
print("\n")

# 2. Traversing on indexes
for i in range(len(a)):
    print(f"{i}: {a[i]}")
print("\n")



# List Methods:
# CRUD --> Create, Read, Update, Delete

# To get the available methods for a certain datatype:
print(dir(list))