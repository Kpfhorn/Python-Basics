#Python Basics

#The '#' character is used to start a line comment

#Python is whitespace-dependent, that is to say, the Python language depends on spaces and tabs to understand how items are separated and what structure each statement belongs to.

##print statements & strings
###functions are independent units of code that perform a specific task. functions are called by typing the function name followed by parentheses. Some functions require external data to perform their task. this data is referred to as arguments. functions can have any number of arguments, even 0. for example, the print function has the task of printing data to the console, as shown below.
print("hello world")

#it is common to start learning a new language by learning how to print 'hello world' to the console.

##variables and data types
### a variable is a label attached to some data. this data can be a variety of types, as seen below

#integer
n = 10
#float
d = 432.45
#String
s = "this is a string"
s2 = 'this is also a string'

#list
l = ["this", "is", "a", "list"]

##using variables
message = "hello world"
print(message)

##getting input from the console 
input1 = input("Enter some text: ")
print(input1)

##type conversion
###Data entered from the console is stored as a String by default. if we want to use it for computation, we must first convert it to the appropriate data type
num = input("Enter a number: ")
print("you entered " + num)
#print(10 - num) #will not run. why?
print(10 - int(num))

#Loops

##While Loops
#Here we implement a counter that counts up to a number entered in the console
num = int(input("Enter a whole number: "))
print("counting to " + str(num))
i = 0
while(i <= num):
  print(i)
  i += 1

##For Loops
#This is the same counter, implemented as a for loop
num = int(input("Enter a whole number: "))
print("counting down from " + str(num))
for i in range(num+1):
  print(i)

#Conditional Statements

##if statements
num = int(input("Enter a whole number: "))
if(num > 20):
  print(str(num) + " is greater than 20")

##else statements
num = int(input("Enter a whole number: "))
if(num > 20):
  print(str(num) + " is greater than 20")
else:
  print(str(num) + " is less than 20")

##elif statements
###elif is a combination of else and if
num = int(input("Enter a whole number: "))
if(num > 20):
  print(str(num) + " is greater than 20")
elif(num > 10):
  print(str(num) + " is greater than 10 but less than 20")
else:
  print(str(num) + " is less than 10")


#combining conditional statements and loops
###This code will check if 5 numbers using the above if structure

for i in range(5):
  num = int(input("Enter a whole number: "))
  if(num > 20):
    print(str(num) + " is greater than 20")
  elif(num > 10):
    print(str(num) + " is greater than 10 but less than 20")
  else:
    print(str(num) + " is less than 10")

#Writing your own functions
def times2(number):
  return number*2;

num = int(input("Enter a whole number: "))
num2 = times2(num)
print(num2)


#List access and iteration

l = ["this", "is", "a", "list"]


print(l[2])
#note that accessing location 2 returns the 3rd item. why?

for i in l:
  print(i)



#Modifying Python Strings
###Strings in Python are immutable. this means that they cannot be modified once created. To alter strings, you must assemble a new string using data from the old string

message = 'hello world'
string_list = message.split("")
string_list[4] = ''
message2 = "".join(string_list)
print(message)
print(message2)