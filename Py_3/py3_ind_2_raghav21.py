"""
Course Number: ENGR 13300
Semester: Fall 2024

Description:
    calculates an approximation of (sin x)/x over the interval [a,b]

Assignment Information:
    Assignment:     e.g. 5.2.1 Py1 Team 1 (for Python 1 Team task 1)
    Team ID:        ### - ## (e.g. LC1 - 01; for section LC1, team 01)
    Author:         Name, login@purdue.edu
    Date:           e.g. 08/29/2024

Contributors:
    Name, login@purdue [repeat for each]

    My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor here as well.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

""" Write any import statements here (and delete this line)."""


import math


def main():
    limLow = float(input("Enter the lower limit of integration: "))
    limHigh = float(input("Enter the upper limit of integration: "))
    precision = input("Enter the number of decimal places for convergence: ")
    # check for valid input
    try:
        precision = int(precision) # will throw ValueError if not integer
        if precision <= 0:
            raise ValueError # throw ValueError if less than 0
    except ValueError: #catch all ValueError and show custom error message
        print("Error: Input a positive integer")
        return # end program
    
    # check for valid input
    terms = input("Enter the maximum number of terms: ")
    try:
        terms = int(terms) # will throw ValueError if not integer
        if terms <= 0:
            raise ValueError # throw ValueError if less than 0
    except ValueError: #catch all ValueError and show custom error message
        print("Error: Input a positive integer")
        return # end program
        
    print("Approximations: ")
    count = 0
    approx = 0
    for i in range(terms): # approx = high - low
        lastRounded = round(approx, precision) # save value before this term
        approx += ( limHigh ** (2*i+1) ) / ( (2*i+1) * math.factorial(2*i+1) ) * ((-1)**i) #calc high and add
        approx -= ( limLow ** (2*i+1) ) / ( (2*i+1) * math.factorial(2*i+1) ) * ((-1)**i) #calc low and subtract
        
        rounded = round(approx, precision)
        print(f"n = {i}: sum = {rounded}")
        
        count = count+1 if lastRounded==rounded else 0 # add to the counter if it is the same as last time or reset it if not
        if count == 2: # if it is the third value in a row, finish the program
            print(f"The integral from {limLow} to {limHigh} is estimated to be {rounded}.")
            print(f"Total number of terms: {i+1}")
            return
    # if it doesn't finish before now it didn't converge and return the error
    print(f"Error: The approximation did not converge to {precision} decimal places with only {terms} terms.")
    
            
        
        


if __name__ == "__main__":
    main()
