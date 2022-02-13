"""
10.000 TL'yi yıllık %10 oran ile 5 yıllığına faize yatırdığımıza 5 yıl
 boyunca her yıl sonunda elde edilecek parayı ekranda görüntüleyen 
 uygulama yazın.

faizli getiri = anapara * (1 + faiz oranı)^süre

Beklenen çıktı:

1. yıl sonunda toplam anapara: 11.000,00 TL
2. yıl sonunda toplam anapara: 12.100,00 TL
3. yıl sonunda toplam anapara: 13.310,00 TL
4. yıl sonunda toplam anapara: 14.641,00 TL
5. yıl sonunda toplam anapara: 16.105,10 TL
"""

anapara = 10000

for i in range(1,6):
    faizGeliri = anapara * (1 + 10/100)** i
    print(str(i) + ". yıl sonunda toplam anapara: "+ str(faizGeliri))