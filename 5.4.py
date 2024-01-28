n=int(input("Nhap so luong pt : "))
a=[]
x,y=0,0
for i in range(n) :
    a.append(int(input()))
for i in range(n) :
    if a[i] == 25 :
        x=x+1
    if a[i] == 50 :
        x=x-1
        y=y+1
        if x < 0 :
            print("No")
            break
    if a[i] == 100 :
     if y>0 :
        x=x-1
        y=y-1
        if x < 0 or y < 0:
            print("No")
        break
     else:
         x=x-3
         if x < 0 :
            print("No")
            break

if x>=0 and y>=0 :
    print("Yes")