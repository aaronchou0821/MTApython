# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 15:44:02 2021

@author: TQC
"""

try :
    a=int(input("第一個數:"))
    b=int(input("第二個數:"))
    r=a/b
    print("r=",r)
except IOError :
    print("輸入錯誤")
except NameError :
    print("名字錯誤")
except ValueError :
    print("數值錯誤")
else:
    print("當try可以執行時,我就print進來")
finally:
    print("123456")