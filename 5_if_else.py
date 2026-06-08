age = int(input("Enter your age: "))

# If - else
if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")


# If - elif - else ladder
if age > 18:
    print("You are adult")
elif age >=13:
    print("You are teenager")
else:
    print("You are child")




# Accept two numbers and print the greatest between them
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num1 < num2:
    print(f"{num2} is greater than {num1}")
else:
    print(f"{num1} is equal to {num2}")




# Accept gender from user and print a greeting message:
gender = input("Enter your gender(M/F): ")

if gender == 'M':
    print("Good morning Sir")
elif gender == 'F':
    print("Good morning Ma'am")
else:
    print("Invalid input")




# Accept an integer and check if it is even or odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")




# Accept a year and check if it is a leap year:
year = int(input("Enter an year: "))
if year % 4 == 0:
    print("Year is a leap year")
else:
    print("Year is not a leap year")