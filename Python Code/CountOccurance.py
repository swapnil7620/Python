
values ="apple";
data ={};
for i in values:
    data[i]= data.get(i,0)+1;

for k ,v in data.items():
    print(k,":",v)        
     
# print(data)

