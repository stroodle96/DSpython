# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 17:14:53 2018

@author: John Stewart

Decison Structures:  IF STATEMENTS

"""

#%%

def test_scores():
# This program gets three test scores and displays
# their average.  It congratulates the user if the
# average is a high score.

# The high score variable holds the value that is
# considered a high score.
    high_score = 95
     
    # Get the three test scores.
    test1 = int(input('Enter the score for test 1: '))
    test2 = int(input('Enter the score for test 2: '))
    test3 = int(input('Enter the score for test 3: '))
    
    # Calculate the average test score.
    average = (test1 + test2 + test3) / 3
    
    # Print the average.
    print('The average score is', average)
    
    # If the average is a high score,
    # congratulate the user.
    if average >= high_score:
        print('Congratulations!')
        print('That is a great average!')





#%%
def if_statement():
    """ Three slightly difference versions of if: if, if-else, if-elif-else"""
    x = 5
    y = 0
    z = 0
    if x > 0:
        print("x is positive")
        
    if y > 0:
        print("y is positive")
    else:
        print("y is not positive")
        
    # elif can be repeated as often as necessary    
    if z > 0:
        print("z is positive")
    elif z < 0:
        print("z is negative")
    else:
        print("z must be 0")
        
        
#%%

        #%%
        
def letterGrade(score):
    if score >= 90:
        letter = 'A'
    else:   # grade must be B, C, D or F
        if score >= 80:
            letter = 'B'
        else:  # grade must be C, D or F
            if score >= 70:
                letter = 'C'
            else:    # grade must D or F
                if score >= 60:
                    letter = 'D'
                else:
                    letter = 'F'
    return letter
#%%

def letterGrade(score):
    if score >= 90:
        letter = 'A'
    elif score >= 80:
        letter = 'B'
    elif score >= 70:
        letter = 'C'
    elif score >= 60:
        letter = 'D'
    else:
        letter = 'F'
    return letter
        



        
        
#%%
def calcWeeklyWages(totalHours, hourlyWage):
    '''Return the total weekly wages for a worker working totalHours,
    with a given regular hourlyWage.  Include overtime for hours over 40.
    '''
    if totalHours <= 40:
        totalWages = hourlyWage*totalHours
    else:
        overtime = totalHours - 40
        totalWages = hourlyWage*40 + (1.5*hourlyWage)*overtime
    return totalWages


#%%



def calcWeeklyWages(totalHours, hourlyWage):
    '''Return the total weekly wages for a worker working totalHours,
    with a given regular hourlyWage.  Include overtime for hours over 40.
    '''
    if totalHours <= 40:
        regularWages = hourlyWage*totalHours
        totalWages = regularWages
    else:
        overtime = totalHours - 40
        regularWages = hourlyWage* (totalHours - 40)
        overtimeWages = (1.5*hourlyWage)*overtime
        totalWages = regularWages + overtimeWages                           
    print(regularWages) 
    print(overtimeWages)                               
    return totalWages
        
            
#%%
"""
Python uses '=' for assignment and '==' for testing equality. Also '!=' is
used to test for non-equality. Try these examples:
"""
#%%

"""Input these values and then try the folowing print statements"""
x = 5
y = 5
z = 6
#%%
""" 
Now we try to following:
"""
print("x is equal to y: ", x == y)
print("x is not equal to y: ", x != y)
print("x is equal to z: ", x == z)
print("x is not equal to z: ", x != z)
#%%
"""
The following function uses an 'if' statement. Note that the indention marks
the scope of the 'if', 'elif', 'else' actions.
"""
def area(type_, x):
    """ Computes the area of a square or circle. 
        type_ must be the string "circle or the string "square" 
        We use type_ here, because type is a Python keyword. """
    if type_ == "circle":
        area = 3.14*x**2
        print(area)
    elif type_ == "square":
        area = x**2
        print(area)
    else:
        print("I don't know that one.")
        

#%%

"""
Example: The next three examples work with the 'input' statement and point out
some of the things that you might need to be aware of in using one. It also
shows how to use the 'print' statement without having a new line started at
the end of that statement by using an 'end' argument in it.
"""
#%%

def fahrenheit_to_celsius1():
    """ BAD. Does not check input before using it. 
    Input from keyboard, which is always a string and must often be
    converted to an int or float. 
    Converts Fahrenheit temp to Celsius.
    """
    
    temp_str = input("Enter a Fahrentheit temperature: ")
    temp = int(temp_str)
    newTemp = 5*(temp-32)/9
    print("The Fahrenheit temperature",temp,"is equivalent to ",end='')
    print(newTemp,"degrees Celsius")
    

#%%
"""
Test the program above by entering a temperature such as 212. Also check what
happens if you simply press enter.   This is a Python Error.  If you just press return
it cannot convert a blank to an integer.  Crashes the program.  A problem. 
"""
#%%

def fahrenheit_to_celsius2():
    """We can improve the program with error checking of input before using it.
    
    Uses 'if' to make sure an entry was made.
    """
    
    temp_str = input("Enter a Fahrenheit temperature: ")
    if temp_str:
        temp = int(temp_str)
        newTemp = 5*(temp-32)/9
        print("The Fahrenheit temperature",temp,"is equivalent to ",end='')
        print(newTemp,"degrees Celsius")

#%%
"""
Test the program above by entering the temperature 212 and also by simply
pressing 'Enter' or 'Return' key. Note the improvement. Now try entering 'a' or
212.5.   What happens?   You still get an error. 
"""
#%%
def fahrenheit_to_celsius3():
    """ MORE IMPROVED. Does even more checking of input before using it. 
    Input from keyboard, which is always a string and must often be
    converted to an int or float. 
    Converts Fahrenheit temp to Celsius.
    Uses if to check whether input is a number and then uses .isdigit() method 
    of strings to check whether input is made of of digits. 
    """
        
    temp_str = input("Enter a Fahrentheit temperature: ")
    if temp_str:
        if temp_str.isdigit():  
            temp = int(temp_str)
            newTemp = 5*(temp-32)/9
            print("The Fahrenheit temperature",temp,"is equivalent to ",end='')
            print(newTemp,"degrees Celsius")
        else:
            print("You must enter a number. Bye")
#%%
"""
Test the program above by entering the temperature 212, by simply pressing 
'Enter' or 'Return' key, and by entering 'a'. Note the improvement. We will
leave the function at this point though further improvements could be made.
"""


#%%

# This program compares two strings.
# Get a password from the user.
password = input('Enter the password: ')

# Determine whether the correct password
# was entered.
if password == 'prospero':
    print('Password accepted.')
else:
    print('Sorry, that is the wrong password.')





#%%


#%%


# This program compare strings with the < operator.
# Get two names from the user.
name1 = input('Enter a name (last name first): ')
name2 = input('Enter another name (last name first): ')
    
# Display the names in alphabetical order.
print('Here are the names, listed alphabetically.')

if name1 < name2:
    print(name1)
    print(name2)
else:
    print(name2)
    print(name1)


#%%

# This program determines whether a bank customer
# qualifies for a loan.

min_salary = 30000.0  # The minimum annual salary
min_years = 2         # The minimum years on the job

# Get the customer's annual salary.
salary = float(input('Enter your annual salary: '))

# Get the number of years on the current job.
years_on_job = int(input('Enter the number of ' +
                         'years employed: '))

# Determine whether the customer qualifies.
if salary >= min_salary:
    if years_on_job >= min_years:
        print('You qualify for the loan.')
    else:
        print('You must have been employed', \
              'for at least', min_years, \
              'years to qualify.')
else:
    print('You must earn at least $', \
          format(min_salary, ',.2f'), \
          ' per year to qualify.', sep='')


#%%
# This program determines whether a bank customer
# qualifies for a loan.

min_salary = 30000.0  # The minimum annual salary
min_years = 2         # The minimum years on the job

# Get the customer's annual salary.
salary = float(input('Enter your annual salary: '))

# Get the number of years on the current job.
years_on_job = int(input('Enter the number of ' +
                         'years employed: '))

# Determine whether the customer qualifies.
if salary >= min_salary and years_on_job >= min_years:
    print('You qualify for the loan.')
else:
    print('You do not qualify for this loan.')


#%%

# This program determines whether a bank customer
# qualifies for a loan.

min_salary = 30000.0  # The minimum annual salary
min_years = 2         # The minimum years on the job

# Get the customer's annual salary.
salary = float(input('Enter your annual salary: '))

# Get the number of years on the current job.
years_on_job = int(input('Enter the number of ' +
                         'years employed: '))

# Determine whether the customer qualifies.
if salary >= min_salary or years_on_job >= min_years:
    print('You qualify for the loan.')
else:
    print('You do not qualify for this loan.')




#%%
"""
ACTIVITY#2

