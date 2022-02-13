"""
Klavyeden iki vize ve final notu alınan öğrencinin yılsonu not 
ortalamasını hesaplayan uygulama yazın.

Notlar
Yılsonu notu, vize notlarının %30'u ve final notunun %40'ı alınarak
 hesaplanır.
"""

vize1 = int(input("1. vize notunu giriniz: "))
vize2 = int(input("2. vize notunu giriniz: "))
final = int(input("Final notunu giriniz: "))

average = 0

if vize1>=0 and vize2>=0 and final>=0:
    average= vize1*30/100 + vize2*30/100 + final*40/100
    print("yılsonu notunuz: ",float(average))
else:
    print("geçerli bir not giriniz.")