"""
Course Number: ENGR 13300
Semester: Fall 2024

Description:
    Prompt the user to enter the x and y coordinates of a point and then display a
    figure window with a shape within a shape and the entered point and print the
    location of the point.

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

import matplotlib.pyplot as plt

from CQ2_utils import (
    get_location_in_rectangle,
    get_location_in_circle,
    get_location_in_triangle,
    add_rectangle,
    add_circle,
    add_triangle,
    label_rectangle_sectors,
    label_circle_sectors,
    label_triangle_sectors,
)

########################################################################################
# Include your imports here. No other parts of this file should be modified.
########################################################################################
from CQ2_D_fun_raghav21 import classify_point

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


def main():

    # Get the user's input
    location_number = int(input("Enter the inner shape location number: "))
    user_x = float(input("Enter the x-coordinate: "))
    user_y = float(input("Enter the y-coordinate: "))

    # Define the parameters of the shapes
    outer_shape = 'triangle'
    inner_shape = 'triangle'

    fig, ax = plt.subplots()
    ax.set_aspect('equal')

    # Plot the outer shape
    outer_labels = ['D5', 'D6', 'D7', 'D8']
    if outer_shape == 'rectangle':
        x, y = get_location_in_rectangle(location_number, OUTER_WIDTH, OUTER_DEPTH)
        add_rectangle(ax, 0, 0, OUTER_WIDTH, OUTER_DEPTH)
        label_rectangle_sectors(ax, outer_labels, 0, 0, OUTER_WIDTH, OUTER_DEPTH)
    elif outer_shape == 'circle':
        x, y = get_location_in_circle(location_number, OUTER_RADIUS)
        add_circle(ax, 0, 0, OUTER_RADIUS)
        label_circle_sectors(ax, outer_labels, x, y, OUTER_RADIUS)
    else:
        x, y = get_location_in_triangle(location_number, OUTER_BASE, OUTER_HEIGHT)
        add_triangle(ax, 0, 0, OUTER_BASE, OUTER_HEIGHT)
        label_triangle_sectors(ax, outer_labels, x, y, OUTER_BASE, OUTER_HEIGHT)

    # Plot the inner shape
    inner_labels = ['D1', 'D2', 'D3', 'D4']
    if inner_shape == 'rectangle':
        add_rectangle(ax, x, y, INNER_WIDTH, INNER_DEPTH)
        label_rectangle_sectors(ax, inner_labels, x, y, INNER_WIDTH, INNER_DEPTH)
    elif inner_shape == 'circle':
        add_circle(ax, x, y, INNER_RADIUS)
        label_circle_sectors(ax, inner_labels, x, y, INNER_RADIUS)
    else:
        add_triangle(ax, x, y, INNER_BASE, INNER_HEIGHT)
        label_triangle_sectors(ax, inner_labels, x, y, INNER_BASE, INNER_HEIGHT)

    # Plot the vertical and horizontal lines
    ax.axhline(y, color='gray', linestyle='--')
    ax.axvline(x, color='gray', linestyle='--')

    # Plot the user's point
    ax.scatter(user_x, user_y, color='red', s=30)

    # Classification of the point's location
    classification = classify_point(x, y, user_x, user_y)

    ax.set_title(
        f"{inner_shape} in {outer_shape} at Location {location_number} "
        f"with Coordinates ({user_x},{user_y}): {classification}"
    )

    plt.show()

if __name__ == '__main__':
    main()