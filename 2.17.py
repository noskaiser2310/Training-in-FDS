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