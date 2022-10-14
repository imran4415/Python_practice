# ----------------------------1----------------------------
'''
name = input("Enter name: ")
print("Good after noon! ",name)
'''
# ----------------------------2-----------------------
'''
letter = "Dear Imran, \n\tThis python course is nice. \n\t\t\tThanks!"
print(letter)
'''
# --------------------------------3------------------------------
'''
str = "I am here to  learn  the python programming."

doubleSpaces = str.find("  ") # other method to do this and then print doubleSpaces

print(str.find("  "))
print(str.replace("  "," "))
'''
# ---------------------------------4---------------------------------------

letter = '''Dear <|NAME|>,
You are selected!
        Date:     <|DATE|>
'''
name = input("Enter name: ")
date = input("Enter date: ")

letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)
print(letter)