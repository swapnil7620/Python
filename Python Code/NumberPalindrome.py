number =15671;
original = number;
flag = True;
update =0;
i=0;
while(number!=0):
    digit = number % 10;
    update = update * 10 +digit;
    number = number // 10; 


if original==update:
    print("Yes")

else :
    print("No")    