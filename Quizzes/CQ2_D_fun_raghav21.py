"""
Course Number: ENGR 13300
Semester: Fall 2024

Description:
    This file contains the function `classify_point`, which classifies a point based on
    its location relative to the outer shape and the inner shape.

Assignment Information:
    Assignment:     CQ #2
    Team ID:        022-11
    Author:         Ankur Raghavan, raghav21@purdue.edu
    Date:           09/26/2024

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

########################################################################################
# Import the function(s) you need from CQ2_utils.py here.
########################################################################################
from CQ2_utils import outside_of_triangle




# Shape Parameters
# Rectangle
OUTER_WIDTH, OUTER_DEPTH = 18, 12
INNER_WIDTH, INNER_DEPTH = 6, 4
# Circle
OUTER_RADIUS = 15
INNER_RADIUS = 2
# Triangle
OUTER_BASE, OUTER_HEIGHT = 45, 45
INNER_BASE, INNER_HEIGHT = 12, 12


def classify_point(x, y, user_x, user_y):
    """
    Classifies a point based on its location relative to the outer shape and the
    inner shape.

    Parameters:
        x : The x-coordinate of the center of the shape.
        y : The y-coordinate of the center of the shape.
        user_x : The x-coordinate of the user's point.
        user_y : The y-coordinate of the user's point.

    Returns:
        str: The location of the user's point.
    """
    
    if user_x == x and user_y == y:
        return 'Intersection'

    if user_x == x:
        return 'Vertical Line'

    if user_y == y:
        return 'Horizontal Line'
    
    if outside_of_triangle(user_x, user_y, 0, 0, OUTER_BASE, OUTER_HEIGHT):
        return 'Outside'

    ####################################################################################
    # Complete this function according to the logic represented in the flowchart.
    ####################################################################################
 
    # D is 1-4 if it is inside the triangle and 5-8 if outside
    # set D equal to the lowest value in the range
    d = 5 if outside_of_triangle(user_x, user_y,x,y, INNER_BASE, INNER_HEIGHT) else 1
    if user_y>y: #d = 1 or 5
        # if it is more than the y it can either be 1/2 or 5/6 so don't add anything
        #add 1 if user x is not more than x to get either 2 or 6
        d += 0 if user_x>x else 1 
    else: #d= 1 or 5
        # if it is less than the y it can either be 3/4 or 7/8 so add at least 2 
        # add 1 more if user x is not less than x to get either 4 or 8
        d += 2 if user_x<x else 3
    return f"Inside D{d}" #return the value
















 
    ####################################################################################