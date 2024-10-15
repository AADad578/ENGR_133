"""
Course Number: ENGR 13300
Semester: e.g. Fall 2024

Description:
    This program takes in 3 values and returns the values of three math functions rounded to 4 decimal places 

Assignment Information:
    Assignment:     5.1.2 Py1 Pre 1 
    Team ID:        022 - 17 
    Author:         Ankur Raghavan, raghav21@purdue.edu
    Date:           9/1/2024

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

from math import sin,pi,factorial,asin

def main():
    a = 5
    b = 9
    c = 2
    
    # 1.
    print("equation 1: " + str(round(
        a * (b**2) + sin(c), 4
    )))
    
    # 2.
    print("equation 2: " + str(round(
        (pi/c) - factorial(b), 4
    )))
    
    # 3.
    print("equation 3: " + str(round(
        b**3 + (c/4.0) + asin(1), 4
    )))


if __name__ == "__main__":
    main()
