"""
Course Number: ENGR 13300
Semester: Fall 2024

Description:
    Decrypts the images

Assignment Information:
    Assignment:     11.1.2
    Team ID:        022-11
    Author:         Ankur Raghavan, raghav21@purdue.edu
    Date:           10/16/2024

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
from tp1_team_3_11 import binToText
from tp2_team_1_11 import compare_images, load_image
from tp2_team_2_11 import to_binary, v_encrypt
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

from tp3_team_1_11 import xor, xor_cypher


# encrypt with the caesar cipher
def c_decrypt(message, shift):
    shift = int(shift) #make sure the shift is a number
    encrypted_text = ""
   
    for char in message:
        if char.isalpha(): #if its a letter
            shift_base = ord('A') if char.isupper() else ord('a') #subtract the ord value for Capital A or lowercase a if it is upper or lowercase respectivly
            encrypted_text += chr((ord(char) - shift_base - shift) % 26 + shift_base) # add the shift and mod 26 to ensure it is still a letter, and convert back to letter
        elif char.isdigit(): #if its a number
            encrypted_text += str((int(char)-shift)%10) #convert to a number and add the shift. Then mod 10 to ensure it is still one digit
        else:
            encrypted_text += char  # Keep non-alphabetical characters unchanged (punctuation, spaces)
   
    return encrypted_text 

def v_decrypt(text, u_key):
    key_value = []
    u_key = u_key.upper() #should be all uppercase
    
    #making the shift vaules into list, then using while to go through the values
    for c in u_key:
            key_ord = ord(c)
            shift = (key_ord - 65)
            key_value.append(shift)
    # print(key_value)
    #main for loop that goes through all of the characters in the string
    new_message = ""
    for i in range(len(text)):
        l = text[i]  
        u = i % len(key_value)
        text_ord = ord(l) #cagegorizes what section it should go into
        if l.isupper():
            new_text = (text_ord - 65) #uppercase A in ASCII is 65
            new_value = new_text - key_value[u] #shift by the key value
            new_value = new_value % 26 # mod 26 to keep it a letter 
            new_message += chr(new_value + 65) # convert back to a character
        elif l.islower():
            new_text = (text_ord - 97) #lowercase a in ASCII is 97
            new_value = new_text - key_value[u] #shift by the key value
            new_value = new_value % 26 # mod 26 to keep it a letter 
            new_message += chr(new_value + 97) # convert back to a character
        elif l.isdigit():
            new_text = int(l) #convert to a number
            new_value = new_text - key_value[u] #shift by the key value
            new_value = new_value % 10 # mod 10 to keep it a single digit 
            new_message += str(new_value) #convert back to string
        else: 
            new_message += l #if its not a letter/number don't change it
    return new_message 


def main():
    cipher = input("Enter the cipher you want to use for encryption: ")
    key = input("Enter the key for the cipher: ")
    start = to_binary(input("Enter the start sequence: ")).replace(" ","")
    end = to_binary(input("Enter the end sequence: ")).replace(" ","")
    path = input("Enter the path of the input image: ")
    
    #converts to binary
    output = processImage(path, start, end) #cconverts image to binary, removing the start and end sequence
    if "0" in output or "1" in output: #if there is a 0 or 1 it must contain binary
        binary = output[19:]
    else:
        return    
    print(f"Extracted Binary Message: {binary}")
    
    
    encrypted = binToText(binary) #convert back to text
    print(f"Converted Binary Text: {encrypted}")
    match cipher:
        case "vigenere":
            message = v_decrypt(encrypted, key) # decrypt text using key
        case "caesar":
            message = c_decrypt(encrypted, key) # decrypt text using key
        case "xor":
            message = binToText(xor_cypher(encrypted, key).replace(" ","")) #decrypt, returns binary, so convert back
        case _:
            print("error")
            return
    
    print(f"Converted text: {message}")
              
if __name__ == "__main__":
    main()
