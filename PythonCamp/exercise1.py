#Yarıçapı klavyeden girilen bir dairenin alanını hesaplayan uygulama yazın. 
# Hesaplanan alanı ekrana 4 basamak ondalık hassasiyeti ile yazdırın.

# alan = pi * r^2

pi = 3.14

class Alan:
    
    def alan(r):
        r = float(input("Yarıçap değeri giriniz: "))

        if r <=0:
            print("lütfen geçerli bir uzunluk giriniz")
        else:
            return pi * r * r
            

matematik =Alan()
sonuc = matematik.alan()
print("Alan: ", float(sonuc))