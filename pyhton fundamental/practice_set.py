# questin : 1 write a program to print this : hello, world! welcome to python

print("hello, world! welcome to python")

# question : 2 wap(write a program) that prints the following poem using a single print() statement, following program is : multilne twinkle twinkle poem?

print('''twinkle twinkle little star
how i wonder what you are''') 

# question : 3 create variables to  store : name, age, height, a boolean value representing whether you are a student print all of them in one line. 

name = "saurya shukla"
age = 19
height = 6.2
student = True
not_student = False

print(f"name is : {name} ,and age is : {age} years old, and height is : {height} feet , and you are a student? : {student}")


# question 4 : typecasting practice you are a given string num = "45" convert it into an integer and add 10 to it. print the result. 

num = "45"
num = int(num)
print(num + 10)

# question 5 : taking user input : wap that : 1. ask the user for there favourit food 2. prints the user input with : wow! i like <food>. 

# food = input("enter your favourit food : ")
# print(f"wow! i also like : {food}")


# question 6 : simple calculater write a program that: 1. takes  two numbers as input from the user. 2. print their sum, difference, product and quotient. 

# a = int(input("enter a first number : "))
# b = int(input("enter a second number : "))

# print(f"sum of {a} + {b} = {a+b}")
# print(f"difference of {a} - {b} = {a-b}")
# print(f"product of {a} x {b} = {a*b}")
# print(f"division of {a} / {b} = {a/b}")


# question 7 : escape sequences : print the following output using escape sequences: harry said, "python is awesome"
# this is on a new line.
# this is a tab ->   <- here

text = "harry said, \"python is awesome\"\nthis is on a new line\nthis is tab ->\t<- here"

print(text)

# question 8 : operator challenge : write a program: 1. takes an int as input from the user. 2. prints the square and cube of that number. 

number = int(input("enter a number : "))

print(f"square of a {number} is : {number * number}")
print(f"cube of a {number} is : {number * number * number}")








