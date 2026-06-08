# Range function:
# Syntax: range(start, stop, step)

for i in range(0, 101, 5):
    print(i, end=" ")


n = int(input("\nEnter a number: "))
for i in range(n, (n * 10) +1, n):
    print(i, end = " ")


print("\n")


a = "Students"
for i in a:
    print(i, end = " ")

print("\n")

for i in range(len(a)):
    print(f"{i}: {a[i]}")

print("\n")



# Break:
for i in range(10):
    print(i)
    if i == 5:
        break


print("\n")


# Continue:
for i in range(10):
    if i == 5:
        continue
    print(i)


print("\n")


# Pass:
for i in range(10):
    pass
print("Done")


print("\n")


# Else:
for i in range(10):
    if i == 40:
        break
else:
    print("No break was encountered")




# Print "Hello World" 3 times:
for i in range(4):
    print("Hello World", end = " ")



print("\n")



# Print numbers from 1 to n:
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    print(i, end = " ")



print("\n")


# Reverse for loop, print n to 1:
n = int(input("Enter a number: "))
for i in range(n, 0, -1):
    print(i, end = " ")