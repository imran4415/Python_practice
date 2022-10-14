# Problem 1
'''
def greatNum(num1,num2,num3):
    if num1>num2:
        if num1>num3:
            return num1
        else:
            return num3
    else:
        if num2 > num3:
            return num2
        else:
            return num3


a = greatNum(22,11,9)
print(a)
'''


# Problem 2
'''
def conTemp(cel):
    return cel*1.8+32

a = conTemp(5)
print(a)
'''

# Problem 3
'''
print("Hello", end="")
print("How are you?", end="")
print("Checked", end="")
'''


# Problem 4
'''
def sumOfNumber(n):
    return n*(n+1)/2

a = sumOfNumber(10)

print(a)
'''

# Problem 5
'''
n = 3
for i in range(n):
    print("*"*(n-i))
'''


# Problem 6
'''
def convert_in_to_cm(inn):
    return inn*2.54

a = convert_in_to_cm(2)
print(a)
'''

# Problem 7


'''
a = "               I am not learning Python        "

def remove_word_and_split(str,word):
    newstr = str.replace(word, "")
    return newstr.strip()

b = remove_word_and_split(a,"not")

print(b)
'''

# Problem 8
'''
def table(n):
    for i in range(1,11):
        print(str(n), "X", str(i), "=", str(n*i))
        i = i+1



a = table(5)

'''