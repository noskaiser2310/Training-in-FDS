n = int(input("Nhap n :"))
if n%2==0 and n>0:
  print("yes")
else :
  print("no")
if n%3==0 and n%5==0 :
  print("yes")
else :
  print("no")
if n%3==0 and n%7!=0 :
  print("yes")
else :
  print("no")
if n%3==0 or n%7==0 :
  print("yes ")
else :
  print("no ")
if n > 30 and n<50 :
  print("yes ")
else :
  print("no ")
if  n>29 and (n% 2==0 or n%3==0 or n%5==0 ) :
    print("yes ")
else :
  print("no ")
if   n>= 10 and n<= 99 and (n%10 == 2 or n%10 == 3 or n%10 == 5 or n%10 == 7) :
    print("yes ")
else:
    print("no ")
if n<=100 and n%23==0:
    print("yes ")
else :
  print("no ")
if not (n>= 10 and n<= 20):
    print("yes ")
else :
  print("no ")
if n%10 == 3 :
    print("yes ")
else :
  print("no ")