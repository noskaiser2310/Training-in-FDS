n=int(input("Nhap so luong pt : "))
a=[]
for i in range(n) :
    a.append(int(input()))
max,min=a[0],a[0]
ki,ka=0,0
for i in range(n):
    if max < a[i] :
        max=a[i]
        ka=i
    if min >= a[i] :
        min=a[i]
        ki=i
print(f"số lớn nhất {max} nằm ở {ka}")
print(f"số nhỏ nhat {min} nằm ở {ki}")
count,cout = 0,0
for i in a:
    for k in range(1, i):
        if i % k == 0:
            count += 1
    if count == 1:
        cout += 1
    count = 0
print(f"số lượng số nguyên tố : {cout} ")
s=0
for i in range(n) :
    for j in range(i+1,n) :
        t = a[i] * a[j]
        if t > s:
            s=t
print(f"tích lớn nhất của 2 số trong danh sách : {s}")
b=[]
for i in range(n-1,-1,-1) :
    b.append(a[i])
if a==b : print("Yes")
else:print("No")

count=1
for i in a:
    count*=i
print(f"tích các số trong danh sách : {count}")
