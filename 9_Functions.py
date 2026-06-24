# Reusable block of code

def hello():
    print("Hello World")

hello()
hello()


a = 123
def reverse(n):
    rev = 0
    while n > 0:
        rev = rev * 10 + n%10
        n = n // 10
    return rev

print(reverse(a))
print(reverse(456))


def addition(a, b):
    return a + b

print(addition(2, 3))
print(addition(123, 456))