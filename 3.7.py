#7
n=int(input("Nhap n :"))
s=0
while n > 0 :
    i=n%10
    s+=i
    n=n//10
print(s)