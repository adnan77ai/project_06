print("Welcome to Guess the Number.")
print()
print("Guess a number between 1 and 10 and I will tell you if you are too low, too high, or get it correct.")
print()
print("Let's play!")

import random
count = 0
my_num = random.randint(1, 10)
while True:
    guess = int(input("pick a random number: "))
    if guess > my_num:
        print("Too high, try agin...")
        count += 1
    elif guess < my_num:
        print("Too low, try again...")
        count += 1
    elif guess == my_num:
        print("You are a winner! 🥳🥳")
        break
    else:
        print("That is not a number I recognize.")
print("It took you", count, "attempt(s) to get the correct answer.")
