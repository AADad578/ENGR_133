"""
Course Number: ENGR 13300
Semester: Fall 2024

Description:
    TODO: Add

Assignment Information:
    Assignment:     9.2.3
    Team ID:        022-11
    Author:         Ankur Raghavan, raghav21@purdue.edu
    Author:         Grant Stevenson, steve395@purdue.edu
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

""" Write any import statements here (and delete this line)."""
def binToText(binary):
    message = ""
    for i in range(0, len(binary), 8):
        group =  binary[i:i+8]
        decoeded = chr(int(group,2))
        message += decoeded
    return message

def main():
    x = input("Enter the binary message: ")
    print(binToText(x))

if __name__ == "__main__":
    main()