# first of all we talk about comments what are comments : comments is nothing but it is something that programmer doesn't want to execute with the program such as this i am writing i want this this line doesn't execute with the program so i am writing this line using pound (#) symbol is a comment so i am writing this line into comments. 

# there are two types of comments first is : 
# 1. single line comment using #
# 2. multiline line comments using  ("""""") triple double quotes or ('''''') triple single quotes we will look this comments one - by - one. 


a = "saurya" # this is single line comment using pound(#) symbol. 
print(a)

''' this is 
multiline comments 
as you can see i can write comments in multiline. 

'''

# escape sequence charcter 

# sequence after a backslach is called escape sequence charcter it is used to add a special charcter on your string or it is used to format a string with new line and tab and etc. 

# there are several escape sequence  charcter : 
# 1. \n to add a new line in a string.
# 2. \t to add a new tab
# 3. \\ to add a backslash
# 4. \" to display double quotes or a single quotes. 

# let's have some example :

a = "hello this is a string about me\ni am a saurya shukla\tand i am going to present you\\something like big like a \'GAME\'"

print(a) # i formatted my string as i want using escape sequence charcter. 


# some properties of print statement. 

# print statement by default add a new line at the end and if you want to print doesn't add new line add something else so you can custmize print statement ending using (end="") this it does not add new line if you using like this but if you want to add something write in quotes. 

# (sep = "") usr this when you want to add something at end of a seperation in a single print statement.  

# some examples of print statement using end = "" and sep = "" :->

print("hello world", "hello saurya" , 56, True) # output : hello world hello saurya 56 True you can see the ouput there is nothing else no , and nothing between data if you using sep="" you can add , at every seperation of the data. 



print("hello world", "hello saurya" , 56, True,  sep= " , ") # output : hello world , hello saurya , 56 , True sep= " , " add , + space at every seperation this will sepeate data with the , in this case. 


# using end="" 

print("hello my name is saurya shukla", end= " ") # if you let quotes blank it's add nothing no new line nothing 
print("i am from rewa madhya predesh", end= " ---- ") # this adds ---- at the ending 
print("i am a student persuing b.tech from r.i.t in c.s.e") # this is end  = ""

# output : hello my name is saurya shukla i am from rewa madhya predesh ---- i am a student persuing b.tech from r.i.t in c.s.e










