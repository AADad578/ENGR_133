"""

Course Number: ENGR 13300
Semester: Fall 2024

 

Description:
    Efficiency of electric vehicle charged by wind turbine

 

Assignment Information:

    Assignment:     Py1 Team 11 Task 3

    Team ID:        Team 11

    Author:         Arjun Narayanan, naray129@purdue.edu
                    Ramon Randolph, Randolph@purdue.edu
                    Grant Stevenson, steve395@purdue.edu
                    Ankur Raghavan, raghav21@purdue.edu

    Date:           9/6/2024

 

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

import math as m

def main():
    rho=1.2
    A= float(input("Enter Area:"))
    Cp= 0.3
    v= float(input("Enter Wind Velocity:"))
    t= float(input("Enter Time:"))
    e= 0.007   
    power=turbine_power(rho,A,Cp,v)
    energy=accumulated_energy(power,t)
    distance=vehichle_distance(energy,e)
    print(f"The turbine generates {power}W, which accumulated {energy}Wh of energy.The vehicle has a range of {distance}km")

def turbine_power(rho,A,Cp,v):
    power=0.5*rho*A*Cp*v**3
    return power

def accumulated_energy(power,t):
    energy=power*t
    return energy

def vehichle_distance(energy,e):
    distance=energy*e
    return distance

if __name__ == "__main__":
    main()