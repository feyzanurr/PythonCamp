#kullanıcı tarafındna girilen cümle içindeki kelime sayısını bulan program

sentence = str(input("Cümleyi giriniz: "))

temp=0
for i in sentence:
    if i == " ":
        temp+=1
print(temp+1)


#ilk 100 doğal sayının toplamlarının karesi ile karelerinin toplamı
#arasındaki farkı bulan program

kareToplam=0
for i in range(1,101):
    kareToplam= kareToplam + i*i
print(kareToplam)

toplam=0
for j in range(1,101):
    toplam= toplam +j
toplamKare = toplam*toplam
print(toplamKare)


fark = toplamKare - kareToplam
print(fark)