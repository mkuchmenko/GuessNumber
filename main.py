import random


print("Hello! The goal of the game is to guess a number from 1 to 50, to start, type your first assumption:")

my_number=random.randint(1,50)

user_input=int(input())

while user_input!=my_number:
    if user_input>my_number:
        print("My number is smaller!")
        user_input = int(input())
    elif user_input<my_number:
        print("My number is bigger!")
        user_input = int(input())

print("You won!")