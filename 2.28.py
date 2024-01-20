import math
a,b,c = eval(input("nhap cac he so : "))
dt=b**2-4*a*c
if a<0 :
    print("VO SO NGHIEM")
else:
    if dt<0 :
     print("VO NGHIEM")
    elif dt == 0 :
     print(-b/2/a)
    else:
     x1=round((-b+math.sqrt(dt))/2/a,2)
     x2=round((-b-math.sqrt(dt))/2/a,2)
     if x1 < x2:
         print(x1)
         print(x2)
     else :
         print(x2)
         print(x1)