# It works on a condition based 
'''
Syntax:

while <Condition>:
    statement(s)
    update (increment/decrement)

'''

a = 1
while a != 20:
    print(a, end = " ")
    a+= 1


print("\n")


# separate each digit of a number and print on a new line
n = int(input("Enter a number: "))

while n > 0:
    print(n % 10)
    n //= 10


print("\n")


# Accept a number and print its reverse:
num = int(input("Enter a number: "))
rev = 0

while num > 0:
    rev = rev * 10 + num % 10
    num //= 10

print("The reverse number is ", rev)