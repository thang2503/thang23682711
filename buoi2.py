# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 07:16:13 2024

@author: ACER
"""

distance = float(input("Nhập độ dài đoạn đường đến trường: "))
if distance < 300:
    print("Đường đến trường quá gần. Thôi! Đi bộ")
elif distance > 1200:
    print("Đường đến trường quá xa. Thôi! Đi xe máy") 
elif distance >= 300 and distance <= 700:
    print("Đường đến trường không xa. Thôi! Đi xe đạp")
else:
    print("Không xác định")