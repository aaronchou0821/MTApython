# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 14:49:15 2021

@author: TQC
"""

score = int(input("分數:"))

if (score>90 and score<=100) :
    print("A")
elif (score>80 and score<=90) :
    print("B")
elif (score>70 and score<=80) :
    print("C")
elif (score>60 and score<=70) :
    print("D")
elif (score>0 and score<=60) :
    print("Not Good")