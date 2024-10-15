"""
Course Number: ENGR 13300
Semester: Fall 2024

Description:
    This file contains utility functions to check if a point is outside of a
    rectangle, circle, or triangle; functions to get the location of a point in
    a rectangle, circle, or triangle based on the location number; functions to
    add a rectangle, circle, or triangle to a figure window; and functions to
    label the sectors of the shapes.  

    ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    YOU DO NOT NEED TO EDIT THIS FILE FOR THE PURPOSES OF THIS QUIZ.
    ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized source, either
    modified or unmodified; nor have I provided another student access to my
    code.  The project I am submitting is my own original work.
"""

import math

import matplotlib.pyplot as plt
import numpy as np


def outside_of_rectangle(user_x, user_y, center_x, center_y, width, depth):
    """
    Function to check if a point is outside of a rectangle.

    Parameters:
        user_x: x-coordinate of the point.
        user_y: y-coordinate of the point.
        center_x: x-coordinate of the center of the rectangle.
        center_y: y-coordinate of the center of the rectangle.
        width: width of the rectangle.
        depth: depth of the rectangle.

    Returns:
        True if the point is outside of the rectangle, False otherwise.
    """

    outer_x_min = center_x - width / 2
    outer_x_max = center_x + width / 2
    outer_y_min = center_y - depth / 2
    outer_y_max = center_y + depth / 2

    if user_x < outer_x_min or user_x > outer_x_max or user_y < outer_y_min or user_y > outer_y_max:
        return True
    return False


def outside_of_circle(user_x, user_y, center_x, center_y, radius):
    """
    Function to check if a point is outside of a circle.

    Parameters:
        user_x: x-coordinate of the point.
        user_y: y-coordinate of the point.
        center_x: x-coordinate of the center of the circle.
        center_y: y-coordinate of the center of the circle.
        radius: radius of the circle.

    Returns:
        True if the point is outside of the circle, False otherwise.
    """

    if (user_x - center_x) ** 2 + (user_y - center_y) ** 2 > radius ** 2:
        return True
    return False


def outside_of_triangle(user_x, user_y, center_x, center_y, base, height):
    """
    Function to check if a point is outside of a triangle.

    Parameters:
        user_x: x-coordinate of the point.
        user_y: y-coordinate of the point.
        center_x: x-coordinate of the center of the triangle.
        center_y: y-coordinate of the center of the triangle.
        base: base of the triangle.
        height: height of the triangle.

    Returns:
        True if the point is outside of the triangle, False otherwise.
    """

    slope = 2 * height / base

    x2, y2 = center_x + base / 2, center_y - height / 2
    x3, y3 = center_x - base / 2, center_y - height / 2

    y_rt = -slope * (user_x - x2) + y2
    y_lt = slope * (user_x - x3) + y3

    if user_y > y_rt or user_y > y_lt or user_y < center_y - height / 2:
        return True
    return False



def get_location_in_rectangle(location, width, height):
    """
    Function to get coordinates of a point in a rectangle based on the location number.

    Parameters:
        location (int): The location number of the inner shape (1-9)

    Returns:
        The x and y coordinates of the center of the inner shape
    """

    # Dictionary to store the location of the inner rectangle
    locations = {
        1: (-width / 4, height / 4),
        2: (0, height / 4),
        3: (width / 4, height / 4),
        4: (-width / 4, 0),
        5: (0, 0),
        6: (width / 4, 0),
        7: (-width / 4, -height / 4),
        8: (0, -height / 4),
        9: (width / 4, -height / 4),
    }

    x, y = locations[location]
    return x, y  # Return the center of the inner shape


def get_location_in_circle(location, radius):
    """
    Function to get coordinates of a point in a circle based on the location number.

    Parameters:
        location (int): The location number of the inner shape (1-9)

    Returns:
        The x and y coordinates of the center of the inner shape
    """

    # Dictionary to store the center of the inner circle based on the location number
    locations = {
        1:  (-radius / 3, radius / 3),
        2:  (0, radius / 2),
        3:  (radius / 3, radius / 3),
        4:  (-radius / 2, 0),
        5:  (0, 0),
        6:  (radius / 2, 0),
        7:  (-radius / 3, -radius / 3),
        8:  (0, -radius / 2),
        9:  (radius / 3, -radius / 3),
    }

    x, y = locations[location]
    return x, y  # Return the center of the inner shape


