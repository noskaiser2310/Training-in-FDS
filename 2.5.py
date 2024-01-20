import math
x1 = int(input("Nhap x1 :"))
y1 = int(input("Nhap y1 :"))
x2 = int(input("Nhap x2 :"))
y2 = int(input("Nhap y2 :"))
AB=math.sqrt((y2-y1)**2+(x2-x1)**2)
print(format(AB, ".2f"))