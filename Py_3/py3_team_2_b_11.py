"""
Course Number: ENGR 13300
Semester: Fall 2024

Description:
    Replace this line with a description of your program.

Assignment Information:
    Assignment:     7.2.2 - Py3 Team 2 B
    Team ID:        022 - 11 
    Author:         Ankur Raghavan, raghav21@purdue.edu
    Author:         Name, login@purdue.edu
    Author:         Name, login@purdue.edu
    Author:         Name, login@purdue.edu
    Date:           e.g. 08/29/2024

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


def my_factorial(num):
    if(num<0):# remove invalid input
        return -999
    output = 1 # start at 1 bc 1 doesn't affect multiplication
    for i in range(num): # 0 -> (num-1)
        output *= (i+1) #multiply by 1 -> num
    return output

def main():
    #input number
    num = int(input("Enter a number: "))
    #calculate factorial
    output = my_factorial(num)
    # if it's an error print that
    if(output == -999):
        print("Error -999 [Negative input].")
    # otherwise return the factorial
    else:
        print(f"The Factorial of {num} is {output}.")
    
if __name__ == "__main__":
    main()
