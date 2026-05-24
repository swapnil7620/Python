
'''
If a group of statements is repeatedly required then it is not recommended to write these 
statements everytime seperately.We have to define these statements as a single unit and 
we can call that unit any number of times based on our requirement without rewriting. 
This unit is nothing but function. 
 
The main advantage of functions is code Reusability. 

'''
'''
Python supports 2 types of functions 
 
1. Built in Functions 
2. User Defined Functions 
'''
def sum(x,y):
    val1=x
    val2=y
    return val1+ val2;

result =sum(10,20)
print(result)


#name = "python"
#Reverce ="" ;


def reversed_value(name):
        Reverce ="" ;
        i = len(name)-1
        while i>=0:
            Reverce += name[i]
            i= i-1
        return  Reverce;


Result = reversed_value("hello")
print(Result)

'''
In other languages like C,C++ and Java, function can return atmost one value. But in 
Python, a function can return any number of values

'''

def sum_sub(a,b):   
        sum=a+b   
        sub=a-b   
        return sum,sub   
    
x,y=sum_sub(100,50)   
print("The Sum is :",x)   
print("The Subtraction is :",y)   

# Types of argument

# There are 4 types are actual arguments are allowed in Python

''' 
1. positional arguments 
2. keyword arguments 
3. default arguments 
4. Variable length arguments 
'''
'''
1. positional arguments: 
These are the arguments passed to function in correct positional order. 
 '''
def sub(a,b): 
  print(a-b) 
 
sub(100,200) 
sub(200,100)


'''
2) keyword arguments: 
 
We can pass argument values by keyword i.e by parameter name.
'''

def wish(name,msg):   
     print("Hello",name,msg)   


wish(name="kafka",msg="Good Morning")   
wish(msg="Good Morning",name="kafka") 


'''
3. Default Arguments:  
Sometimes we can provide default values for our positional arguments. 
'''

def wish(name="Guest"):   
     print("Hello",name,"Good Morning")   

wish("Durga")   
wish()  

'''
4. Variable length arguments: 
 
Sometimes we can pass variable number of arguments to our function,such type of 
arguments are called variable length arguments. 
 
We can declare a variable length argument with * symbol   as follows 
 
def f1(*n): 
 
We can call this function by passing any number of arguments including zero number. 
Internally all these values represented in the form of tuple. 
'''


def sum(*n):
     
     total =0;
     for i in  n:
          total = total +i;
     return total;


result = sum(1,3,7)
print(result)

''' 
Note: Function vs Module vs Library: 
 
1. A group of lines with some name is called a function 
2. A group of functions saved to a file , is called Module 
3. A group of Modules is nothing but Library 
'''