# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 18:54:44 2018

@author: dstro
"""

#%%


"""ACTIVITY 1

Write a program that displays these numbers in a column
with decimal points aligned """


num1 = 127.899
num2 = 3465.148
num3 = 3.776
num4 = 264.821
num5 = 88.081
num6 = 799.999

print('The number is' , format(num1, '8,.2f'))
print('The number is' , format(num2, '8,.2f'))
print('The number is' , format(num3, '8,.2f'))
print('The number is' , format(num4, '8,.2f'))
print('The number is' , format(num5, '8,.2f'))
print('The number is' , format(num6, '8,.2f'))






#%%

"""ACTIVITY 2 


Write a program that asks the user for number of miles driven and gallons used
Calculate the MPG and display the result. 

"""
miles_driven = float(input('Enter Miles driven: '))
gas_used = float(input('How many Gallons of gas did you use?:\n '))

mpg = miles_driven // gas_used
print('Your MPG is' , format(mpg, '8,.2f'))



1

#%%

"""Activity 3

Write a program that calculates the total cost of meal at a resturant. Ask the user for input
on the cost of the meal.  Calculate the tip and the tax.  Print out the 
tax, tip, and the total.  You can ask the user for tax and tip or you can use 
hard coded numbers.  

"""

#%%
initial_cost = float(input('Enter the initial cost for your meal: '))
tip = initial_cost * 0.20
tax = initial_cost * 0.06
total_cost = initial_cost + tip + tax
print('Your tip due is ' , format(tip, '13,.2f'))
print('Your tax due is ' , format(tax, '13,.2f'))
print('Your total cost due is ' , format(total_cost, '2,.2f'))


#%%
"""
ACTIVITY 

Create a function to solve this problem. 
 A car is traveling down down the interstate.
 Ask the user for the speed of the car. 
 Using D = S * T, 
calculate and give an output of the distance the car will travel in 5,
8, and 12 hours. 



The output should look like:
    
    The distance the car will travel in 5 hours is...  
"""




#%%
speed = float(input('WHAT IS YOUR SPEED(MPH)? '))
time = float(input('How long have you been driving(hours)? '))
distance = speed * time
print('Your distance travelled is ' , format(distance, '2,.2f'), 'miles.')
