n=int(input("Nhap so luong pt : "))
a=[]
k=0
for i in range(n) :
    a.append(int(input()))
for i in range(1,n) :
    if a[i] > a[i - 1]:
        k=0
    else:
        k=1
        break
if k==0 :
    print("Yes")
else:
    print("No")