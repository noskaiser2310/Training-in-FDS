n=int(input("Nhap n :"))
sc=0
sl=0
while n > 0 :
    i=n%10
    if i % 2 ==0 :
     sc+=i
    else:
     sl+=i
    n=n//10
print(sc)
print(sl)