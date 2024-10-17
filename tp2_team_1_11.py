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
#copied from tp1_team_2_11.py
# finds the LSD of each value in an image
def img_to_bin(img):
    output = ""
    isRGB = len(img.shape)==3 #if there are 3 dimensions its rgb not grayscale
    
    if(isRGB and img.shape[2]==4):
        img = np.delete(img, 3, 2)        
    for row in img:
        for item in row:
            values = item if isRGB else [item] #make a list with each value, if rgb the list is already made, else make one item list
            for i in values: # for each value add to the output
                output += str(i%2) #add 0 if even (LSD is 0) or 1 if odd (LSD is 1)
    return output


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
    img1_bin = img_to_bin(img1)
    img2_bin = img_to_bin(img2)
    diff_bin = ""
    for i in range(len(img1_bin)):
        diff_bin += str(int(img1_bin[i]!=img2_bin[i])) #returns 1 if different
    isRGB = img1.ndim==3
    
    counter = 0
    for i in range(img1.shape[0]):
        row = []
        for j in range(img1.shape[1]):
            pixel = []
            if(isRGB):
                for k in range(3):
                    different = different if diff_bin[counter]=="0" else True
                    pixel.append(int(diff_bin[counter])*255)
                    counter+=1
                row.append(pixel)
            else:
                row.append(int(diff_bin[counter])*255)
                different = different if diff_bin[counter]=="0" else True
                counter +=1
                
        imgO.append(row)
    
    plt.imshow(imgO, cmap='gray', vmin= 0, vmax= 255)
    if(resultPath!=None):
        plt.savefig(resultPath)
    plt.show()
    return different
        
def main():
    path1 = "output.png"
    path2 = "bear_col_020_11_v.png"
    pathDiff = "diff.png"
    # path1 = input("Enter the path of your first image: ")
    # path2 = input("Enter the path of your second image: ")
    # pathDiff = input("Enter the path for the output image: ")
    img1 = load_image(path1)
    img2 = load_image(path2)
    if img1.ndim != img2.ndim or img1.shape[0] != img2.shape[0] or img1.shape[1] != img2.shape[1]:
        print("Cannot compare images in different modes (RGBA and L) or of different sizes.")
        print(img1.shape, img2.shape)
        return
    if compare_images(img1, img2, pathDiff):
        print("The images are different.")
    else:
        print("The images are the same.")


if __name__ == "__main__":
    main()
