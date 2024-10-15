"""
Course Number: ENGR 13300
Semester: Fall 2024

Description:
    This function reads data from a file and returns it as a numpy array.
    
Assignment Information:
    Assignment:     e.g. TTYK #3
    Team ID:        ### - ## (e.g. 011 - 01; for section 11, team 01)
    Author:         Name, login@purdue.edu  
    Date:           10/3/2024

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

########################################################################################
# add the function definition here
########################################################################################
def read_data(file_in):
    """
    This function reads data from a file and returns it as a numpy array.

    Parameters:
    file_in (string): The name of the file to read from.

    Returns:
    data_out (numpy array): The data from the file as a numpy array.
    """
    # Initialize the data_in list
    data_in = []

    # Open the file as read only using the with context manager
    with open(file_in, 'r') as file:

        # Iterate through each line in
        for line in file:

            # Split the line into a list of integers and append to data_in
            row = list(map(int, line.strip().split(',')))

            # Append the row to data_in
            data_in.append(row)

    # Convert the data_in list to a numpy array
    data_out = np.array(data_in)
    return data_out
########################################################################################
# add the function return here
########################################################################################
