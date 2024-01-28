n=int(input("Nhap n :"))
k=0
for i in range(1,n):
    if n%i==0 :
        k+=1
if k == 1 : print("Yes")
else:print("No")