"""
Course Number: ENGR 13300
Semester: Fall 2024

Description:
    Finds the minimum number of terms that function requires to reach a specified accuracy

Assignment Information:
    Assignment:     7.2.3 Py3 Team 3 b
    Team ID:        022-11
    Author:         Ankur Raghavan, raghav21@purdue.edu
    Author:         Grant Stevenson, steve395@purdue.edu
    Author:         , @purdue.edu
    Date:           09/19/2024

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
import sys

from py3_team_2_b_11 import my_factorial


def main():
    #inputs
    x = float(input("Enter the value of x: "))
    target = float(input("Enter the target error threshold: "))/100.0
    
    #find the true value
    trueValue = (math.e**x)
    
    #initalize the number of terms, the percent error, and the output
    n=0
    error = sys.maxsize
    output = 0
    
    # repeat until the error is below the target
    while(error > target):
        #increase the number of terms
        n+=1
        output = 0
        
        # add each term in the series to the output
        for i in range(n):
            output += (x**i)/(my_factorial(i))
        
        #calculate percent error
        error = (trueValue - output)/trueValue
    
    # print outputs 
    print(f"Terms needed: {n}")
    print(f"Actual value: {trueValue:.2f}")
    print(f"Approximate value: {output:.2f}")
    print(f"Target error threshold: {target*100:.1f}%")


if __name__ == "__main__":
    main()
