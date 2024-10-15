"""
Course Number: ENGR 13300
Semester: Fall 2024

Description:
    Calculates the volume of a pool.

Assignment Information:
    Assignment:     6.3.2 - Py2 Ind 2 Main
    Team ID:        022-11
    Author:         Ankur Raghavan, raghav21@purdue.edu
    Date:           09/13/2024

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

from py2_ind_2_functions_raghav21 import standard, ramp, round

def main():
    # get input type
    type = input("Enter the name of the pool to calculate (Standard, Ramp, or Round): ")
    
    # check if input is valid
    if(type != "Standard" and type != "Ramp" and type != "Round"):
        print("Please run the program again and enter a valid pool name.")
        return
    
    # get input for size
    L1 = float(input("Enter the surface length or radius. "))
    L2 = float(input("Enter the surface width or bottom radius. "))
    Ds = float(input("Enter the shallow end depth. "))
    Dd = float(input("Enter the deep end depth. "))
    
    if(type == "Standard"):
        # find volume
        vol = standard(L1,L2,Ds,Dd)
        # if there isn't an error print the volume
        if vol != None:
            print(f"The volume of the Standard pool with your dimensions is {vol:,.2f} gallons.")
    if(type == "Ramp"):
        # find volume
        vol = ramp(L1,L2,Ds,Dd)
        # if there isn't an error print the volume
        if vol != None:
            print(f"The volume of the Ramp pool with your dimensions is {vol:,.2f} gallons.")
    if(type == "Round"):
        # find volume
        vol = round(L1,L2,Ds,Dd)
        # if there isn't an error print the volume
        if vol != None:
            print(f"The volume of the Round pool with your dimensions is {vol:,.2f} gallons.")
            
            


if __name__ == "__main__":
    main()
