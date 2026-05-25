
# List Data Type
''' 
If we want to represent a group of individual objects as a single entity where insertion 
order preserved and duplicates are allowed, then we should go for List. 
# List is mutable
1)Insertion order preserved. 
2)duplicate objects are allowed 
3)heterogeneous objects are allowed. 
4)List is dynamic because based on our requirement we can increase the size and decrease 
the size. 
5) In List the elements will be placed within square brackets and with comma seperator.
'''
list = [10,2222,6763,887,99,9086,900,'hi'];
print(list)
# Slicing 
print(list[1:7:2])


list2 =[100,90,50];
list3 =[1000,320,670];

# we can mix two differnet list
mix = [list2,list3];
print(mix[1][0])


# we can combine two different list by using + operator

list4 =[100,90,50];
list5 =[1000,320,670];

combine = list4 + list5;
print(combine)

# appned()
# we can add the value at the end by append
list4 =[100,90,50];
list4.append(600)
print(list4);

# count -> To check the occurance of an value

list5 =[10,10,333,333,212,221]

print(list5.count(333))

# insert -> it will insert the value at perticular index

list5.insert(2,2);
print(list5)

# Remove -> To delete the value 

list5.remove(10)
print(list5)

# pop -> It will delete the value by using index , Default it will remove last 

list5.pop();
print(list5)

# del -> To delete the value from perticular index to perticular index then del is used

del list5[1:3]
print(list5)

# extend -> To add the multiple value 

list5.extend([999,666]);
print(list5)

# In built function 
# reverse
list5.reverse()
print(list5)

# sort -> it will sort in ascending order
list5.sort()
print(list5)


# important Question 
a=[33,76,24,56]
b=["navin" , "kiran" ,"harsh"]

print(((a[ :2] + b[1:])[-3]))


# min , max , sum -> Inbuilt function

print(min(list5))
print(max(list5))
print(sum(list5))


# Way to iterate on list

# 1) By using for loop
'''
list = [33,76,24,56,3990]


for i in list:
    print(i)
'''
 
# 2) By using While loop

list = [33,76,24,56,3990];

i=0;
while(i<len(list)):
    print(list[i])
    i=i+1


# cloning the object 
x=[10,20,30,40]   

y=x.copy()   
y[1]=777                                                      
print(x)    
print(y) 