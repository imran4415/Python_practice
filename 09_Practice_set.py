# Problem 1
'''
with open("poem.txt") as f:
    a = f.read()

findWord = input("Enter word to find :")

if findWord in a:
    print(f"Yes! {findWord} exists in file.")
else:
    print(f"No! {findWord} does not exist in file.")
'''



# Problem 2


'''
# def game_score(score):
#     return score
score = 80

with open("high_score.txt","r") as f:
    a = f.read()

if a == "":
    with open("high_score.txt","w") as f:
        f.write(str(score))

    print("Congratulations! You made a new high score!")

elif int(a) < score:
    with open("high_score.txt","w") as f:
        f.write(str(score))
    print("Congratulations! You made a new high score!")

elif int(a) > score:
    with open("high_score.txt","a") as f:
        if len(a) > 0:
            f.write("\n")
        f.write(str(score))
    print("You need to play again to beat your own high score!")
    
'''


# Problem 3

'''
for i in range(2,21):
    with open(f"tables/multiplication table of {i}.txt", "w")as f:
        for j in range(1,11):
            f.write(f"{i}X{j}= {i*j}\n")
    
'''

# Problem 4
'''
with open("new_file_pr04.txt")as f:
    data = f.read()

data = data.replace("Donkey", "@#$!@&*%$")

with open("new_file_pr04.txt", "w")as f:
    data = f.write(data)
'''

# Problem 5
'''
list1 = ["donkey", "monkey", "dumb", "stupid"]

with open("new_file_pr04.txt") as f:
    content = f.read()

for word in list1:
    content = content.replace(word, "@#$!@&*%$")
    with open("new_file_pr04.txt", "w") as f:
        f.write(content)
'''

#  Problem 6
'''
with open("log.txt") as f:
    content = f.read()

if 'python' in content.lower():
    print("Yes python is present")
else:
    print("No python is not present")
'''

#  Problem 10
'''
with open("newfile.txt","w") as f:
    f.write("")
'''

# Problem 8
'''
newfile = "copyfile.txt"

with open("this.txt")as f:
    content = f.read()

with open(newfile, "w")as f:
    f.write(content)
'''

# Problem 10
'''
file1 = "this.txt"
file2 = "copyfile.txt"

with open(file1) as f:
    f1 = f.read()
with open(file2) as f:
    f2 = f.read()

if f1 == f2:
    print("The file is identical")
else:
    print("File does not matches.")
'''

# Problem 11
'''
import os
oldname = "renamefile.txt"
rename = "renamed_by_python.txt"

with open("renamefile.txt") as f:
    content = f.read()

with open(rename, "w")as f:
    f.write(content)

os.remove(oldname)

'''