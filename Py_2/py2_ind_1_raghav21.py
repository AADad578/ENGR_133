"""
Course Number: ENGR 13300
Semester: Fall 2024

Description:
    Monitors the conditions inside a extraction vessel

Assignment Information:
    Assignment:     6.3.1 - Py2 Ind 1
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


CRITICAL_TEMP = 304.2
CRITICAL_PRESSURE = 73.8

MAX_SPEC_TEMP = 344.14*.95
MAX_SPEC_PRESSURE = 137*.95

def check_status(temp, pressure):
    # make output string 
    output = ""
    
    # if at critical point, print that and end the function
    if(CRITICAL_TEMP == temp and CRITICAL_PRESSURE==pressure):
        print("CO2 is at the critical point.")
        return  
    # if the temperature is below critical, print how much to increase it by 
    if temp<CRITICAL_TEMP:
        print(f"CO2 is below the critical temperature.\nIncrease the temperature by at least {(CRITICAL_TEMP-temp):.2f} Kelvin.")  
    # if below max spec but above critical point, print that it is safe 
    elif temp<MAX_SPEC_TEMP:
        print("Temperature is within safe operating conditions.")       
    # if above max spec, print that it is out of range and how much to reduce it by
    else:
        print(f"Warning! Reduce the temperature!\nDecrease the temperature by at least {abs(MAX_SPEC_TEMP-temp):.2f} Kelvin.")
    
    # if the pressure is below critical, print how much to increase it by 
    if pressure<CRITICAL_PRESSURE:
        print(f"CO2 is below the critical pressure.\nIncrease the pressure by at least {(CRITICAL_PRESSURE-pressure):.2f} bar.")
    # if below max spec but above critical point, print that it is safe 
    elif pressure<MAX_SPEC_PRESSURE:
        print("Pressure is within safe operating conditions.")
    # if above max spec, print that it is out of range and how much to reduce it by
    else:
        print(f"Warning! Reduce the pressure!\nDecrease the pressure by at least {abs(MAX_SPEC_PRESSURE-pressure):.2f} bar.")

    return

        

def main():
    temp = float(input("Enter the temperature of carbon dioxide in Kelvin: "))
    if(temp<0):
        print("Error: Please enter a valid temperature.")
        return
    
    pressure = float(input("Enter the pressure of carbon dioxide in bar: "))
    if(pressure<0):
        print("Error: Please enter a valid pressure.")
        return

    check_status(temp, pressure)
    return


if __name__ == "__main__":
    main()
