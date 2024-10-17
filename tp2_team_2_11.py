"""
Course Number: ENGR 13300
Semester: Fall 2024

Description:
    TODO: Add

Assignment Information:
    Assignment:     TODO: Add
    Team ID:        022-11
    Author:         Grant Stevenson, raghav21@purdue.edu
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

""" Write any import statements here (and delete this line)."""


def v_encrypt(text, u_key):
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
            new_value = new_text + key_value[i % len(key_value)]
            new_value = new_value % 26 
            new_message += chr(new_value + 65)
        elif l.islower():
            new_text = (text_ord - 97)
            new_value = new_text + key_value[i % len(key_value)]
            new_value = new_value % 26 
            new_message += chr(new_value + 97)
        elif l.isdigit():
            new_text = int(l)
            new_value = new_text + key_value[i % len(key_value)]
            new_value = new_value % 10
            new_message += str(new_value)
        else: 
            new_message += l 
        # print(i, l, new_text, u_key[u:u+1], key_value[i % len(key_value)], chr(new_value + 97))
    return new_message

        

#converts string of text to binary
#From Checkpoint 1 task 2
def to_binary(string):
    output=""
    for char in string:
        byte = bin(ord(char))[2:]
        output += "0"*(8-len(byte))+byte
        output += " "
    return output




def main():
    # text = input("Enter the plaintext you want to encrypt: ")
    # key = input("Enter the key for Vigenere cipher: ")
    # start_seq = input("Enter the start sequence: ")
    # end_seq = input("Enter the end sequence: ")
    text = "Team 11 is praiseworthy!!!"
    key = "RItwKtCnrV"
    start_seq = "117"
    end_seq = "711"
    
    new_message = v_encrypt(text, key)
    print(f"Encrypted Message using Vigenere Cipher: {new_message}")
    binary = to_binary(start_seq + new_message + end_seq)
    print(f"Binary output message: {binary}")

if __name__ == "__main__":
    main()