# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 13:02:07 2018

@author: John Stewart 
"""

"""Arithmatic Operations"""

12+2



#%%
"""
Floating Point and Integer Division

"""

5/2

#Integer Division


5//2


-5//2

#%%

"""Precidence"""

12.0 + 6.0 /3.0

#%%

(5 + 2) * 4



#%%

""" Exponent Operator """

4**2

#%%

5**3


#%%
"""
Remainder Operator

"""

leftover = 17 % 3
print(leftover)



#%%
# Get a number of seconds from the user.
total_seconds = float(input('Enter a number of seconds: '))

# Get the number of hours.
hours = total_seconds // 3600

# Get the number of remaining minutes.
minutes = (total_seconds // 60) % 60

# Get the number of remaining seconds.
seconds = total_seconds % 60

# Display the results.
print('Here is the time in hours, minutes, and seconds:')
print('Hours:', hours)
print('Minutes:', minutes)
print('Seconds:', seconds)

#%%

"""DATA TYPE CONVERDIONS"""

my_number = 5 * 2.0
print(my_number)

#%%

fvalue = 2.6
invalue = int(fvalue)
print(invalue)

#%%

invalue = 3
fvalue = float(invalue )
print (fvalue)


#%%


#%%

# This program gets an item's original price and
# calculates its sale price, with a 20% discount.

# Get the item's original price.
original_price = float(input("Enter the item's original price: "))

# Calculate the amount of the discount.
discount = original_price * 0.2

# Calculate the sale price.
sale_price = original_price - discount

# Display the sale price.
print('The sale price is', sale_price)



#%%

"""Escape Characters:  \n gives you a new line """

monday = 30008
tuesday = 29384
wednesday = 41948

print ("Monday's sales are", monday, "\n and Tuesday's sales are", tuesday, 
"\n and Wednesday's sales are", wednesday)

#%%
print("one\ntwo\nthree")


#%%


"""Supressing the print Functions Ending Newline """

print('One')
print('Two')
print('Three')

print('One', end=' ')
print('Two', end=' ')
print('Three', end=' ')



#%%

"""Formatting Numbers"""

# This program demonstrates how a floating-point
# number is displayed with no formatting.
amount_due = 5000.0
monthly_payment = amount_due / 12
print('The monthly payment is', monthly_payment)

#%%

"""format specifier

In this case .2 is the precision and f is the data type of the number
we are specifying"""


print(format (12345.6789, '.2f'))
print(format (12345.6789, '.1f'))

print('The number is', format(1.23456, '.2f'))


#%%

# This program demonstrates how a floating-point
# number can be formatted.
amount_due = 5000.0
monthly_payment = amount_due / 12
print('The monthly payment is', \
      format(monthly_payment, '.2f'))



#%%

"""Comma Separators"""

print(123456789)

print(format(12345.6789, ',.2f'))

print(format(123456789.456, ',.2f'))

print(format(12345.6789, ',f'))


#%%

# This program demonstrates how a floating-point
# number can be displayed as currency.
monthly_pay = 5000.0
annual_pay = monthly_pay * 12
print('Your annual pay is $', \
      format(annual_pay, ',.2f'), \
      sep='')


#%%

"""Setting minimum field width"""

print('The number is' , format(12345.6789, '20,.2f'))
print('The number is' , format(12345.6789, '12,.2f'))
print('The number is' , format(12345.6789, '4,.2f'))


 
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

