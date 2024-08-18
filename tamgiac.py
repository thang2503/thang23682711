# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 10:07:32 2024

@author: ACER
"""

print("kiểm tra 3 cạnh")
a=float(input("nhap a: "))
b=float(input("nhap b: "))
c=float(input("nhap c: "))
if a+b>c and a+c>b and b+c>a:
    if a*a==b*b+c*c or b*b==a*a+c*c or c*c==a*a+b*b:
        print (a,b,c, "là 3 cạnh của tam giác vuông")
    elif a==b and b==c:
        print (a,b,c, "là 3 cạnh của tam giác đều")
    elif a==b or b==c or a==c:
        print(a,b,c, "là 3 cạnh của tam giác cân")
    else:
        print(a,b,c, "là 3 cạnh của tam giác thường")
else:
        print(a,b,c, "không là 3 cạnh của tam giác")
        