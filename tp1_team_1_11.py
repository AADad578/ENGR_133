"""
Course Number: ENGR 13300
Semester: Fall 2024

Description:
    Replace this line with a description of your program.

Assignment Information:
    Assignment:     9.2.1 Team Project 1 Task 1
    Team ID:        022-11
    Author:         Ankur Raghavan, raghav21@purdue.edu ; Grant Stevenson, steve395@purdue.edu
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

def load_image(path):
    img = plt.imread(path)
    
    if int(np.max(img)) <= 1.0:
        img =img * 255
        img = img.astype(np.uint8)
        
    return img

def main():
    path = input("Enter the path of the image you want to load:")
    img = load_image(path)
    
    plt.imshow(img, cmap= 'gray', vmin= 0, vmax= 255)
    plt.show()
    
    
if __name__ == "__main__":
    main()
