from math import factorial


isim=input("adınız")
print("isim: " +isim)

sayi= int(input("kaçın faktoriyelini hesaplayayım : "))

factorial= 1

if sayi<=0:
    print("negatif sayıların faktorieli hesaplanamaz.")
elif sayi==0:
    print("sonuç = 1")
else:
    for i in range(1,sayi+1):
        factorial = factorial*i
    print("sonuç: ",factorial)