def get_location_in_triangle(location, base, height):
    """
    Function to get coordinates of a point in a triangle based on the location number.

    Parameters:
        location (int): The location number of the inner shape (1-10)

    Returns:
        The x and y coordinates of the center of the inner shape
    """

    # Dictionary to store the center of the inner triangle based on the location number
    locations = {
        1:  (0 * (-base /  6) , 2 * ( height / 12)),
        2:  (1 * (-base / 18) , 1 * ( height / 12)), 
        3:  (1 * ( base / 18) , 1 * ( height / 12)), 
        4:  (1 * (-base / 15) , 1 * (-height /  6)),   
        5:  (0 * ( base /  4) , 1 * (-height /  6)), 
        6:  (1 * ( base / 15) , 1 * (-height /  6)), 
        7:  (2 * (-base / 12) , 2 * (-height /  6)),   
        8:  (1 * (-base / 18) , 2 * (-height /  6)), 
        9:  (1 * ( base / 18) , 2 * (-height /  6)),
        10: (2 * ( base / 12) , 2 * (-height /  6))
    }

    x, y = locations[location]
    return x, y  # Return the center of the inner shape


def add_rectangle(ax, x_center, y_center, width, height):
    x_min = x_center - width / 2
    x_max = x_center + width / 2
    y_min = y_center - height / 2
    y_max = y_center + height / 2
    ax.add_patch(
        plt.Rectangle((
            x_min, y_min),
            x_max - x_min,
            y_max - y_min,
            fill=False,
            edgecolor='black'
        )
    )


def add_circle(ax, center_x, center_y, radius):
    ax.add_patch(
        plt.Circle(
            (center_x, center_y),
            radius,
            fill=False,
            edgecolor='black'
        )
    )


def add_triangle(ax, center_x, center_y, base, height):
    ax.add_patch(
        plt.Polygon(
            [
                (center_x, center_y + height / 2),
                (center_x + base / 2, center_y - height / 2),
                (center_x - base / 2, center_y - height / 2),
            ],
            fill=False,
            edgecolor='black'
        )
    )



def label_rectangle_sectors(ax, labels, x, y, width, depth):

    if width > 10:
        # Label the quadrants of the outer rectangle
        ax.text( width / 2,  depth / 2, "Q5", ha='right', va='top')  
        ax.text(-width / 2,  depth / 2, "Q6", ha='left' , va='top') 
        ax.text(-width / 2, -depth / 2, "Q7", ha='left' , va='bottom')  
        ax.text( width / 2, -depth / 2, "Q8", ha='right', va='bottom') 
        return

    # Label the quadrants of the inner rectangle
    x1, y1 = x - width / 4, y - depth / 4
    x2, y2 = x + width / 4, y + depth / 4
    ax.text(x2, y2, "Q1", ha='center', va='center') 
    ax.text(x1, y2, "Q2", ha='center', va='center')  
    ax.text(x1, y1, "Q3", ha='center', va='center')  
    ax.text(x2, y1, "Q4", ha='center', va='center')  



