# opreators what are operators : operators are used to perform mathematical comparision and many more operations in python 

# types of operators in python :
# 1. airthmeitc operators,
# 2. comparsion operators
# 3. logical operators
# 4. assignment operators
# 5. membership operators
# 6. identify operators we will look into this one -by - one 



# 1. airthmeitc operators are used to perform mathematical operations in python operators : +, -, *, /, **, //, % and etc. are airthmatic operators. 

a = 45
b = 7

print(a + b) 
print(a - b)
print(a * b)
print(a / b)
print(a // b) # this is floor division operator, it means : it returns a round of value of a division in this  case output : 7. 
print(a % b) # it is a modules operator it returns a remainder of a and b in this case output : 3.
print(a ** b) # this is exponenets operator.

# rules of modules operator : if a>b a%b = remainder, if a<b a%b = a, if -a%b = a%b, if a%-b = -a%b, if -a%-b = -a%b that' the rule of modules operator. 


# 2. comparsion operators are used to compare things such as : comparsion between two variables and many more it's return value in boolean operators : ==, <=, >=, != and etc.

a = 78
b = 67

print(a == b) # output : false
print(a >= b) # output : true
print(a <= b) # output : false
print(a != b) # output : true



# 3 assignment operators it is used to assign a value to the variable  , modify, and update a value to the variable. operators are : =, +=, -=, *=, /= and etc. 

a = 67
print(a) # output : 67
a += 3
print(a) # output : 70
a *= 5
print(a) # output : 350
a -= 54
print(a) # output : 296
a /= 3
print(a) # output : 98.6666


# 4 logical operators are used to check and combine multiple conditions it is mostly used for if and elif to evaluate and combine the multiple conditions,  operators are : and, or, not. it's return value in boolean. 


a = 56
b = 78

print(a>=50 and b<=50) # output : false
print(a>=50 or b<=50) # output : true
print(not(a>=50)) # output : false. 

# and operator : if both conditions are true then it is true otherwise false
# or operator : if any one conditions is true then it is true otherwise if both are false than it is false.
# not operator : it inverts true to false and false to true. 


# 5 membership operator : it is used to find elements in iterables like (list, tuple, string, sets and etc.) if element in iterables then it's true otherwise it's return false. operator : 'in' and 'not in'

li = [1, "saurya", 23.8, "saumya", "sagar", 3000]

print(3000 in li) # output : true
print(23 in li) # output : false
print(23  not in li) # output : true

# not in operator : if  element is not there than it's return true otherwise it's return false. this operator not in operator. 


# 6 identity operator is used to compare two objects(variables) memory location if both variable have same memory location than it's return true otherwise false operator : 'is', 'is not' it's return value is in boolean. 

a = 10
b = 10
c = 12
print(a is b) # output : true
print(a is not c) # output : true
print(b is c) # output : false

# is not operator :  it's return true if a and b is not same otherwise it's return false.  

















