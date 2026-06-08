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



# Continue:
for i in range(10):
    if i == 5:
        continue
    print(i)




# Pass:
for i in range(10):
    pass
print("Done")
