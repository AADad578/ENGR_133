"""
Course Number: ENGR 13300
Semester: Fall 2024

Description:
    plot values in a scatter plot from a csv

Assignment Information:
    Assignment:     8.1.2 Py4 Pre 1
    Team ID:        022-11
    Author:         Ankur Raghavan, raghav21@purdue.edu
    Date:           9/19/2024

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

import csv
import math
import time
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def main():
    x,y = [],[]
    #open the file
    with open('py4_pre_task0_data.csv',newline='') as csvfile:
        #create a reader obejct to read the file
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader: 
            #add each item to the corresponding list, multiply y axis by 4
            x.append(int(row[0]))
            y.append(int(row[1])*4)

    #make the scatter plot
    plt.scatter(x,y)
    plt.xlabel("Time (s)")
    plt.ylabel("Original Data *4")
    plt.title("Py4_Pre_1_data")
    #write the new csv file
    with open('py4_pre_1_raghav21.csv', 'w',newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        for i in range(len(x)):
            #write each row with the x and y
            writer.writerow([x[i], y[i]])
            
    plt.show()

if __name__ == "__main__":
    main()
