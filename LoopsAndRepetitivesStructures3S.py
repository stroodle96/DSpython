# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 17:19:29 2018

@author: John Stewart
LOOPs
Repetitive Structures
"""

#%%    

"""
The 'while' loop. Loops are used to repeat actions and the scope of this
repetition is indicated by the indention after the 'while' statement.
"""
#%%

def counts():
    count = 0
    while (count < 9):
      print ('The count is:', count)
      count = count + 1
      
      #%%
      
      
      
      
#%%

# This program calculates sales commissions.

# Create a variable to control the loop.
keep_going = 'y'

# Calculate a series of commissions.
while keep_going == 'y':
    # Get a salesperson's sales and commission rate.
    sales = float(input('Enter the amount of sales: '))
    comm_rate = float(input('Enter the commission rate: '))

    # Calculate the commission.
    commission = sales * comm_rate

    # Display the commission.
    print('The commission is $', \
          format(commission, ',.2f'), sep='')

    # See if the user wants to do another one.
    keep_going = input('Do you want to calculate another ' + \
                       'commission (Enter y for yes): ')


#%%

"""  Functions can be called in the loop """

#%%


password = ''

while password != 'password':
    print('What is the password?')
    password = input()

print('Yes, the password is ' + password + '. You may enter.')

#%%


import random

number = random.randint(1, 25)

number_of_guesses = 0

while number_of_guesses < 5:
    print('Guess a number between 1 and 25:')
    guess = input()
    guess = int(guess)

    number_of_guesses = number_of_guesses + 1

    if guess < number:
        print('Your guess is too low')

    if guess > number:
        print('Your guess is too high')

    if guess == number:
        break

if guess == number:
    print('You guessed the number in ' + str(number_of_guesses) + ' tries!')

else:
    print('You did not guess the number. The number was ' + str(number))



#%%

# 
# Username and Password...
# The programs purpose: A user must enter the correct username and password for a site called FaceSnap...
# The correct username is elmo and the correct password is blue.


userName = input("Hello! Welcome to Pioneers! \n\nUsername: ") #Ask's the User for Username input
password = input("Password: ") # Ask's the user for their password


count = 0 # Create a variable, to ensure the user has limited attempts at entering their correct username and password
#count += 1 # The user has already had one attempt above, therefore count has been incremented by 1 already.


while userName == userName and password == password: # The Input will always lead to this while loop, so we can see if their username and password is wrong or correct.


    if count == 3 and userName != 'elmo' and password != 'blue': # Counter, to make sure the user only gets a limited number (3)of attempts
        print("\nThree Username and Password Attempts used. Goodbye") # Lets the user know they have reached their limit
        break # Leave the Loop and the whole program


    elif userName == 'elmo' and password == 'blue': # The userName and password is equal to 'elmo' and 'blue', which is correct, they can enter FaceSnap!
        print("Welcome! ") # Welcomes the User, the username and password is correct
        break # Leave the loop and the whole program as the username and passowrd is correct


    elif userName != 'elmo' and password != 'blue': # The userName and password is NOT equal to 'elmo' and 'blue', the user cannot enter FaceSnap
        print("Your Username and Password is wrong!") # Lets the user know that the Username and password entered is wrong.
        userName = input("\n\nUsername: ") # Requests the user to have another attempt at entering their correct username
        password = input("Password: ") # Requests the user to have another attempt at entering their correct password
        count += 1 # Increments the count by 1
        continue # Continue, as the user hasn't managed to get their username and password correct yet


    elif userName == 'elmo' and password != 'blue': # The userName is equal to 'elmo', but password is NOT equal to 'blue', the user cannot enter FaceSnap
        print("Your Password is wrong!") # Lets the user know that their password is wrong
        userName = input("\n\nUsername: ") # Requests the user to have another attempt at entering their correct username
        password = input("Password: ") # Requests the user to have another attempt at entering their correct password
        count += 1 # increments the count by 1
        continue # Continue, as the user hasn't managed to get their username and password correct yet


    elif userName != 'elmo' and password == 'blue': # The userName is NOT equal to 'elmo', however password is equal to 'blue', the user cannot enter FaceSnap
        print("Your Username is wrong!") # Lets the user know that their username is wrong
        userName = input("\n\nUsername: ") # Requests the user to have another attempt at entering their correct username
        password = input("Password: ") # Requests the user to have another attempt at entering their correct password
        count += 1 # Increments the count by 1
        continue # Continue, as the user hasn't managed to get their username and password correct yet




#%%


count = 0 
while True: 
    userName = input("Hello! Welcome to Pioneers! \n\nUsername: ") 
    password = input("Password: ")
    
    if count == 3: 
        #tells user bye
        break #exit
    else:
        if userName == 'elmo' and password == 'blue':
            #let them in
            print("You are logged in!")
            break #they are in, exit loop
        else:
            #tell them it is wrong and have them retry, stay in loop
            print("Wrong!")
count += 1           
            
#%%
   #Creating empty list
countries = []

#Creating variable that will control number of countries we can enter
count = 0

#Creating the while loop
while count < 5: #This ensures that only five countries can be entered
       next=input("Please enter a country you've been to: ")
     
       #If conditional statement to verify input
       if len(next) > 0 and next.isalpha():
              countries.append(next)
              count = count + 1
       else:
              print( "I'm sorry, but I can't accept that input")
print (countries)         
  

#%% #%%



def Great():
    """ Prints 2 4 6 8,  Notice that everything in 
    the while loop is indented. The first line not indented is the first
    line following the while loop. """
    ct = 2
    while ct <= 8:
        print(ct,end=" ")  # end = " " keeps from starting a new line
        ct = ct + 2
    print()                # now we'll start a new line
    print("Isn't Python Great?")
    


 
#%%

"""  For loops  are count controlled loops.  They iterate a specific number of times

