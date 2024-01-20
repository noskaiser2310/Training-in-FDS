n= int(input("Nhập n : "))
a= int(input("Nhập a : "))
b= int(input("Nhập b : "))
if a*2 < b :
    x=n
    y=0
else:
    y=n//2
    x=n%2
print(x*a+b*y)