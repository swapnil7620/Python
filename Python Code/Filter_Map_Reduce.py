
from functools import reduce
# imperative way to filter

nums =[2,10,5,4,7,9]

even =[]

'''
for i in nums:
    if i % 2 == 0:
        even.append(i)
print(even)        

'''
# using declartive way
'''
def is_even(n):
      return n % 2==0
# 
is_even = lambda n: n % 2==0
List = list(filter((is_even),nums))

print(List)
'''

even =  list(filter(lambda n:n % 2!=0,nums))
double = list(map(lambda  n:n*2,even)) 
sum =  reduce(lambda a,b : a+b,double)
print(even)
print(double)
print(sum)