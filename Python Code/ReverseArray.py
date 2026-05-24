
arr =[10,20,30,40,50];
# Declartive way
first =0;
last = len(arr) -1;

while(first <last):
    temp = arr[first];
    arr[first] = arr[last];
    arr[last] = temp;
    first= first+1;
    last = last-1;

for i in arr:
    print(i,end="\t")
 

 #  Imperative way -> Bulit in Function
arr =[10,20,30,40,50];
arr2 = reversed(arr);
print()

for i in arr2:
    print(i,end="\t")

# Built in method
print()
arr.reverse()   ;
print(arr,end="\t")