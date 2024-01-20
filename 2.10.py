a = int(input("Nhap a :"))
b = int(input("Nhap b :"))
c = int(input("Nhap c :"))
if b + c > a > 0 and a + c > b > 0 and a + b > c > 0:
    print("YES")
else:
    print("NO")