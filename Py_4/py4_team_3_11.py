"""
Course Number: ENGR 13300
    Semester: Fall 2024

Description:
    takes input from file and calculates concentrations

Assignment Information:
    Assignment:     8.2.3
    Team ID:        022-11
    Author:         Ankur Raghavan, raghav21@purdue.edu
    Date:           9/26/2024

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


# Function to calculate concentration using Beer's Law
def absorb_calc(absorbency, path_length, molar_ext_coeff):
    return absorbency / (path_length * molar_ext_coeff)



# Main function
def main():

    # Input data
    with open("py_4/py4_task3_input.txt", "r") as input_file:
        
        substance_name = input_file.readline()[6:-1]
        path_length = float(input_file.readline()[13:-1])
        molar_ext_coeff = float(input_file.readline()[30:-1])
        absorbency_values = []
        while(True): # get all the values remaining in the file, one per line
            try: #if it runs out of file to read, it will throw an error
                absorbency_values.append(float(input_file.readline()[13:-1]))
            except: #(error caught here) and end the loop
                break
    # Calculate concentrations for the absorbency values
    concentrations = [absorb_calc(absorbency, path_length, molar_ext_coeff) for absorbency in absorbency_values]

    # Output the results
    print(f"The name of the substance is {substance_name}")
    for absorbency, concentration in zip(absorbency_values, concentrations):
        print(f"For {absorbency:.4f} absorbency value, the concentration is {concentration:.7f}")




# Run the main function

if __name__ == "__main__":
    main()