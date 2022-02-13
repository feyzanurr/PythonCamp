#klavyeden girilen sayının mutlak değerini bulma 

num= int(input("Bir sayı giriniz"))

if num>= 0:
    print("sayının mutlak değeri : "+ str(num))
else:
    num=num * -1
    print("sayının mutlak değeri: "+ str(num))
    