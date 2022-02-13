#Bir dizideki en küçük elemanı bulan uygulama yazın.

array=[8,7,9,17,3,-5,-1,6,20,13]

temp=array[0]

for i in range(0,10):
    if temp>array[i]:
        temp=array[i]
print("en büyük değer : "+str(temp))

temp=array[0]

for i in range(0,10):
    if temp<array[i]:
        temp=array[i]
    
print("en küçük eleman :"+str(temp))
