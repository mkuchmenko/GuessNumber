import random


print("Hello!👋 The goal of the game is to guess a number from 1 to 50, to start, type 1:")
tries=0
while True:
    answer = int(input())
    if answer==1:
        print("Type your guess:")

        my_number=random.randint(1,50)


        while True:
            tries += 1
            user_input = input()
            if user_input.isdigit():
                user_input=int(user_input)
                if user_input>my_number and user_input<50 and user_input>1:
                    print("My number is smaller!")

                elif user_input<my_number and user_input<50 and user_input>1:
                    print("My number is bigger!")
                elif user_input>50 or user_input<1:
                    print("Type a number from 1 to 50")
                else:
                    print("You won! Your tries this round:",tries,"\nTo restart, type 1. To exit, type any number.")
                    tries=0
                break
            else:  print("Type a number from 1 to 50")
    else: break