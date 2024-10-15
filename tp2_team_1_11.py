"""
Course Number: ENGR 13300
Semester: Fall 2024

Description:
    Compares two images and produces a difference map

Assignment Information:
    Assignment:     10.2.1
    Team ID:        022-11
    Author:         Ankur Raghavan, raghav21@purdue.edu
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

from matplotlib import pyplot as plt
import numpy as np

#copied from tp1_team_1_11.py
def load_image(path):
    img = plt.imread(path)
    
    if int(np.max(img)) <= 1.0:
        img =img * 255
        img = img.astype(np.uint8)
        
    return img

def compare_images(img1, img2, resultPath):
    different = False
    imgO = []
    for i in range(img1.shape[0]):
        row = []
        for j in range(img1.shape[1]):
            item = []
            value1 = img1[i][j] if(len(img1.shape)==3) else [img1[i][j]]
            value2 = img2[i][j] if(len(img2.shape)==3) else [img2[i][j]]
            for k in range(min(len(value1),3)):
                
                if(value1[k]%2==value2[k]%2):
                    item.append(0)
                else:
                    item.append(255)
                    different = True
            row.append([item[0],item[1],item[2]] if len(item)>1 else item[0])
        imgO.append(row)
    plt.imshow(imgO, cmap='gray', vmin= 0, vmax= 255)
    plt.savefig(resultPath)
    plt.show()
    return different
        


def main():
    path1 = input("Enter the path of your first image: ")
    path2 = input("Enter the path of your second image: ")
    pathDiff = input("Enter the path for the output image: ")
    img1 = load_image(path1)
    img2 = load_image(path2)
    if img1.ndim!=img2.ndim or img1.shape[0]!= img2.shape[0] or img1.shape[1] != img2.shape[1]:
        print("Cannot compare images in different modes (RGBA and L) or of different sizes.")
        print(img1.shape, img2.shape)
        return
    if compare_images(img1, img2, pathDiff):
        print("The images are different.")
    else:
        print("The images are the same.")


if __name__ == "__main__":
    main()
