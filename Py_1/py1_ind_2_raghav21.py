"""
Course Number: ENGR 13300
Semester: Fall 2024

Description:
    Replace this line with a description of your program.

Assignment Information:
    Assignment:     5.3.2 Py1 Ind 2
    Team ID:        022-11
    Author:         Ankur Raghavan, raghav21@purdue.edu
    Date:           9/11/2024

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

import math

def main():
    # get input from the user for the first resistor
    resist1 = float(input("Input the resistance of the first resistor [Ω]: "))
    # set the second resistor
    resist2 = 19.5
    # add the resistor's values for the value of them in series
    series = resist1 + resist2
    # perform the geometric mean for the value of them in parallel
    parallel = 1.0 / ((1.0/resist1) + (1.0/resist2))
    
    # print it all out
    print(f"Type              First         Second         Total Resistance")
    print(f"Parallel          {resist1:.1f} Ω        {resist2:.1f} Ω         {parallel:.1f} Ω")
    print(f"Series            {resist1:.1f} Ω        {resist2:.1f} Ω         {series:.1f} Ω")


if __name__ == "__main__":
    main()