"""


# This program demonstrates a simple for loop
# that uses a list of numbers.

print('I will display the numbers 1 through 5.')
for num in [1, 2, 3, 4, 5]:
    print(num)
    
#%%
"""
The range function will iterate over a range of numbers.  In this case 0 through 5.

"""

for i in range(6):
   print(i)
#In the program above, the stop argument is 6, so the code will iterate from 0-6 (exclusive of 6):

#%%
"""Next, we look at range(start, stop), with values passed for when the iteration should start 
and for when it should stop:
"""

for i in range(20,25):
   print(i)
 
    
   """
  Here, the range goes from 20 (inclusive) to 25 (exclusive)

The step argument of range() is similar to specifying stride while slicing strings in that it can
 be used to skip values within the sequence.

With all three arguments, step comes in the final position: range(start, stop, step). First, let’s 
use a step with a positive value:
    
"""


#%%

#%%

# This program uses a loop to display a
# table showing the numbers 1 through 10
# and their squares.

# Print the table headings.
print('Number\tSquare')
print('--------------')

# Print the numbers 1 through 10
# and their squares.
for number in range(1, 11):
    square = number**2
    print(number, '\t', square)     #  |t is like pressing the tab key


#%%

"""
In this case, the for loop is set up so that the numbers from 0 to 15 print out, 
but at a step of 3, so that only every third number is printed.
"""


for i in range(0,15,3):
   print(i)
   


#%%
"""We can also use a negative value for our step argument to iterate backwards, but we’ll have to
 adjust our start and stop arguments accordingly
 
 
 Here, 100 is the start value, 0 is the stop value, and -10 is the range, so the loop begins at 
    100 and ends at 0, decreasing by 10 with each iteration. We can see this occur in the output:
 
 """

for i in range(100,0,-10):
   print(i)
   
#%%
"""

