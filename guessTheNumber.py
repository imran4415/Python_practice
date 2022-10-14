import random

num = random.randint(1,100)

userguess = None
guesses = 0

while userguess != num:
    userguess = int(input("Enter number: "))
    guesses +=1
    if userguess == num:
        print(f"You guessed number {num} as right number")
    else:
        if userguess>num:
            print("Please choose smaller number")
        else:
            print("Please choose larger number")

print(f"You guessed the right number in {guesses} times")