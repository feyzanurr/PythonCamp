num1 = 10
num2 = 30
num3 = 45
temp =0

if num1>num2:
    temp=num1
elif num1>num3:
    temp=num1
elif num2> num3:
    temp=num2
else:
    temp=num3
print("en büyük sayı : "+str(temp))