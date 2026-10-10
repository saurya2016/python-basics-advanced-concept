# concept of conditionals in python :-> we must be able to execute a set of instructions on a condition being met that is conditional expression for us to understand it i have a examples for you :->
# 1. we play cricket if the day is sunday
# 2. we play video games if our work is complete if else is a basic logic building program. 

# example : 1 create a program that print even if the number is even otherwise print odd. 

# x = int(input("enter a number(only whole number) : "))

# if x % 2 == 0: 
#     print("even")
# else:
#     print("odd")

# print("program is completed")

# if statement : -> code inside in if statement is executed when the condition of if is true that is if statement for you. 
# # else statement : -> block code of else is to be executed when all the conditions are false. 

# example : 2 write a program that return a grade on the basis of given marks by the student we can see here how we use else if : ->

marks = float(input("enter your marks in percentage : ")) 

if marks < 0 or marks > 100:
    raise ValueError("percentage cannot be negative or cannot be a over hundred")

elif marks > 90 and marks < 100 :
    print("GRADE : A+")

elif marks > 80 and marks < 90 :
    print("GRADE : A")

elif marks > 70 and marks < 80 :
    print("GRADE : B")

elif marks > 60 and marks < 70 :
    print("GRADE : B-")

elif marks > 50 and marks < 60 :
    print("GRADE : C")

elif marks > 40 and marks < 50 :
    print("GRADE : D")

else:
    print("YOU ARE FAILED")


# this program print a grade according to their marks we ca see here there is multiple elif statements between if and else that is a work of elif.
# elif statement :-> we use elif statement if we execute a set of instruction in a multiple condition or it is a multiway decision taken by our due to a certain condition that is elif for you. 


# logical and comparsion operator 


# comparsion operator :->  we use comparsion to evaluate conditions on a if and elif statement. 
# logical operator : -> logical opeator is used evaluate and combine multiple decisions. 

# properties of if and elif and else : 

# 1. we can use if independently
# 2. there can be any number of elif statement between if and else. 
# 3. elif and else can not be used independently. 



