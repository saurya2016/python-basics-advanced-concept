# concept of loops : loops is used to reapet a set of instruction like : we want to print no. from 1 to 1000 or we want to print a table of a given value in these some kind of cases we use loops. loops makes easy for a programmer to tell the computer which set of instructions is to be reapet and how. it tackle repitition means why we write same code multiple times. this is loops for you. 

# what is for loop : for loop is used to iterate through a sequence like : list, tuples, string, sets and etc it is iterate list, tuple, string and sets one by one we will see example. 
# range function : range function is used to generate a sequence of a number it takes three arguments : start,stop and stepsize : start : where to start is included, stop : where to stop is excluded and step size : how many iterations will be skip. generally we use two : start and stop.range function is used with for loop for generating a sequence of a number. 

# examples of for loops : 

# example : 1 write a program to print a table of a given number : 

# n = int(input("enter a number : "))

# for i in range(1, 11):
#     print(f"{n} x {i} = {n*i}")

# example : write a program to iterate a strings : 


# s = "saurya shukla"

# for i in s:
#     print(i) # it is iterate string element one - by - one. 


# example 3 : write a program to print each element of a list with numbring.  : 

li = [1, 2, 3, "saurya", "saumya", 67.90]
n = 0
for i in li:
    print(f"item {i} at index {n}")
    n += 1

# this is for loop this can anything the loop does. 