User Controlled loop iterations 
"""


# This program uses a loop to display a
# table of numbers and their squares.

# Get the ending limit.
print('This program displays a list of numbers')
print('(starting at 1) and their squares.','\n')
end = int(input('How high should I go? '))
    
# Print the table headings.
print()
print('Number\tSquare')
print('--------------')

# Print the numbers and their squares.
for number in range(1, end + 1):
    square = number**2
    print(number, '\t', square)

#%%
# This program uses a loop to display a
# table of numbers and their squares.

# Get the starting value.
print('This program displays a list of numbers')
print('and their squares.')
start = int(input('Enter the starting number: '))

# Get the ending limit.
end = int(input('How high should I go? '))
   
# Print the table headings.
print()
print('Number\tSquare')
print('--------------')

# Print the numbers and their squares.
for number in range(start, end + 1):
    square = number**2
    print(number, '\t', square)


#%%


"""
Use a loop to track a running total
"""

# This program calculates the sum of a series
# of numbers entered by the user.

max = 5   # The maximum number

# Initialize an accumulator variable.
total = 0.0
   
# Explain what we are doing.
print('This program calculates the sum of')
print(max, 'numbers you will enter.')

# Get the numbers and accumulate them.
for counter in range(max):
    number = int(input('Enter a number: '))
    total = total + number

# Display the total of the numbers.
print('The total is', total)



#%%

"""

Sentinals 

A Sentinal is a special value that signals the end of the sequence within 
the loop and the loop should terminate.

"""
# This program displays property taxes.

TAX_FACTOR = 0.0065   # Represents the tax factor.

# Get the first lot number.
print('Enter the property lot number')
print('or enter 0 to end.')
lot = int(input('Lot number: '))

# Continue processing as long as the user
# does not enter lot number 0.
while lot != 0:
    # Get the property value.
    value = float(input('Enter the property value: '))

    # Calculate the property's tax.
    tax = value * TAX_FACTOR

    # Display the tax.
    print('Property tax: $', format(tax, ',.2f'), sep='')

    # Get the next lot number.
    print('Enter the next lot number or')
    print('enter 0 to end.')
    lot = int(input('Lot number: '))






#%%

"""
Input validation loops

An example of a nested loop

"""

# This program calculates retail prices.

mark_up = 2.5  # The markup percentage
another = 'y'  # Variable to control the loop.

# Process one or more items.
while another == 'y' or another == 'Y':
    # Get the item's wholesale cost.
    wholesale = float(input("Enter the item's " + \
                            "wholesale cost: "))

    # Validate the wholesale cost.
    while wholesale < 0:
        print('ERROR: the cost cannot be negative.')
        wholesale = float(input('Enter the correct ' + \
                                'wholesale cost:'))

    # Calculate the retail price.
    retail = wholesale * mark_up

    # Display the retail price.
    print('Retail price: $', format(retail, ',.2f'))


    # Do this again?
    another = input('Do you have another item? ' + \
                    '(Enter y for yes): ')



#%%


#%%

"""
Program: tidbit.py


Print a payment schedule for a loan to purchase a computer.

Input
   purchase price

Constants
   annual interest rate = 12%
   downpayment = 10% of purchase price
   monthly payment = 5% of purchase price
   
"""

ANNUAL_RATE = .12
MONTHLY_RATE = ANNUAL_RATE / 12


purchasePrice = float(input("Enter the puchase price: "))

monthlyPayment = .05 * purchasePrice
month = 1
balance = purchasePrice
print("Month  Starting Balance  Interest to Pay  Principal to Pay  Payment  Ending Balance")
while balance > 0:
    if monthlyPayment > balance:
        monthlyPayment = balance
        interest = 0
    else:
        interest = balance * MONTHLY_RATE
    principal = monthlyPayment - interest
    remaining = balance - monthlyPayment
    print("%2d%15.2f%15.2f%17.2f%17.2f%17.2f" % \
          (month, balance, interest, principal, monthlyPayment, remaining))
    balance = remaining
    month += 1
    



 
    
    


#%%




character = '#' # The symbol to print
numRows = 7     # The number of rows
space = ' '     # The space character

# Iterate over the rows.
for row in range(numRows):
    		
    # Each row includes 2 more columns
    # than the row number.
    for col in range(row + 2):
        
        # Print the symbol in the first
        # and last column.
        if col == 0 or col == row + 1:
            print(character, end='')
            
        # Add spaces between symbols.
        else:  
            print (space, end='')

    # Go to the next row.
    print()

#%%

#%%


"""
Activity #1

Write a program that averages test scores.   Ask the user for input on the number of 
and the number of tests per student. 

The output should display the average test score for that student.  You can go by student
number (1, 2, 3, etc. )


