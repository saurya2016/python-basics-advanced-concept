# concepts of variable 
  
# variable is a name given to a memory location that stores data. it's like container that holds a value. we can use variables to store different types of data like numbers, strings, lists, etc. this is also called a identifire. 

a = 10 
name = "saurya"
print(a) # output will be : 10
print(name)  # output will be : saurya

# concept of data types

# before we talk about data types we understand python is a dynamically typed language which means we don't need to declare the data type of a variable while creating it. python automatically assigns the data type based on the value assigned to the variable.

# primary data types in python are:
# 1. int : used to store whole numbers (integers)
# 2. float : used to store decimal numbers (floating point numbers)
# 3. str : used to store text (strings)
# 4. bool : used to store boolean values (True or False)
# 5. none : used to represent the absence of a value or a null value  and many more like list, tuple, set, dict etc. we will discuss them in detail in upcoming lessons.

number = 789  # this is int data type <class int>
person = "raja" # this is string data type <class str>
decimal = 56.88  # this is float data type <class float>
right_or_wrong = True # this is boolean data type <class bool>
nothing = None # this is none data type <class none>

print(number, type(number))  # you have seen here a type() what is it? it is nothing but it can tell you a data  type of python it takes argument as a variable name. 
print(person, type(person))   # you have seen here a type() what is it? it is nothing but it can tell you a data  type of python.
print(decimal, type(decimal)) # you have seen here a type() what is it? it is nothing but it can tell you a data  type of python.
print(right_or_wrong, type(right_or_wrong)) # you have seen here a type() what is it? it is nothing but it can tell you a data  type of python.
print(nothing, type(nothing)) # you have seen here a type() what is it? it is nothing but it can tell you a data  type of python.

