# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 10:19:30 2024

@author: ACER
"""

a = float (input("Số km taxi đi được: "))
if a<=1:
    b=20.000
    print("tiền taxi là: ", b)
elif a<=3:
     b=13.000*a
     print("tiền taxi là: ", b)
elif a>8:
    b=3*13+(a-3)*12
    print("tiền taxi là: ", b)
if b >100:
    b =b*0.92
    print("tiền taxi sau giảm là: ", b)
    
    
     
     


