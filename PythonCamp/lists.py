
from math import prod


products = ["laptop", "mouse","keybord"]

print(products)
print(type(products))

products.append("phone")
print(products)

students1= ["ilker", "cavit", "berkay"]
students2 =["kerem", "halil", "murat"]

students1 = students2  #oop
students2[0] = "engin"

print(students1)
print(students2)


num1 = 10
num2 = 20
num1 = num2
num2=60
print(num2,num1)

#referans tip -> list(diziler)  **heapde çalışır
#değer(sayısal) tip ->int   **stackte çalışır
#str de bir liste türüdür.

isim="feyza"
print(isim[0])  
