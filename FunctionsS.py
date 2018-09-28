# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 17:19:33 2018

@author: John Stewart

FUNCTIONS 

"""
#%%
# This program demonstrates a function.
# First, we define a function named message.
def message():
    print('I am Arthur')
    print('King of the Britons')

# Call the message function.
message()
#%%

# This program has two functions. First we
# define the main function.
def main():
    print('I have a message for you.')
    message()
    print('Goodbye!')
    
# Next we define the message function.
def message():
    print('I am Arthur')
    print('King of the Britons.')

# Call the main function.
main()
#%%
"""
This will cause an error!  WHY?

"""
# Definition of the main function.
def main():
    get_name()
    print('Hello', name)     # This causes an error!

# Definition of the get_name function.
def get_name():
    name = input('Enter your name: ')

# Call the main function.
main()
#%%

# This program demonstrates an argument being
# passed to a function.

def main():
    value = 5
    show_double(value)
    
# The show_double function accepts an argument
# and displays double its value.
def show_double(number):
    result = number * 2
    print(result)

# Call the main function.
main()

#%%

# This program demonstrates a function that accepts
# two arguments.

def main():
    print('The sum of 12 and 45 is')
    show_sum(12, 45)

# The show_sum function accepts two arguments
# and displays their sum.
def show_sum(num1, num2):
    result = num1 + num2
    print(result)

# Call the main function.
main()


#%%
"""
Python can use keyword arguments. When a function argument is passed to a function, within the 
function it is passed to, it is called a parameter.   In addition to matching function arguments
and parameters, python allows for writing an argument in this format:
    
    parameter_name=value
    
An argument written with this syntax is known as a kwyword argument.

"""

# This program demonstrates keyword arguments.

def main():
    # Show the amount of simple interest using 0.01 as
    # interest rate per period, 10 as the number of periods,
    # and $10,000 as the principal.
    show_interest(rate=0.01, periods=10, principal=10000.0)

# The show_interest function displays the amount of
# simple interest for a given principal, interest rate
# per period, and number of periods.

def show_interest(principal, rate, periods):
    interest = principal * rate * periods
    print('The simple interest will be $', \
          format(interest, ',.2f'), \
          sep='')

# Call the main function.
main()
#%%

# This program demonstrates passes two strings as
# keyword arguments to a function.

def main():
    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name: ')
    print('Your name reversed is')
    reverse_name(last=last_name, first=first_name)

def reverse_name(first, last):
    print(last, first)

# Call the main function.
main()

#%%

# This program demonstrates passing two string
# arguments to a function.

def main():
    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name: ')
    print('Your name reversed is')
    reverse_name(first_name, last_name)

def reverse_name(first, last):
    print(last, first)

# Call the main function.
main()
#%%

# This program demonstrates what happens when you
# change the value of a parameter.

def main():
    value = 99
    print('The value is', value)
    change_me(value)
    print('Back in main the value is', value)

def change_me(arg):
    print('I am changing the value.')
    arg = 0
    print('Now the value is', arg)

# Call the main  function.
main()








#%%


# This program demonstrates keyword arguments.

def main():
    # Show the amount of simple interest using 0.01 as
    # interest rate per period, 10 as the number of periods,
    # and $10,000 as the principal.
    show_interest(rate=0.01, periods=10, principal=10000.0)

# The show_interest function displays the amount of
# simple interest for a given principal, interest rate
# per period, and number of periods.

def show_interest(principal, rate, periods):
    interest = principal * rate * periods
    print('The simple interest will be $', \
          format(interest, ',.2f'), \
          sep='')

# Call the main function.
main()


#%%


# This program demonstrates passes two strings as
# keyword arguments to a function.

def main():
    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name: ')
    print('Your name reversed is')
    reverse_name(last=last_name, first=first_name)

def reverse_name(first, last):
    print(last, first)

# Call the main function.
main()

#%%

# Create a global variable.
my_value = 10

# The show_value function prints
# the value of the global variable.
def show_value():
    print(my_value)

# Call the show_value function.
show_value()

#%%

# Create a global variable.
number = 0

def main():
    global number
    number = int(input('Enter a number: '))
    show_number()

def show_number():
    print('The number you entered is', number)

# Call the main function.
main()

"""
Comment out the "global number line

"""

#%%

"""
ACTIVITY#1


A company pays a quaterly bonus to its workiers along with retirement benefits
in the form 5% of each employees gross pay.    Both go to the employees retirement
plan.  Write a progam that calculates the company's contribution to an employee's
retirement account for the year.  Use 2 functions and call them.

Get the eimployee's annual gross pay.
Get the total amount of bonuses paid to the employee.
Calculate and display the contribution for gross pay.
Calculate and display the contribution for bonuses.
"""
#%%
def main():
    global bonus_pay, bonus_bonus, retirement_pay, total_pay
    company_percent = 0.05
    grosspay = int(input('What is your annual Gross Pay?  '))
    bonus = int(input('How much did you get in bonuses?  '))
    bonus_pay = grosspay * company_percent
    bonus_bonus = bonus * company_percent
    retirement_pay = bonus_pay + bonus_bonus
    total_pay = grosspay + bonus
    display()
    
    
def display():
    print('Your businesses contribution for you retirement account is $', retirement_pay)
    print('Your pay before business contributes is $', total_pay)
   
    
main()





