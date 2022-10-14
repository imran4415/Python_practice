# Problem 1
'''
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
num4 = int(input("Enter number 4: "))

if num1>num2:
    f1 = num1

else:
    f1 = num2

if num3>num4:
    f2 = num3

else:
    f2 = num4

if f1>f2:
    print(str(f1)+ " is greatest")
else:
    print(str(f2) + " is greatest")
'''



# Problem 2
'''
sub1 = int(input("Enter marks of subject 1: "))
sub2 = int(input("Enter marks of subject 2: "))
sub3 = int(input("Enter marks of subject 3: "))

subtotal = sub1+sub2+sub3
percentage = subtotal/3

if percentage>33:
    print("pass\nThe total percentage is",str(percentage),"%")

else:
    print("Fail\nThe total percentage is",str(percentage),"%")
    
'''


#  Problem 3

'''
comment = input("Enter Comment: ")

if ("make a lot of money" in comment):
    print("It's a spam")
elif ("buy now" in comment):
    print("It's a spam")
elif ("subscribe this" in comment):
    print("It's a spam")
elif ("click this" in comment):
    print("It's a spam")
else:
    print("It's not a spam")
'''


# Problem 4

'''
username = input("Enter username: ")
a = len(username)
if a<10:
    print("username contains less than 10 characters")

else:
    print("username does not contains less than 10 characters")
'''

# Problem 5
'''
name_list = ["imran", "azeem", "swapneil", "shahbaz", "sunny"]
name = input("Enter name to check your invitation: ")

if name in name_list:
    print(name + " is invited")

else:
    print("Sorry! You are not invited")
'''

# Problem 6

'''
marks = int(input("Enter Your Marks: "))

if marks>90:
    print("Your grade is 'Excellent'")
elif marks>80 and marks<90:
    print("Your grade is 'A'")
elif marks>70 and marks<80:
    print("Your grade is 'B'")
elif marks>60 and marks<70:
    print("Your grade is 'C'")
elif marks>=50 and marks<60:
    print("Your grade is 'D'")
elif marks<50:
    print("You are Fail")

'''


# Problem 7
'''
post = "the post can be anything or about anything, i am just typing this to check my result after the code made by me, although i am learning from Harry."

if "Harry" in post:
    print("Yes, post is talking about Harry")
else:
    print("Post is not talking about Harry")

'''