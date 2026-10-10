# concept of break continue and pass we will lock into this one - by - one 

# break : break statement breaks the loop it instruct the program to exict the loop now. means it breaks the loop before the loop completed.
#  
# continue : continue statement instruct the program to skip perticular iteration means continue skip perticular value you doesn't want to execute. 

# pass : pass is the placeholder that does nothing it instructs the program to do nothing. means nothing.

# we will look these concepts in the examples :

# for break : 

for i in range(1, 50):
    if i == 5:
        break # this will break loop at 5  output will be : 1, 2, 3, 4
    print(i)

# for continue :


for i in range(1, 50):
    if i == 5:
        continue # this will skip value 5  output will be : 1, 2, 3, 4, 6,........,50
    print(i)


# for pass : 

for i in range(1, 10):
    pass # this statement did nothing it means nothing happenes in this loop if you don't use this this will be throw an error. 


# for with else statement : as a optional statement you use else with for loop, else will be executed if the loop is completed otherewise if the loop is break else doesn't executed it is also worked with while loop as well let's understand with examples :->

li = [1, 2, 3]

for i in li:
    print(i)

else:
    print("loop is completed")

i = 0

while i <= 2:
    print(i)
    i += 1

else:
    print("loop is completed")

# that's all about these concepts. 
