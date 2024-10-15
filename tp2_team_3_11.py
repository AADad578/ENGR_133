"""
Course Number: ENGR 13300
Semester: Fall 2024

Description:
    Encodes a binary message into the LSDs of a given image

Assignment Information:
    Assignment:     10.2.3 
    Team ID:        022-11
    Author:         Ramon Randolph, randol15@purdue.edu
    Author:         Ankur Raghavan, raghav21@purdue.edu
    Date:           10/14/2024

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

from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

from tp2_team_1_11 import load_image
from tp2_team_2_11 import v_encrypt, to_binary


def encodeImage(binary_message,image_path,output_path):
    binary_message = binary_message.replace(" ","")
    image= load_image(image_path)
    if image.ndim==2:
        x= image.shape[0]*image.shape[1]
        if len(binary_message)> x:
            print("Given message is too long to be encoded in the image")
            return
        pos=0
        for i in range(len(image)):
            if(pos>=len(binary_message)):
                break
            for j in range(len(image[i])):
                if(pos>=len(binary_message)):
                    break
                value=image[i][j]
                y=value % 2
                bin_value=binary_message[pos:pos+1] 
                pos+=1
                if bin_value==y:
                    continue
                if y==0: 
                    image[i,j]+=1
                else:
                    image[i,j]-=1
        pil_image = Image.fromarray(image, mode="L")
        pil_image.save(output_path)
    else:
        x= image.shape[0]*image.shape[1]*image.shape[2]
        if len(binary_message)> x:
            print("Given message is too long to be encoded in the image")
            return
        pos=0
        for i in range(len(image)):
            if(pos>=len(binary_message)):
                break
            for j in range(len(image[i])):
                if(pos>=len(binary_message)):
                    break
                for k in  range(len(image[i,j])):
                    if(pos>=len(binary_message)):
                        break
                    value =image[i][j][k]
                    y=value % 2
                    bin_value=binary_message[pos:pos+1] 
                    # print(bin_value, y, image[i,j,k])
                    pos+=1
                    if int(bin_value)==y:
                        continue
                    if y==0: 
                        image[i,j,k]+=1
                    else:
                        image[i,j,k]-=1
                    print(bin_value, image[i,j,k])
        
        pil_image = Image.fromarray(image)
        pil_image.save(output_path)
    print(f"Message successfully encoded and saved to: {output_path}")
    

def main():
    message = "Team 11 is exemplary!"
    key = "RItwKtCnrV"
    start_seq = "117"
    end_seq = "711"
    imagePath = "bear_col.png"
    outputPath = "output.png"
    # message = input("Enter the plaintext you want to encrypt: ")
    # key = input("Enter the key for Vigenere cipher: ")
    # start_seq = input("Enter the start sequence: ")
    # end_seq = input("Enter the end sequence: ")
    # imagePath = input("Enter the path of the image: ")
    # outputPath = input("Enter the path for the encoded image: ")
    
    
    encrypted = v_encrypt(message, key)
    print(f"Encrypted Message using Vigenere Cipher: {encrypted}")
    binary = to_binary(start_seq + encrypted + end_seq)
    print(f"Binary output message: {binary}")
    
    encodeImage(binary, imagePath, outputPath)

if __name__ == "__main__":
    main()