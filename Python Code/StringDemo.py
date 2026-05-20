'''
name ="virat " *10
print(name)

print ('virat\\\'s '  'hello');

'''

# declared constant we can change because  constant does  not support in python
NAME ='Python is programming language'

# slicing in python  by using indexing 
# staring point =0, last index = 4 ( but 4-1=3  due to index ), skip iterarion = 2
# print(NAME[0:4:2])

# print(NAME[-2:-1])
#  For reverse Slicing 
# print(NAME[-5:-7 :-1])

#   Point to remener we cannot go reverse  by default it will moves from  left to right 
#  but if we want to  then we can use  skip iteration like we use at line number 18 which is -1 at the end

#  we can change the value of an variable but we cannot change the  existing string

sentence = "Python is use for coding purpose";
#  we cannot change the existing string 
#  if we do this we will welcome by TypeError -> String object does not support item assignment
# sentence[0:3] ='Hel';

sentence ="hello"
#  Reassignment is possible
# print(sentence);

#  Several ways to declare the string 
#  1) if we want to print the text on different line
name =''' 
hi \n
virat this 
side

'''
# print(name)

#  2) By using \n -> use for new line

value ="\n virat  \n mahajan";
# print(value)

# Several method of an String Class

# print(len(value))

name =" virat kohli"
# upper and  lower
# print(name.upper().lower())

# title  -> It wil make each first character as capital of an whole string
print(name.title()) 

# capitalize -> It makes only first character as uppercase from whole string

print(name.capitalize())

# strip -> Removes the spaces 

print(name.strip())

# Replace -> This used to replace the character from string

print(name.replace('v','V'))

# will convert string into list
names = name.strip().split(" ")

print(names)


# find  -> To index of an alphabet

print(name.find("v"))


# startWith -> check starting text 
print(name.startswith("kohli"))

# endsWith ->  check ending text

print(name.endswith("kohli"))

# count -> to count the occurance

print(name.count("i"))

# isalpha -> only alpha  or not

print(name.isalpha())

# isdigit ->  check if string contain only digit or not

print(name.isdigit())

# isalnum -> it will check is it contain alphabets and  digits or not

print(name.isalnum())

# used to add space around text
print("Python".center(20))

# join used to join two string 
letters = ['P', 'Y', 'T', 'H', 'O', 'N']

print("".join(letters))