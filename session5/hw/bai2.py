import math

a = int(input("nhap vao 1 so: "))

count = 0
for i in range(2, a):

    if a % i == 0:
        count += 1
if count == 0:
    print("la so nguyen to")
else:
    print("k phai so nguyen to")    
