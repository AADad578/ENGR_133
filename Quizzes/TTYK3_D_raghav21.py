"""
Course Number: ENGR 13300
Semester: Fall 2024

Description: 
This program initializes a file name and calls the read_data function from the
TTYK3_fun file. The read_data function reads the data from the file and returns
it as a numpy array. The program extracts specific rows and columns from the
data and performs operations on them. The program uses flowchart logic to
determine the operations to be performed. The program prints the results of
these operations.    

Assignment Information:
    Assignment:     TTYK #3
    Team ID:        022-11
    Author:         Ankur Raghavan, raghav21@purdue.edu       
    Date:           10/02/2024

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
from TTYK3_fun import read_data
import numpy as np

def main():

    # Initialize the file name
    file_name = 'data_D.csv'

    # Call the read_data function
    data = read_data(file_name)

    ###############################################################################################
    # Complete this function according to the logic represented in the flowchart.
    ###############################################################################################
    data = data[:20, 51]
    sum = 0
    for item in data:
        sum += item
    print(sum)












    ###############################################################################################
    
if __name__ == '__main__':
    main()
