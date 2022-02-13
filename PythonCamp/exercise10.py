"""
Klavyeden 1-7 arası girilen sayının hangi gün olduğunu bulan bir 
uygulama yazın.

Klavyeden 1-7 aralığı dışında bir sayı girilirse kullanıcıya 
hata mesajı gösterilmeli ve tekrar giriş yapması istenmelidir.

1: Pazartesi
2: Salı
3: Çarşamba
4: Perşembe
5: Cuma
6: Cumartesi
7: Pazar
Diğer ihtimaller için: Hatalı giriş
"""

temp=int(input("gün numarası giriniz:"))

if temp==1:
    print("Pazartesi")
elif temp==2:
    print("salı") 
elif temp==3:
    print("çarşamba") 
elif temp==4:
    print("perşembe") 
elif temp==5:
    print("cuma") 
elif temp==6:
    print("cumartesi") 
elif temp==7:
    print("Pazar") 
else:
    print("hatalı giriş") 