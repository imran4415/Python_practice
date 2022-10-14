# Problem 1

'''
number = int(input("Enter table number: "))
for i in range(1,11):
    print(str(number) "X", str(i), "=", str(number*i))
    i = i+1
'''


# Problem 2
'''
l1 = ["Rahul", "Harry","Sohan", "Sachijjjjjn", "sahil"]

for name in l1:
    if name.startswith("S"):
        print("Welcome "+name)

    if name.startswith("s"):
        print("Welcome "+name)
'''



# Problem 3
'''
number = int(input("Enter table number: "))
i = 1
while i<11:
    print(str(number), "X", str(i), "=", str(number*i))
    i = i+1

'''


# Problem 4
'''
num = int(input("enter number: "))

prime = True
 for i in range(2,num):  #For getting prime number ,here division should calculate till the number, which we are checking for, ex- num - 11 check till '11%10==0' 
    if(num%i==0):
        prime = False
        break

if prime:
    print("This is prime number")
else:
    print("This is not prime")
'''

# Problem 5

'''
#  Note: This is copied from internet

# Sum of natural numbers up to num

num = 20

if num < 0:
   print("Enter a positive number")
else:
   sum = 0
   # use while loop to iterate until zero
   while(num > 0):
       sum += num
       num -= 1
   print("The sum is", sum)
'''



# Problem 6

'''
num = int(input("Enter number for factorial: "))
factorial = 1
for i in range(1,num+1):
    factorial = factorial * i
print(factorial)
'''

# Problem 7

'''
num = 3
for i in range(3):
    print(" " * (num-i-1), end="")
    print("*" * (2*i+1),end="")
    print(" " * (num - i - 1))
'''

# Problem 8
'''
num = 3
for i in range(num+1):
    print("*"*i)

'''

# Problem 9
'''
n = 5
for i in range(1):
    for i in range(n):
        for j in range(n):
            if i ==0 or i ==n-1 or j ==0 or j==n-1:
                print("*",end="")
            else:
                print(" ",end="")
        print("")
        
        
'''

# Problem 10
# Copied from internet
'''
num=int(input("Enter the number: "))
for table in range(1,11):
    i=11-table
    print(f"{num}X{i}={num*i}")
    
'''

# Extra code for Matrix transpose
'''
A = [[5,7,9],
     [2,8,4],
     [4,6,1],
     [3,0,2]]

transResullt = [[0,0,0,0],
                [0,0,0,0],
                [0,0,0,0]]

for a in range(len(A)):
    for b in range(len(A[0])):
        transResullt[b][a]=A[a][b]

print("The transpose of matrix is: ")
for rrr in transResullt:
    print(rrr)
'''