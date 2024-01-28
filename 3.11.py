n=int(input("Nhap n :"))
sc=0
sl=0
while n > 0 :
    i=n%10
    if i % 2 ==0 :
     sc+=1
    else:
     sl+=1
    n=n//10
if sl==sc :
    print("YES")
else:print("NO")