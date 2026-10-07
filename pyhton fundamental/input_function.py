# here we are talking about what is input() and what it can do so input() is a built in function it is used to taking input from a user it is like input() function paused a program for a sec and give chance to the user to type something when user complete the typing then program is runinning again in simple form it is used to taking input from a user.  let's have a some example :->

name = input("enter your name : ") # this is a syntax of input function it's return a value as a string. 
print(name) # name is a string data type in this case. 

a = input("enter a number : ") # if you enter a number or any data type value it is always stored as a string. 
print(a)

# this program is a great exammple of how input() has a string return value and in this example you can see that if you concatenate string and int using "+" operator so this program will throw an value error because you cannot concatenate str and int so that's it. 

# a = input("enter a number : ") # if you enter a number or any data type value it is always stored as a string. 
# print(a+4)

# so you can perform mathematical operation in a user input using type conversion you can convert input() in any type you want using type conversion and perfom operations on you user input.

# in this case we convert input into int and perform mathematical operations. 

a = int(input("enter a first number : "))
b = int(input("enter a second number : "))
print(a+b)
