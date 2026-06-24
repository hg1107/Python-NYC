# Reusable block of code

def hello():
    print("Hello World")

hello()
hello()


print("\n")


a = 123
def reverse(n):
    rev = 0
    while n > 0:
        rev = rev * 10 + n%10
        n = n // 10
    return rev

print(reverse(a))
print(reverse(456))


print("\n")


def addition(a, b):
    return a + b

print(addition(2, 3))
print(addition(123, 456))


print("\n")


# Types of arguments

# 1. Positional
def multiply(a, b, c, d):
    print(a * b * c * d)

# multiply(1, 2, 3)   -->  Will give error
multiply(1, 2, 3, 4)


print("\n")


# 2. default
def addition(a, b, c = 10):
    print(a + b + c)

addition(1, 2)
addition(1, 2, 3)


print("\n")


# 3. Keyword
def subtraction(a, b):
    print(b - a)

subtraction(b = 30, a = 10)