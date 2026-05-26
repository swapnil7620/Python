
''' 
 
  If we want to represent a group of objects as key-value pairs then we should go for 
Dictionary

 Duplicate keys are not allowed but values can be duplicated. 
 Hetrogeneous objects are allowed for both key and values. 
 insertion order is not preserved 
 Dictionaries are mutable 
 Dictionaries are dynamic 
 indexing and slicing concepts are not applicable 
'''
data = {'Java': 'eclipse' ,'python':['pycharm','vs code']}

print(data)
print(data['python'][1])

# methods of Dictionary

# Zip -> To combine keys and values pair 
keys =['math','science','English'];
values =[98,82,90];

marks =  dict(zip(keys,values));

print(marks)

# keys -> to get keys form dictionary

data = {'Java': 'eclipse' ,'python':['pycharm','vs code']}
print(data.keys())

# values ->  To get values  form dictionary

data = {'Java': 'eclipse' ,'python':['pycharm','vs code']}

print(data.values())

# del -> to delete  specific key values for to delete entire dictionary
data = {'Java': 'eclipse' ,'python':['pycharm','vs code']}

del data['Java']
print(data)


# len -> To return the length of an dictionary

data = {'Java': 'eclipse' ,'python':['pycharm','vs code']}

print(len(data))


# get -> To return value associated with key or to return message

print(data.get('Java',"not found"))


# pop()  It removes the entry associated with the specified key and returns the corresponding 
# value 
#  If the specified key is not available then we will get KeyError 

print(data.pop('Java'))
print(data)

# popItems  -> To delete the entire key and values

print(data.popitem())


# itmes() -> To get entire dictornary

data = {'Java': 'eclipse' ,'python':['pycharm','vs code']}

for k,v  in data.items():
    print(k,":",v);