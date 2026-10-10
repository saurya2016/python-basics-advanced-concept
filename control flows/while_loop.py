# concept of while loop : it is also used to reapet set of instructions like for while loop mechanism is different from for loop : code inside the while loop keeps getting executed if the condition is true if condition becomes falls program exict from loop (loop is completed) in this while loop two processes reapet again and again first is increment and second is condition check until the condition becomes falls. 

# where for loop is sufficient and where while loop is sufficient : 

# for loop: Use when you know in advance how many times the loop should run (e.g., repeating a fixed number of times or iterating through a list/array).

# while loop: Use when you do not know the exact number of iterations and want the loop to run based on a condition (e.g., keeping a process active until a user clicks 'quit'). thats all about while loop. 

# examples of while loop :
 

# wap to print the 500 numbers one by one. 

i = 1
while(i<=500):
    print(i)
    i += 1

# write a program to print string elements one by one on a perticular point 

i = input("enter something : ")
n = 0

while n < len(i):
    print(i[n])
    n += 1


# that's all about while loop we will look it's usage further.  