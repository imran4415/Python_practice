import random

def game_snake(comp, user):
    if comp == user:
        return None
    elif comp == "Snake":
        if user == "Water":
            return False
        elif user == "Gun":
            return True

    if comp == "Water":
        if user == "Gun":
            return False
        elif user == "Snake":
            return True

    if comp == "Gun":
        if user == "Snake":
            return False
        elif user == "Water":
            return True

print("Computer Turn : Snake or Water or Gun")

randNo = random.randint(1,3)

if randNo == 1:
    comp = "Snake"
elif randNo == 2:
    comp = "Water"
elif randNo == 3:
    comp = "Gun"

player = input("Your Turn : Snake or Water or Gun : ")
user = player.capitalize()
a = game_snake(comp, user)

print(f" Computer chose {comp}")
print(f" You chose {user}")

if a == None:
    print("The game is tie")
elif a == True:
    print("You Won")
else:
    print("Computer Won")