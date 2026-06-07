# Indexing --> Accessing the characters of a string
name = "Hardeep"
print(name)

print("First letter:", name[0])
print("Last letter:", name[-1])


# Slicing --> Accessing a range of characters in a string
# Syntax --> variable[start:stop:step]

print("Slicing:", name[3:7])
print("Using step:", name[0::2])
print("Reversed string:", name[::-1])


# Task:
task = "Hello how are you"
# how:
print(task[6:9])
# you:
print(task[14:])
# Hello:
print(task[0:5])