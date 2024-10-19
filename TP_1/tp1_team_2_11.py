"""
Course Number: ENGR 13300
Semester: Fall 2024

Description:
    Finds secret messages in the images

Assignment Information:
    Assignment:     9.2.2 Team Project 1
    Team ID:        022-11
    Author:         Ankur Raghavan, raghav21@purdue.edu
    Date:           10/1/2024

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
import numpy as np
from tp1_team_1_11 import load_image

#converts string of text to binary
def to_binary(string):
    output=""
    for char in string:
        byte = bin(ord(char))[2:]
        output += "0"*(8-len(byte))+byte
    return output

# finds the LSD of each value in an image
def img_to_bin(img):
    output = ""
    isRGB = len(img.shape)==3 #if there are 3 dimensions its rgb not grayscale
    for row in img:
        for item in row:
            values = item if isRGB else [item] #make a list with each value, if rgb the list is already made, else make one item list
            for i in values: # for each value add to the output
                output += str(i%2) #add 0 if even (LSD is 0) or 1 if odd (LSD is 1)
    return output

def findMessage(start, end, bitfield):
    sIndex = bitfield.find(start)
    eIndex = bitfield.find(end)
    if(sIndex==-1 or eIndex==-1):
        return None
    sIndex += len(start)
    return bitfield[sIndex:eIndex]

def processImage(path, start, end):
    img = load_image(path)
    output = img_to_bin(img)
    message = findMessage(start, end, output)
    if(message==None):
        return "Start or end sequence not found in the image."
    else:
        return f"Extracted Message: {message}"

def main():
    path = input("Enter the path of the image you want to load: ")
    start = to_binary(input("Enter the start sequence: "))
    end = to_binary(input("Enter the end sequence: "))
    print(processImage(path, start, end))
    
if __name__ == "__main__":
    main()
