"""A receptionist has the duty of noting the details of visitors walking-in to the office. She notes in the register their name, phone number, place coming from and body temperature. In a view to change this pen-paper task to a computer task, use your python programming skills to make a solution for this operation.
The program should be able to gather the four inputs mentioned earlier. Besides, a database/text file should be created in the local device (computer) with this data. Bring out the best solution! When there are no more entries, any solution as per programmer's choice may be used to terminate the execution of the program.
Note:
1. Use of any suitable data structure is entertained
2. Concepts discussed during 'File Handling' may help to create file in machine with current date-time as file name
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
