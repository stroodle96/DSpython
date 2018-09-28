# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 11:49:53 2018

This asks the user for a host name and then tells them if it is pingable or not.

@author: dstro
"""
#%%
def main():  "Asks the user for the hostname and also calls the respond function"
    global response
    import os
    hostname = input('What is the HostName or IP? \n')
    response = os.system("ping " + hostname )
    respond()

def respond():  "Checks the response of the ping test and displays the results."
    if response == 0:
        print (hostname, 'is up!')
    else:
        print (hostname, response, 'is down!')

main()



"""
OUTPUT

What is the HostName or IP? google.com
google.com is up!
"""