"""

#%%
def main():
    student_num = input('How many Students? ')
    test_num = input('How many tests per student?')


def get_scores():
    while student_num > 0
        

    student_num - 1
main()
   #%%
    
"""
ACTIVITY #2


Write a program that simulate the game of sevens until all funds are depleted.  Ask the user for input on 
number of dollars they have. 

1) Rules:
       roll two dice
       if the sum equals 7, win $4, else lose $1
2) The input is:
       the amount of money the user is prepared to lose 
3) Computations:
       use a random number generator to simulate rolling the dice
       loop until the funds are depleted 
       count the number of rolls
       keep track of the maximum amount
4) The outputs are:
       the number of rolls it takes to deplete the funds
       the maximum amount 
       
       You might consider importing random and using it as in the example below:

"""
#%%

"""

This code will help with this activity

"""

import random

dice = random.randint(1, 6)
print(dice)


#%%


# This program draws a design using repeated squares.
import turtle

# Named constants
NUM_SQUARES = 36    # Number of squares to draw
LINE_LENGTH = 200   # Length of each line
ANGLE_1 = 90        # Angle to turn after each side
ANGLE_2 = 10        # Angle to turn after each square
ANIMATION_SPEED = 0 # Animation speed

# Initialize the turtle.
turtle.speed(ANIMATION_SPEED)
turtle.hideturtle()

# Draw 36 squares, with the turtle tilted
# by 10 degrees after each square is drawn.
for x in range(NUM_SQUARES):
    turtle.forward(LINE_LENGTH)   # First side
    turtle.left(ANGLE_1)
    turtle.forward(LINE_LENGTH)   # Second side
    turtle.left(ANGLE_1)
    turtle.forward(LINE_LENGTH)   # Third side
    turtle.left(ANGLE_1)
    turtle.forward(LINE_LENGTH)   # Fourth side
    turtle.left(ANGLE_1)
    turtle.left(ANGLE_2)    



      # Angle for next square

#%%


import turtle

# Named constants
STARTING_X = -4
STARTING_Y = 4
STARTING_SIZE = 8
NUM_SQUARES = 50
STEP = 2
NUM_SIDES = 4
ANGLE = 90
ANIMATION_SPEED = 0

turtle.speed(ANIMATION_SPEED)
turtle.hideturtle()

x = STARTING_X
y = STARTING_Y
size = STARTING_SIZE

for count in range(2, 100, 2):
    # Position the turtle.
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    
    # Draw the square
    for s in range(NUM_SIDES):
        turtle.forward(size)
        turtle.right(ANGLE)

    # Prepare for the next square.
    x = x - 4
    y = y + 4
    size = size + 4
    
    #%%
    
    
    
    # This program draws a design using repeated circles.
import turtle

# Named constants
NUM_CIRCLES = 36    # Number of circles to draw
RADIUS = 25         # Radius of each circle
ANGLE = 10          # Angle to turn
ANIMATION_SPEED = 0 # Animation speed

# Set the animation speed.
turtle.speed(ANIMATION_SPEED)

# Draw the center of the flower as 36 circles, with the
# turtle tilted by 10 degrees after each circle is drawn.
for x in range(NUM_CIRCLES):
    turtle.circle(RADIUS)
    turtle.left(ANGLE)

# Reposition the turtle.
turtle.penup()
turtle.goto(0,0)
turtle.setheading(0)

# Draw the petals.
for x in range(36):
    turtle.forward(RADIUS * 2)
    turtle.pendown()
    turtle.left(25)
    turtle.forward(100)
    turtle.right(90)

    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.penup()
    turtle.goto(0,0)




#%%



import turtle

# Named constants
ANIMATION_SPEED = 0
NUM_LINES = 50
STARTING_LENGTH = 1
ENDING_LENGTH = 500
STEP = 10
ANGLE = 90

#Initialize the turtle.
turtle.hideturtle()
turtle.speed(ANIMATION_SPEED)

# Draw the lines.
for x in range(STARTING_LENGTH, ENDING_LENGTH, STEP):
    turtle.forward(x)
    turtle.left(ANGLE)


#%%
"""
Challenge Activity # 3

 See if you can create a design using Turtle Graphics
 
 Try to make an interesting design,   you should be able to turn in something.

"""
   
