day = int(input("Nhap so ngay :"))
y=day//365
w=(day%365)//7
d=day-y*365-w*7
print(y,w,d)