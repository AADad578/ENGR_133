"""
Course Number: ENGR 13300
    Semester: Fall 2024

Description:
    

Assignment Information:
    Assignment:     8.2.3 Py4 Team 1
    Team ID:        022-11
    Author:         Ankur Raghavan, raghav21@purdue.edu
    Date:           09/24/2024

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


def main():
    lastName = input("Enter your last name: ").strip()
    firstName = input("Enter your first name: ").strip()
    years = int(input("Enter your age in whole years: "))
    days = int(input("Enter the days elapsed since your last birthday: "))
    
    days += years*365.242199 # add the number of years in days
    years = days/365.242199 #find the total number of years
    seconds = days * 24 * 60 * 60
    
    with open("py4_team_2_11.txt", "w") as file:
        file.write(firstName + " " + lastName+"\n")
        file.write(f"You are {years} years old\n")
        file.write(f"You are {seconds:.0f} seconds old.")
        


if __name__ == "__main__":
    main()
