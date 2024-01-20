a=input("Nhap kí tự : ")
a = a.lower()
b = ord(a) + 1
b = chr(b)
if a == "Z" or a=="z" :
    b = "a"
print(b)