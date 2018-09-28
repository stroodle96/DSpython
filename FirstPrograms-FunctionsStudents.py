
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 17:06:03 2018

@author: John Stewart
"""

# First Programs and Functions -*-

"""
Simple Programs and Computations
Python Basics
Numeric Datatypes
Arithmetic operations 
variables, expressions, and statements
input statements



"""
"""

We will mainly use the following window panes: IPython Console, Editor, 
File Explorer, and Object Inspector.



#%% breaks up the Editor document into cells. 

The green triangle in the tool 
bar executes the entire file (after saving it), Ctrl-Enter (Command-Return on a
Mac) executes only the cell that the cursor is in (but does not save). 

Instructions on changing working directory in Spyder: 
    
At the top on the right you will see a path, the working directory. To its right is a file 
folder. 

Click it and you can change the working directory. When you do, you 
can click the icon to the right of that and set that path as the IPython 
console's new working directory. 

Then all the panes: Editor, IPython Console, 
and File Explorer are pointed to this current working directory. 

In the more 
recent versions of Spyder, this button has been eliminated and the editor and 
IPython console are automatically set to the current working directory. 
"""


#%%
"""A Simple Function"""

def hello():
    """ prints hello, world """
    print("Hello, world!")
    
    
    #%%
"""Variable Assignment """
   
    # Create two variables: top_speed and distance.
top_speed = 160
distance = 300

# Display the values referenced by the variables.
print('The top speed is')
print(top_speed)
print('The distance traveled is')
print(distance)
    
#%% 
#Example of another funtion
def areacircle(radius):
    """ Computes the area of a circle of the given radius """
    area = 3.14*radius**2
    print("The area of a circle of radius",radius,"is", area)

#%%

"""
ACTIVITY 1:
    
Compute the area of a Triangle 

Write a function called triangArea to compute the area
of a triangle: formula is area = .5*b*h.

Output should look like:
The area of a triangle of base 3 and height 5 is 7.5

You can test your function by executing the following code:
"""
def triangArea(b,h):
    area = b*h*.5
    print("The area of a triangle with a height of",h,"and a base of" ,b,"is ", area,".")
    
#%%
# The following will test areatriangle()
#triangArea(3,5)
#triangArea(2,20)
 
 

#%%


def mi_km(miles):
        km = miles * 1.60934
        print(miles, "miles", "is equal to", km, "kilometers")
    
        """
Convert miles to kilometers 
1 mile = 1.60934 km 


ACTIVITY 2:
    
WRITE A FUNCTION TO CONVERT KILOMETERS TO MILES

"""

def km_mi(km):
    miles = km *0.621371
    print(km, "Kilometers", "is equal to", miles, "Miles"

#%%

def fahrenheit_to_celsius(temp):
    """ Converts Fahrenheit temperature to Celsius. 
        Formula is 5/9 of temp minus 32 """
    # Note that this line is not executed
    # end='' keeps print from starting a new line.
    newTemp = 5*(temp-32)/9
    print("The Fahrenheit temperature",temp,"is equivalent to",newTemp,end=' ')
    print(" degrees Celsius")
    
    """
    end=' ' eliminates the print statement carrying over to 2 lines.  This addition will 
    print a blank and keep the statement on one line
    """
    
#%%

"""
ACTIVITY 3:
    
Write a function 'def celsius_to_fahrenheit' to convert Celsius
to Fahrentheit temperature. The formula is (9/5) times temp plus 32. 
Print the output in the form:
The Celsius temperature 50.0 is equivalent to 122.0 degrees Fahrenheit.
"""

#%%
"""
Solution:
"""
#%%

 
    
    
# Use the following will test the above function

celsius_to_fahrenheit(100)
celsius_to_fahrenheit(0)
celsius_to_fahrenheit(50.)



#%%
"""
We can write a function that takes input directly from the keyboard
"""

def name():
    """ Input first and last name, combine to one string and print """
    fname = input("Enter your first name: ")
    lname = input("Enter your last name: ")
    fullname = fname + " " + lname

    print("Your name is:", fullname)
    

#%% 
"""
ACTIVITY 4:
    
Add to the above name function  to include the city and state where you live.
That is, ask two more questions to get the city and the state you live in.

Your run should look like the following (even if this is not the customary
way in your country):
    
    
Enter your first name: John 

Enter your last name: Stewart

Enter the city you live in: Apollo

Enter the state you live in: PA
Your name is: John Stewart
You live in:  Apollo,PA

"""

