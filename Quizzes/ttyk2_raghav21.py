"""
Course Number: ENGR 13300
Semester: Fall 2024

Description:
    Prompt the user to enter the x and y coordinates of a point and then
    display a figure window with a shape and the entered point and print the
    location of the point.

Assignment Information:
    Assignment:     TTYK #2
    Team ID:        022-11
    Author:         Ankur Raghavan, raghav21@purdue.edu
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

import matplotlib.pyplot as plt
import math as m
import numpy as np

def main():
    # Define the radius of the circle
    radius = 5.5  # x-axis and y-axis dimensions


    # Define the points for plotting the circle
    theta = np.linspace(0, 2 * np.pi, 100)
    x_circle = radius * np.cos(theta)
    y_circle = radius * np.sin(theta)

    fig, ax = plt.subplots()
    ax.plot(x_circle, y_circle) 
    ax.plot([0, 0], [-radius - 1, radius + 1], dashes=[4, 4])  
    ax.plot([-radius - 1, radius + 1], [0, 0], dashes=[4, 4])  
    ax.set_title('Circle Center at Origin')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    # plotting the shape of the figure

    # input coordinates 
    x = float(input("Enter the x value: "))
    y = float(input("Enter the y value: "))

    # plot the point on the graph to show
    ax.plot(x, y, "o")
    ax.annotate(f"({x}, {y})", (x, y), xytext=(0, 5), textcoords='offset points', ha='center', va='bottom')

    # Set equal aspect ratio so the circle is not distorted
    ax.set_aspect('equal')

    # Calculate the distance of the point (x, y) from the origin (radius vector)
    d = m.sqrt(x**2 + y**2)

    if d>radius:
        print("Outside")
    elif d==radius:
        print("On the line")
    elif x>0 and y>0:
        print("Inside Q1")
    elif x>0 and y<0:
        print("Inside Q4")
    elif x<0 and y<0:
        print("Inside Q3")
    elif x<0 and y>0:
        print("Inside Q2")
    else:
        print("On an axis")

    # Label the quadrants
    ax.text( radius / 2,  radius / 2, 'Q1', fontsize=12, ha='center', va='center', color='purple')  # Quadrant 1
    ax.text( radius / 2, -radius / 2, 'Q4', fontsize=12, ha='center', va='center', color='purple')  # Quadrant 4
    ax.text(-radius / 2, -radius / 2, 'Q3', fontsize=12, ha='center', va='center', color='purple')  # Quadrant 3
    ax.text(-radius / 2,  radius / 2, 'Q2', fontsize=12, ha='center', va='center', color='purple')  # Quadrant 2

    plt.show()

    # remember to close the figure window to rerun the code

if __name__ == "__main__":
    main()