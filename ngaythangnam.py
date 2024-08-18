# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 11:11:14 2024

@author: ACER
"""

def is_leap_year(year):
    """kiem tra mot nam co phai la nam nhuan khong."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def is_valid_date(day, month, year):
    """Kiem tra tinh hop le cua ngay thang nam."""
    if month < 1 or month > 12:
        return False
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 1 <= day <= 31
    elif month in [4, 6, 9, 11]:
        return 1 <= day <= 30
    elif month == 2:
        if is_leap_year(year):
            return 1 <= day <= 29
        else:
            return 1 <= day <= 28
    return False

def main():
    date_str = input("Nhap ngay thang nam theo dinh dang dd/mm/yyyy hoac dd-mm-yyyy: ")
    date_str = date_str.replace('-', '/')
    try:
        day, month, year = map(int, date_str.split('/'))
        
        if is_valid_date(day, month, year):
            print("Ngay thang nam hop le.")
        else:
            print("Ngay thang nam khong hop le.")
    except ValueError:
        print("Dinh dang ngay thang khong dung.")
        