Design a simple payroll program that calculates an employees gross pay including 
overtime wages.  If an emplyee works over 40 hours they are entitled to
overtime pay for the hours worked over 40.  Use and call FUNCTIONS to modularize your
code. 

Include tax rate module and determine net pay

"""
#%%45
payrate = int(input('What is your hourly rate?  '))
hours = int(input('How many hours did you work this week?  '))

def main():
    global pay, regular_pay, overtime_pay, hours
    if hours <= 40:
        pay = payrate * hours
    else:
        overtime_hours = hours - 40
        overtime_pay = (1.5 * payrate) * overtime_hours
        regular_pay = payrate * 40
        pay = overtime_pay + regular_pay 
    printing()
    
def printing():
    if hours <= 40:
        print('Your total pay is $', pay)
    else:
        print('Your regular pay is $', regular_pay)
        print('Your overtime pay is $', overtime_pay)
        print('Your total pay is $', pay)
    return print
main()



#%%
ACTIVITY#3
"""
A company sells widgits that retail for $100. but quantity discounts are
available according tothe following schedule:
    
Quantity        Discoumt
10-19           20%
20-49           30%
50-99           40%
100 or more     50%

Write a program that gets input from the user on the quantity and calculates
and displays the amount of the discount and the total amount of the 
transaction after the discount. 

