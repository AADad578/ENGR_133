"""
Course Number: ENGR 13300
Semester: Fall 2024

Description:
    Completes the equations given

Assignment Information:
    Assignment:     6.1.2 Py2 Pre 1
    Team ID:        022 - 11 (e.g. LC1 - 01; for section LC1, team 01)
    Author:         Ankur Raghavan, raghav21@purdue.edu
    Date:           9/9/2024

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

import math

def calc_perform(a,b,c):
    # if a is above 4
    if a>=4:
        # perform the given equation
        ans = (a - b + math.sin(c)) / (a * c)
    # otherwise
    else:
        # perform the other equation
        ans = (math.tan(c)) / (a - ((a * c) / b))
    # return the answer
    return ans

def main():
    # take input for the value of a and convert to a float
    a = float(input("Input a number for variable a (can be negative): "))
    # set the values of b and c
    b = 20
    c = 47
    # perform the calculation
    ans = calc_perform(a,b,c)
    # print the result
    print(f"The result of the function was {ans:.2f}")


if __name__ == "__main__":
    main()
