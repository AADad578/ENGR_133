"""
Course Number: ENGR 13300
Semester: Fall 2024

Description:
    Implements Atbash cipher

Assignment Information:
    Assignment:     8.3.2
    Team ID:        022-11
    Author:         Ankur Raghavan, raghav21@purdue.edu
    Date:           10/2/2024

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

def atbash_cipher(start):
    output = ""
    for char in start:
        if not char.isalnum(): # skip character if its not a letter or number
            output += char
            continue
        offset = 48 if char.isdigit() else 97 if char.islower() else 65 # offset is 48 if its a number, 65 if its uppercase, or 97 if it's lowercase
        totalNum = 25 if char.isalpha() else 9 # if its a letter there are 26 options, if its a number there are 10
        num = ord(char)-offset # find index in a sorted list of characters
        output += chr((totalNum-num)+offset) # add the inverted character (plus offset) to the output
    return output


def main():
    with open(input("Enter the name of the file: "),"r") as readFile:
        output = atbash_cipher(readFile.readline())
    print(f"The encrypted message is: '{output}'")
    with open("atbash_cipher.txt", "w") as writeFile:
        writeFile.write(output)
    print("Encryption completed. Check the output files for results.")

if __name__ == "__main__":
    main()