"""
#%%
price = 100
discount_20 = .2
discount_30 = .3
discount_40 = .4
discount_50 = .5

quantity = int(input('How many widgets are you buying?  '))

if quantity < 10:
    discount = 0
    total_price = (quantity * price) - discount
elif quantity >= 10 and quantity <= 19:
    discount = (quantity * price) * discount_20
    total_price = (quantity * price) - discount
elif quantity >= 20 and quantity <= 49:
    discount = (quantity * price) * discount_30
    total_price = (quantity * price) - discount
elif quantity >= 50 and quantity <= 99:
    discount = (quantity * price) * discount_40
    total_price = (quantity * price) - discount
else:
    discount = (quantity * price) * discount_50
    total_price = (quantity * price) - discount
    
print('Your discount is $', discount)
print('Your total price after the discount is $', total_price)




#%%
"""
ACTIVITY#4

In this program, we will be taking a password as a combination of alphanumeric characters along 
with special characters, and check whether the password is valid or not with the help of few 
conditions.

Primary conditions for password validation :

Minimum 8 characters.
The alphabets must be between [a-z]
At least one alphabet should be of Upper Case [A-Z]
At least 1 number or digit between [0-9].
At least 1 character from [ _ or @ or $ ].

                          
Ask the user for a password and test its acceptability based on the above criterea
Display whether the password is accceptable or not. 


"""
#%%
password = input('What is the Password?')
good_pass = 1
import re
if re.search('[@$]', password):
        good_pass = 0
        break
elif len(password) < 8:
        good_pass = 0
        break
elif re.search('[A-Z]', password):
        good_pass = 0
        break
elif re.search('[a-z]', password):
        good_pass = 0
        break
elif re.search('[0-9]', password):
        good_pass = 0
        break
if good_pass == 0:
    print('Your Password does not meet requirements.')
else:
    print('Your password looks good!')

    
    
    
"""

This last activity is more of a challenge.   In my code, I used 

If-elif-else
re.search to search for different characters in the password string
the len function to determine the length of the password string
a flag variable to detemine if the password chosen is acceptable or not
a while loop with a Break


"""
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1





#%%


#Example of the use of len() function 

mylist = ["apple", "banana", "cherry"]
x = len(mylist)
print(x)


#%%



"""

Python offers two different primitive operations based on regular expressions:
re.match() checks for a match only at the beginning of the string,
 while re.search() checks for a match anywhere in the string (this is what Perl does by default).

For example:
    
"""
import re
#re.match("c", "abcdef")    # No match
re.search("c", "abcdef")   # Match

#%%

"""
FLAGS 

Very often flags are variables that are allowed to only have TWO values. In most languages you find
 flags should only have 2 values, and the Boolean values are usually allowed to be True and False. 
(Those are the constants that Python uses.)

A flag is a logical concept, not a special type of variable. The concept is that a variable records
 the occurrence of an event.
That it is set "one way" if the event happened, and set "the other way" if the event did not happen.

"""

## An example of the use of a flag variable 
big_number_flag = False
for i in range(5):
	n = int (input("Enter a number"))
	if n > 2000:
		big_number_flag = True
	else:
  		big_number_flag = False

# after the loop
if big_number_flag:
      print("saw at least one big number")
else:
      print("didn't see any big numbers")
















