"""
Course Number: ENGR 13300
Semester: Fall 2024

Description:
    Replace this line with a description of your program.

Assignment Information:
    Assignment:     7.2.3 - py3 team 3 a
    Team ID:        022-11
    Author:         Grant Stevenson, steve395@purdue.edu
    Author:         Ankur Raghavan, raghav21@purdue.edu
    Author:         , @purdue.edu
    Date:           09/17/2024

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

from py3_team_2_b_11 import my_factorial
import math as m

def main():
    # take inputs
    n = int(input(f"Enter the value of n: "))
    x = float(input(f"Enter the value of x: "))


    actual_value = 0
    # add each term in the series 
    for i in range(n+1): 
        actual_value += ((x ** (i))/ my_factorial(i)) 
    
    # calculate real value of e^x
    e = (m.e) ** x

    # calculate percent error
    percent_error = ((actual_value - e) / e) * 100
    
    # print outputs
    print(f"Actual value: {e:.2f}")
    print(f"Approximate value: {actual_value:.2f}")
    print(f"Error: {percent_error:.1f}%")


if __name__ == "__main__":
    main()
