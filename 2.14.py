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