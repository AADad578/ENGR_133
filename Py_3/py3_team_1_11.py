"""
Course Number: ENGR 13300
Semester: Fall 2024

Description:
    works with arrays and loops

Assignment Information:
    Assignment:     7.1.2 Py3 Pre Class Task 0
    Team ID:        022-11
    Author:         Ankur Raghavan, raghav21@purdue.edu
    Date:           9/12/2024

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

import numpy as np


def main():
    # define the array
    x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print("FOR loop:")
    # loop using i as iterative variable
    for i in range(len(x)):
        # loop using j as iterative variable
        for j in range(len(x[i])):
            # print values
            print(f"X[{i},{j}] = {x[i][j]}")
    
    print("WHILE loop:")
    i=0
    j=0
    # loop using i as iterative variable
    while (i < len(x)):
        # loop using j as iterative variable
        while (j<len(x[i])):
            # print values
            print(f"X[{i},{j}] = {x[i][j]}")
            # iterate j
            j+=1
        # iterate i and reset j
        i+=1
        j=0

if __name__ == "__main__":
    main()
