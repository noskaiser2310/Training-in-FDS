import math
a = int(input("Nhap a : "))
b = int(input("Nhap b : "))
c = int(input("Nhap c : "))
d = int(input("Nhap d : "))
ma = a
mi = a

if b > ma:
    ma = b
if b < mi:
    mi = b
if c > ma:
    ma = c
if c < mi:
    mi = c
if d > ma:
    ma = d
if d < mi:
    mi = d
print(ma)
print(mi)
print(max(a,b,c,d))
print(min(a,b,c,d))