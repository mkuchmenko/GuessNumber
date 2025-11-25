import random



print("Hello!👋 The goal of the game is to guess a number from 1 to 50, to start, type 1:")

while True:
    answer = int(input())
    if answer==1:
        print("Type your guess:")

        my_number=random.randint(1,50)


        while True:

            user_input = int(input())
            if user_input>my_number:
                print("My number is smaller!")

            elif user_input<my_number:
                print("My number is bigger!")

            else:
                print("You won! 🎉🎉 To restart, type 1. To exit, type anything")
                break
    else: break