# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 11:49:53 2018
***This program asks the user for a host name and then tells them if it is pingable or not.
@author: Drew Strobel
"""
#%%
#the main function
def main():
    #Import the librarys and initialize the variables.
    import os
    up_cnt = 0
    down_cnt = 0
    #Prompt the user for the input.
    hostname = input("Enter a hostname or IP\n>> ")
    ping_num = int(input("How many times do you want to ping?\n>> "))
    #Ping the host based on the amount of times the user requested.
    while ping_num > 0:
        ping_num = ping_num - 1
        response = os.system("ping " + hostname)
        #adds 1 to the right up or down counter.
        if response == 0:
            up_cnt = int(up_cnt)+1
        else:
            down_cnt = int(down_cnt)+1

    #Prints the result of the test
    if ping_num == 0:
        print(hostname, 'was up for ', up_cnt, ' ping tests,\n and was down for ', down_cnt, ' ping tests.')

main()
#%%


"""
OUTPUT

Enter a hostname or IP
>> google.cvfs

How many times do you want to ping?
>> 2
google.cvfs was up for  0  ping tests,
 and was down for  2  ping tests.
 
 
 
Enter a hostname or IP
>> google.com

How many times do you want to ping?
>> 3
google.com was up for  3  ping tests,
 and was down for  0  ping tests.

"""