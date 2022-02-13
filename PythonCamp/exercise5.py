#Klavyeden girilen 10 adet sayının ortalamasını hesaplayan uygulama yazın.
average=0
for i in range(1,11):
    num= int(input(str(i) + ".sayıyı giriniz: "))
    average += num
print("ortalama : "+str(average))