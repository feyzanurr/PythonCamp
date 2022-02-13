class mathematic:
    def __init__(self,num1,num2):  #contructer-yapıcı blok
        #self local bir değişken olduğu için globale çevirdik
        self.n1=num1
        self.n2=num2
        #self keywordünü kullanmak zorunlu,ini yazılmasa bile arkada zaten dönüyor
        print("matematik başladı (referans Oluştuu)")

    def Topla(self):
        return self.n1+self.n2
    
    def Cıkar(self):
        return self.n1-self.n2

    def bol(self):
        return self.n1/self.n2
    
    def Carp(self):
        return self.n1*self.n2

matematik = mathematic(6,7)
sonuc = matematik.Topla()
print("sonuç : "+str(sonuc))

#inheritance

class Istatistik(mathematic):
    def __init__(self, num1, num2):
        super().__init__(num1, num2)
    def varyansHesapla(self):
        return self.n1*self.n2

istatistik = Istatistik(5,8)