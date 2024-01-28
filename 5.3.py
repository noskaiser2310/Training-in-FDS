n=int(input("Nhap so luong pt : "))
lst=[]
for i in range(n) :
    lst.append(int(input()))
max=lst[0]
print(lst[0])
for i in lst:
    if max <i:
        max=i
        print(i)