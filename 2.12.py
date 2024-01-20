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