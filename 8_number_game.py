import random
rand = random.randint(1, 100)
tries = 10

while tries != 0:
    num = int(input("Enter the number you are thinking: "))
    if num > rand:
        print("The number you guessed is greater than the actual number, try lower!")
        tries -= 1
    elif num < rand:
        print("The number you guessed is smaller than the actual number, try higher!")
        tries -= 1
    else:
        print("Congratulations! You guessed the number")
        break

if tries == 0:
    print(f"You ran out of tries. The number was {rand}")
