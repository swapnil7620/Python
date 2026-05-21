8
value = "abba";
flag = True;
for i in range(len(value)):
     if(value[i] != value[len(value)-1-i]):
        flag =False;  
     

if(flag) : 
   print("yes") 
else :
   print("No")