import math
"""
#1
x = int(input("Nhap x :"))
A = x**3 + 3*x**2 + x + 1
print(A)
"""
"""
#2
a = int(input("Nhap a :"))
b = int(input("Nhap b :"))
c = int(input("Nhap c :"))
S = a*(b+c)+b*(a+c)
print(S)
"""
"""
#3
C = int(input("Nhap nhiet do C :"))
F = (C * 9 / 5) + 32
print(format(F, ".2f"))

"""
"""
#4
R = int(input("Nhap ban kinh  :"))
C=2*3.14*R
s=R**2*3.14
print(format(C, ".4f"),format(s, ".4f"),)
"""
"""
#5
x1 = int(input("Nhap x1 :"))
y1 = int(input("Nhap y1 :"))
x2 = int(input("Nhap x2 :"))
y2 = int(input("Nhap y2 :"))
AB=math.sqrt((y2-y1)**2+(x2-x1)**2)
print(format(AB, ".2f"))
"""
"""
#6
n = int(input("Nhap n :"))
if n%2==0 and n>0:
  print("yes")
else :
  print("no")
if n%3==0 and n%5==0 :
  print("yes")
else :
  print("no")
if n%3==0 and n%7!=0 :
  print("yes")
else :
  print("no")
if n%3==0 or n%7==0 :
  print("yes ")
else :
  print("no ")
if n > 30 and n<50 :
  print("yes ")
else :
  print("no ")
if  n>29 and (n% 2==0 or n%3==0 or n%5==0 ) :
    print("yes ")
else :
  print("no ")
if   n>= 10 and n<= 99 and (n%10 == 2 or n%10 == 3 or n%10 == 5 or n%10 == 7) :
    print("yes ")
else:
    print("no ")
if n<=100 and n%23==0:
    print("yes ")
else :
  print("no ")
if not (n>= 10 and n<= 20):
    print("yes ")
else :
  print("no ")
if n%10 == 3 :
    print("yes ")
else :
  print("no ")
"""
"""
#7
a = int(input("Nhap a :"))
b = int(input("Nhap b :"))
print(a//b*b)
print((a + b - 1)// b * b)
"""

"""
#9
year = int(input("Nhập nm cần kiểm tra : "))
if year % 4 == 0 or (year % 4 == 0 and year % 100 != 0) :
    print("Day la nam nhuan ")
else :
    print("Day khong phai nam nhuan")
"""
"""
#10
a = int(input("Nhap a :"))
b = int(input("Nhap b :"))
c = int(input("Nhap c :"))
if b + c > a > 0 and a + c > b > 0 and a + b > c > 0:
    print("YES")
else:
    print("NO")
"""
"""
#11
a = int(input("Nhap a :"))
b = int(input("Nhap b :"))
c = int(input("Nhap c :"))
if  b + c > a > 0 and a + c > b > 0 and a + b > c > 0:
    if a==b==c :
        print("1")
    elif a==b or a==b or c==b :
        print("2")
    elif a**2+b**2 == c**2 or c**2+b**2 == a**2 or a**2+c**2 == b**2 :
        print("3")
    else:
        print("4")

else:
    print("INVALID")
"""

"""
#12
m = int(input("Nhap m :"))
y = int(input("Nhap y :"))

nhuan = y % 4 == 0 or (y % 4 == 0 and y % 100 != 0)
if not ( 13>m>0 and y> 1 ) :
    print("INVALID")
else:
    if (m==1 or m==3 or m== 5 or m==7 or m==8 or m==10 or m==12 ) :
        print("31")
    elif nhuan and m==2 :
        print("29")
    elif (not nhuan) and m==2 :
        print("28")
    else:
        print("30")
"""
"""
#13
day = int(input("Nhap so ngay :"))
y=day//365
w=(day%365)//7
d=day-y*365-w*7
print(y,w,d)
"""

"""
#14
a = float(input("Nhap diem hs 1 :"))
b = float(input("Nhap diem hs 1 :"))
c = float(input("Nhap diem hs 2 :"))
d = float(input("Nhap diem hs 3 :"))
dtb=(a+b+c*2+d*3)/7
if dtb >=8 :
    print("Giỏi")
elif dtb >= 6.5 :
    print("Khá")
elif dtb >= 5:
    print("Trung bình")
else:
    print("Yếu")
"""

"""
#15
n,a,b= eval(input("Nhập n,a,b : "))
if a*2 < b :
    x=n
    y=0
else:
    y=n//2
    x=n%2
print(x*a+b*y)
"""
"""
#16
a=input("Nhap kí tự : ")
a = a.lower()
b = ord(a) + 1
b = chr(b)
if a == "Z" or a=="z" :
    b = "a"
print(b)
"""

"""
#17
a=input("Nhap kí tự : ")
if a.isalpha() :
    if a.isupper() :
     print("UPPER")
    else:
     print("LOWER")
else:
    if a.isdigit() :
        print("DIGIT")
    else:
        print("SPECIAL")
"""

"""
#18
a=input("Nhap kí tự : ")
if a.isupper() :
    print(a.lower())
else:
    print(a.upper())
"""

"""
#19
import math
m = float(input("Nhap m : "))
n = float(input("Nhap n : "))
a = float(input("Nhap a : "))
s=math.ceil(n/a)+math.ceil(m/a)
print(s)
"""
"""
#20

"""
"""
#21
n = int(input("Nhap n : "))
s = int(input("Nhap s : "))
print(math.ceil(s/n))
"""
"""
#22
a = int(input("Nhap a : "))
b = int(input("Nhap b : "))
c = int(input("Nhap c : "))
d = int(input("Nhap d : "))
print(max(a,b,c,d))
print(min(a,b,c,d))
"""

"""
#23
a=float(input("Nhap a : "))
n=a-int(a)
if n <0.5 :
    a=int(a)
else:
    a=int(a)+1
print(a)
"""

"""
#24
n=int(input("Nhap n :"))
u1=int(input("Nhap u1 :"))
d=int(input("Nhap d :"))
print((2*u1+d*(n-1))*(n/2))
"""

"""
#25
a = float(input("Nhap a : "))
b = float(input("Nhap b : "))
c = float(input("Nhap c : "))
d = float(input("Nhap d : "))
m= b/a
if d/c==m and c/b==m :
    print("Yes")
else:
    print("no")
"""

"""
#26
n=int(input("Nhap n : "))
print(int((n+1)*n/2))
"""
"""
#27
n=int(input("Nhap n : "))
print(math.comb(n,2))
"""
"""
#pt^2
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
"""



