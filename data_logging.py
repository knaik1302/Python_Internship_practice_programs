# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 12:00:08 2021

@author: kartik naik
"""

import datetime

x = datetime.datetime.now()
dt=x.strftime("%d")+"_"+x.strftime("%b")+"_"+x.strftime("%Y") 

while (1):
    e = input("Do you want to enter entry: y/n")
    if(e=='y'):
        name=input("enter the name")
        phno=int(input("enter the phone nummber"))
        place=input("enter place")
        temp=float(input("enter temperature"))
        list = [('Name: ', name),('PhNo: ',phno),('place: ',place),('Temperature: ',temp),('Date_time: ', datetime.datetime.now())]
        with open(dt+".txt", "a") as f:
            f.write("-----------------------------\n")
            f.write('\n'.join('{} {}'.format(x[0],x[1]) for x in list))   
            f.write("\n-----------------------------\n")
            f.close()
    else:
        break     