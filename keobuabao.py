# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 10:52:44 2024

@author: ACER
"""

from random import randint
print("chon 'keo', 'bua', 'bao': "); chon = input(); rdom = randint(0,2)
if rdom == 0:
    rdom = 'bao'
elif rdom == 1:
    rdom = 'bua'
else:
    rdom = 'keo'
print('Ban chon: '+chon); print('he thong chon: '+rdom);print('Ket qua: ')
if chon == rdom:
    print('Hoa')
elif chon == 'bao':
     if rdom == 'keo':
          print('He thong thang')
     else:
       print('ban thang')
elif chon =="bua":
     if rdom == "keo":
       print('Ban thang')
     else:
       print( 'He thong thang')
elif chon == "keo":
    if rdom == "bao":
       print("Ban thang")
    else:
       print ("He thong thang")
    
    
    

    