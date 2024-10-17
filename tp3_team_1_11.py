"""
Course Number: ENGR 13300
Semester: Fall 2024

Description:
    TODO: Add

Assignment Information:
    Assignment:     TODO: Add
    Team ID:        022-11
    Author:         Ankur Raghavan, raghav21@purdue.edu
    Date:           TODO: Add

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


from tp1_team_3_11 import binToText
from tp2_team_1_11 import compare_images, img_to_bin, load_image
from tp2_team_2_11 import to_binary, v_encrypt
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

# @author Arjun 
def c_encrypt(message, shift):
    shift = int(shift) 
    encrypted_text = ""
   
    for char in message:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        elif char.isdigit():
            encrypted_text += str((int(char)+shift)%10)
            print(int(char))
            print(str((int(char)+shift)%10))
        else:
            encrypted_text += char  # Keep non-alphabetical characters unchanged (punctuation, spaces)
   
    return encrypted_text

def xor(a, b):
    return str(int(a != b))

#from tp2_team_3_11.py but added offset
def encodeImage(binary_message,image_path,output_path, offset):
    binary_message = "0"*offset+ binary_message.replace(" ","")
    image= load_image(image_path)
    length = len(binary_message)
    if image.ndim==2:
        x= image.shape[0]*image.shape[1] #number of bits (width*height)
        if length> x:
            print("Given message is too long to be encoded in the image")
            return
        pos=0
        for i in range(len(image)):
            if(pos>=length):
                break
            for j in range(len(image[i])):
                if(pos>=length):
                    break
                if(pos<offset):
                    pos+=1
                    continue
                value=image[i][j]
                y=value % 2
                bin_value=int(binary_message[pos:pos+1])
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
        x= image.shape[0]*image.shape[1]*3 # number of bits (width*height*3)
        if length> x:
            print("Given message is too long to be encoded in the image")
            return
        pos=0
        for i in range(len(image)):
            if(pos>=length): #if message is done, exit
                break
            for j in range(len(image[i])):
                if(pos>=length):
                    break
                for k in  range(3):
                    if(pos<offset): #if the offset isnt over, pass
                        pos+=1
                        continue
                    if(pos>=length):
                        break
                    value =image[i][j][k] # value at pixel
                    y=value % 2 #LSB of value
                    bin_value=int(binary_message[pos:pos+1]) #value of message
                    pos+=1
                    if int(bin_value)==y:
                        continue
                    if y==0: 
                        image[i,j,k]+=1
                    else:
                        image[i,j,k]-=1
        
        pil_image = Image.fromarray(image)
        pil_image.save(output_path)
    print(f"Message successfully encoded and saved to: {output_path}")
    
def xor_cypher(message, key):
    m_bin = to_binary(message).replace(" ", "")
    k_bin = to_binary(key).replace(" ", "") #convert to binary and remove spaces
    output = ""
    counter = 0
    for i in range(len(m_bin)):
        output += xor(m_bin[i], k_bin[i%len(k_bin)])
        if counter == 7:# add a space every 8 characters
            counter = 0
            output+= " "
        else:
            counter+=1
    return output


def main():
    cipher = input("Enter the cipher you want to use for encryption: ")
    message = input("Enter the plaintext you want to encrypt: ")
    key = input("Enter the key for the cipher: ")
    start_seq = to_binary(input("Enter the start sequence: "))
    end_seq = to_binary(input("Enter the end sequence: "))
    offset = int(input("Enter the bit offset before you want to start encoding: "))
    input_path = input("Enter the path of the input image: ")
    output_path = input("Enter the path for your encoded image: ")
    comp_path = input("Enter the path of the image you want to compare: ")
    # cipher = "caesar"
    # message = "Love ENGR"
    # key = "777"
    # start_seq = to_binary("40")
    # end_seq = to_binary("04")
    # offset = 9
    # input_path = "ref_col.png"
    # output_path = "col_c.png"
    # comp_path = "ref_col_c.png"
    
    encrypted = None
    match cipher:
        case "vigenere":
            encrypted = v_encrypt(message, key)
            binary = start_seq + to_binary(encrypted) + end_seq
            print(f"Encrypted Message using Vigenere Cipher: {encrypted}")
        case "caesar":
            encrypted = c_encrypt(message, key)
            binary = start_seq + to_binary(encrypted) + end_seq
            print(f"Encrypted Message using Caesar Cipher: {encrypted}")
        case "xor":
            binary = xor_cypher(message, key)
            encrypted = binToText(binary.replace(" ",""))
            binary = start_seq + binary + end_seq
            print(f"Encrypted Message using XOR Cipher: {encrypted}")
        case _:
            print("error")
            return
    
    print(f"Binary output message: {binary}")
    encodeImage(binary, input_path, output_path, offset)
    
    #compare images
    img1 = load_image(output_path)
    plt.imshow(img1)
    plt.show()
    img2 = load_image(comp_path)
    if img1.ndim != img2.ndim or img1.shape[0] != img2.shape[0] or img1.shape[1] != img2.shape[1]:
        print("Cannot compare images in different modes (RGBA and L) or of different sizes.")
        print(img1.shape, img2.shape)
        return
    if compare_images(img1, img2, None):
        print("The images are different.")
    else:
        print("The images are the same.")
    
            
            
            
if __name__ == "__main__":
    main()
