#5
n=int(input("Nhap n :"))
s=0
for i in range(1,n+1) :
    s+=1/(2*i)
print(round(s,2))