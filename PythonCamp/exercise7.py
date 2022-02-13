"""
Kullanıcı 1 ile 100 arasında sayı girene kadar tekrar giriş yapmasını isteyen bir uygulama yazın.

Notlar

Her seferinde

1'den küçükse "Girdiğiniz sayı 1'den küçük. Tekrar deneyin.",

100'den büyükse "Girdiğiniz sayı 100'den büyük. Tekrar deneyin.",

1-100 arasındaysa "Teşekkürler! 1 ile 100 arasında bir sayı girdiniz."

şeklinde kullanıcıya uyarı verin. 
"""

i= int(input("Bir sayı giriniz: "))

if i<=0:
    print("Girdiğiniz sayı 1'den küçük. Tekrar deneyin.")
if i>100:
    print("Girdiğiniz sayı 100'den büyük. Tekrar deneyin.")
if i<100 and i>0:
    print("Teşekkürler! 1 ile 100 arasında bir sayı girdiniz.")