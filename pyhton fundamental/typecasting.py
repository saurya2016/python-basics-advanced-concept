# in geneeral typecasting is the process of converting one data type into another data type. In Python, there are two types of typecasting: implicit and explicit.

# implicit typecasting is when the conversion of one data type to another is done automatically by the Python interpreter. This usually happens when we perform operations on different data types, and Python converts them to a common data type to avoid errors.

# explicit typecasting is when the conversion of one data type to another is done manually by the programmer using built-in functions like int(), float(), str(), etc.

# this is int to str conversion. 
age = 67
print(age, type(age)) # here the type of a data is <class int>
age = str(age) # here we convert data int into str data type this process is called typecasting. 
print(age, type(age)) # here data converted into a string that's all about typecasting. 

# this is str to int conversion.

n = "123456"
print(n, type(n))
n = int(n) # this is typecasting process. 
print(n, type(n))

# int to str , str to int , int to float , float to int and many more tuple to list, list to tuple and many more type conversions are there all the type conversions syntax are like this but one thing is different conversion type name such as in this case : - int(n) where int is a conversion type and n is a variable now. 

# there is just one thing you have to know : if you convert wrong data into another data type program will throw an value error for a example :- 

name = "saurya shukla"
print(name, type(name))
name = int(name)
print(name, type(name))

# in this case as you can see if you converted saurya shukla into int data type than program will throw an error because you are converting wrong data in wrong data type. 



