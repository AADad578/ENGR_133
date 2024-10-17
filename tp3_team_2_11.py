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


from tp1_team_2_11 import processImage
from tp2_team_1_11 import compare_images, load_image
from tp2_team_2_11 import to_binary, v_encrypt
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

from tp3_team_1_11 import xor, xor_cypher

#from tp1_team_3_11.py
def binToText(binary):
    message = ""
    for i in range(0, len(binary), 8):
        group =  binary[i:i+8]
        decoeded = chr(int(group,2))
        message += decoeded
    return message

def c_decrypt(message, shift):
    shift = int(shift) % 26  # Reduce the shift to the range 0-25
    encrypted_text = ""
   
    for char in message:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            encrypted_text += char  # Keep non-alphabetical characters unchanged (punctuation, spaces)
   
    return encrypted_text

def v_decrypt(text, u_key):
    key_value = []
    u_key = u_key.upper()
    #reading the text and making it the number

    a = len(text)

    #making the shift vaules into list, then using while to go through the values
    for c in u_key:
            key_ord = ord(c)
            shift = (key_ord - 65)
            key_value.append(shift)
    # print(key_value)
    #main for loop that goes through all of the characters in the string
    new_message = ""
    for i in range(a):
        l = text[i]  
        u = i % len(key_value)
        text_ord = ord(l) #cagegorizes what section it should go into
        if l.isupper():
            new_text = (text_ord - 65)
            new_value = new_text - key_value[i % len(key_value)]
            new_value = new_value % 26 
            new_message += chr(new_value + 65)
        elif l.islower():
            new_text = (text_ord - 97)
            new_value = new_text - key_value[i % len(key_value)]
            new_value = new_value % 26 
            new_message += chr(new_value + 97)
        elif l.isdigit():
            new_text = int(l)
            new_value = new_text - key_value[i % len(key_value)]
            new_value = new_value % 10
            new_message += str(new_value)
        else: 
            new_message += l 
        # print(i, l, new_text, u_key[u:u+1], key_value[i % len(key_value)], chr(new_value + 97))
    return new_message


def main():
    # cipher = input("Enter the cipher you want to use for encryption: ")
    # key = input("Enter the key for the cipher: ")
    # start = to_binary(input("Enter the start sequence: ")).replace(" ","")
    # end = to_binary(input("Enter the end sequence: ")).replace(" ","")
    # path = input("Enter the path of the input image: ")
    cipher = "caesar"
    key = "778"
    start = to_binary("40").replace(" ","")
    end = to_binary("04").replace(" ","")
    path = "ref_col_c.png"
    
    
    output = processImage(path, start, end)
    if "0" in output or "1" in output: #if there is a 0 or 1 it must contain binary
        binary = output[19:]
    else:
        return    
    print(f"Extracted Binary Message: {binary}")
    
    encrypted = binToText(binary)
    print(f"Converted Binary Text: {encrypted}")
    match cipher:
        case "vigenere":
            message = v_decrypt(encrypted, key)
        case "caesar":
            message = c_decrypt(encrypted, key)
        case "xor":
            message = binToText(xor_cypher(encrypted, key).replace(" ",""))
        case _:
            print("error")
            return
    
    print(f"Converted text: {message}")
              
if __name__ == "__main__":
    main()