def label_circle_sectors(ax, labels, x, y, radius):

    if radius < 10:
        # Label the inner circle sectors
        for index, mid_angle in enumerate([45, 135, 225, 315]):
            mid_angle = np.radians(mid_angle)
            factor = radius / 1.5
            adjusted_x = x + factor * np.cos(mid_angle)
            adjusted_y = y + factor * np.sin(mid_angle)
            ax.text(adjusted_x, adjusted_y, labels[index], va='center', ha='center')
        return

    bisector_length = 50

    # General case for 45 and 135 degrees
    for angle_deg in [45, 135]:
        angle_rad = np.radians(angle_deg)
        
        delta_x = bisector_length * np.cos(angle_rad)
        delta_y = bisector_length * np.sin(angle_rad)
        endpoint_x = x + delta_x
        endpoint_y = y + delta_y
        
        slope = (endpoint_y - y) / (endpoint_x - x)
        intercept = y - slope * x
        
        a = 1 + slope**2
        b = 2 * slope * intercept
        c_val = intercept**2 - radius**2
        
        discriminant = b**2 - 4*a*c_val
        
        if discriminant >= 0:
            x1 = float((-b + np.sqrt(discriminant)) / (2 * a))
            x2 = float((-b - np.sqrt(discriminant)) / (2 * a))
            y1 = float(slope * x1 + intercept)
            y2 = float(slope * x2 + intercept)
            
            factor = radius - 1.5
            if angle_deg == 45:
                angle = np.arctan2(y1, x1)
                adjusted_x = factor * np.cos(angle)
                adjusted_y = factor * np.sin(angle)
                ax.text(adjusted_x, adjusted_y, labels[0])

                angle = np.arctan2(y2, x2)
                adjusted_x = factor * np.cos(angle)
                adjusted_y = factor * np.sin(angle)
                ax.text(adjusted_x, adjusted_y, labels[2])

            elif angle_deg == 135:
                angle = np.arctan2(y1, x1)
                adjusted_x = factor * np.cos(angle)
                adjusted_y = factor * np.sin(angle)
                ax.text(adjusted_x, adjusted_y, labels[3])

                angle = np.arctan2(y2, x2)
                adjusted_x = factor * np.cos(angle)
                adjusted_y = factor * np.sin(angle)
                ax.text(adjusted_x, adjusted_y, labels[1], va='center', ha='center')



def label_triangle_sectors(ax, labels, x, y, base, height):

    # Calculate the mid angle between the bisector angles
    mid_angle = [45, 135, 225, 315]

    outer = False
    if base > 20:
        outer = True
        V1 = (0, 0 + height / 2)
        V2 = (0 + base / 2, 0 - height / 2)
        V3 = (0 - base / 2, 0 - height / 2)
    else:
        V1 = (x, y + height / 2)
        V2 = (x + base / 2, y - height / 2)
        V3 = (x - base / 2, y - height / 2)
    V = [V3, V2, V1]

    triangle_edges = [(V[i], V[(i + 1) % len(V)]) for i in range(len(V))]

    # Initialize the final label positions
    label_positions_final = []

    for angle in mid_angle:

        # Convert the angle to radians and calculate the direction vector
        rad = np.radians(angle)

        # Direction vector from the bisector origin
        direction_x = np.cos(rad)
        direction_y = np.sin(rad)

        # Initialize variables to track the closest intersection
        closest_intersection = None
        min_distance = float('inf')  

        # Check intersection with all triangle edges (AB, BC, CA)
        for p1, p2 in triangle_edges:
            edge_vec = p2[0] - p1[0], p2[1] - p1[1]

            # Calculate the denominator for the intersection calculation
            denom = (edge_vec[0] * direction_y) - (edge_vec[1] * direction_x)

            # Check if lines are not parallel
            if denom != 0:
                # Calculate t using the derived formula manually verified
                t = ((p1[0] - x) * (p1[1] - p2[1]) - (p1[1] - y) * (p1[0] - p2[0])) / denom

                # Check if the intersection point is within the edge segment
                if t >= 0:
                    # Calculate the exact intersection coordinates
                    x_intersection = x + t * direction_x
                    y_intersection = y + t * direction_y
                    
                    # Calculate distance from bisector origin
                    distance = math.sqrt((x_intersection - x) ** 2 + (y_intersection - y) ** 2)
                    
                    # Update the closest intersection point
                    if distance < min_distance:
                        min_distance = distance
                        closest_intersection = (round(x_intersection, 2), round(y_intersection, 2))

        # If an intersection point was found, calculate the final label position
        if closest_intersection is not None:
            x_intersection, y_intersection = closest_intersection
            direction_to_center_x = x - x_intersection
            direction_to_center_y = y - y_intersection

            # Normalize the direction vector
            length = math.sqrt(direction_to_center_x ** 2 + direction_to_center_y ** 2)
            unit_vector_x = direction_to_center_x / length
            unit_vector_y = direction_to_center_y / length

            # Calculate the final label position with an offset
            offset = 1
            y_final = y_intersection + offset * unit_vector_y
            x_final = x_intersection + offset * unit_vector_x
            if angle > 180:
                x_final += (x - x_final)*0.2
            
            # Append the final label position to the list
            label_positions_final.append((round(x_final, 2), round(y_final, 2)))

    # Plot the labels on the plot
    for (x, y), label in zip(label_positions_final, labels):
        ax.text(x, y, label, ha='center', va='center')