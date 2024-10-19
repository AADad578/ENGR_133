"""
Course Number: ENGR 13300
Semester: Fall 2024

Description:
    TODO: Add

Assignment Information:
    Assignment:     9.2
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

from tp1_team_2_11 import processImage
from tp1_team_2_11 import to_binary
from tp1_team_3_11 import binToText

def main():
    path = input("Enter the path of the image you want to load: ")
    start = to_binary(input("Enter the start sequence: "))
    end = to_binary(input("Enter the end sequence: "))
    output = processImage(path, start, end)
    print(f"Below is the img_array output of {path}:")
    print(output)
    if "0" in output or "1" in output: #if there is a 0 or 1 it must contain binary
        binary = output[19:]
        print(binToText(binary))
    
    
if __name__ == "__main__":
    main()
