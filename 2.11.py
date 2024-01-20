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