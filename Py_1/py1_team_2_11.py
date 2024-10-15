"""
Course Number: ENGR 13300
Semester: Fall 2024

Description:
    Replace this line with a description of your program.

Assignment Information:
    Assignment:     5.2.2 Py1 Team 2 
    Team ID:        022 - 11
    Author:         Grant Stevenson, steve395@purdue.edu
    Author:         Ankur Raghavan, raghav21@purdue.eduW
    Author:         Ramon Randolph, randol15@purdue.edu
    Date:           09/5/2024

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

import random
from fractions import Fraction

def main():
    # take in input for the random seed
    random.seed(int(input("Enter the seed: ")))
    
    # generate and round the first number
    a = round(random.uniform(0, 100),3)
    # print the first random number
    print(f"First Random Number : {a}")
    
    # generate and round the second number
    b = round(random.uniform(10,50), 3)
    # print the first random number
    print(f"Second Random Number : {b}")
    
    # generate and round the third number
    c = round(random.uniform(20, 40), 3)
    # print the first random number
    print(f"Third Random Number : {c}")
    
    # generate and round the fourth number
    d = round(random.uniform(100, 200),3)
    # print the first random number
    print(f"Fourth Random Number : {d}")

    # sum all random numbers
    x = round(a + b + c + d,3)
    # print the sum of the random numbers
    print(f"Sum from decimals: {a} + {b} + {c} + {d} = {x}")

    # print the sum of the random numbers as a fraction
    print(f"Sum from fractions: {Fraction(a).limit_denominator(100)} + {Fraction(b).limit_denominator(100)} + {Fraction(c).limit_denominator(100)} + {Fraction(d).limit_denominator(100)} = {Fraction(x).limit_denominator(100)}")
if __name__ == "__main__":
    main()
