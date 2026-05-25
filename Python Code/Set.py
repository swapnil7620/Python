
# set is collection of unorder unique elements

'''
 If we want to represent a group of unique values as a single entity then we should go 
 for set. 
 Duplicates are not allowed. 
 Insertion order is not preserved.But we can sort the elements. 
 Indexing and slicing not allowed for the set. 
 Heterogeneous elements are allowed. 
 Set objects are mutable i.e once we creates set object we can perform any changes in 
that object based on our requirement. 
 We can represent set elements within curly braces and with comma seperation 
 We can apply mathematical operations like union,intersection,difference etc on set 
objects.
'''

set1 = {20,10,20,10,50,60,60.1}
print(set1)

# Sorting the set 
print(sorted(set1))

# len -> To count the length 

print(len(set1))


# split the string

set2 = set('abcdeddssdd')

#print(set2)

# union and intersection and Union all

value1 = set('abcde');
value2 = set('defgh');


print(value1 - value2)

# intersection -> maching value 
print(value1 & value2)

# union All ->  every value 
print(value1 | value2)

# ^ -> print the thing which are not comman

print(value1 ^ value2)
