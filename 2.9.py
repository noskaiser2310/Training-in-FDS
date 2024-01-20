year = int(input("Nhập nm cần kiểm tra : "))
if year % 4 == 0 or (year % 4 == 0 and year % 100 != 0) :
    print("Yes ")
else :
    print("NO")