"""
Course Number: ENGR 13300
Semester: e.g. Fall 2024

Description:
    Finds the phenotypes of the features in the input csv file.

Assignment Information:
    Assignment:     7.3.1 py3 ind 1
    Team ID:        022-11
    Author:         Ankur Raghavan, raghav21@purdue.edu
    Date:           09/25/2024

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

import csv


def main():
    features = []
    
    #open the file
    with open('py_3/list_of_features.csv',newline='') as csvfile:
        #Load File
        
        #create reader to read it
        reader = csv.reader(csvfile, delimiter=',')
        firstrow = True
        prevRow = {}
        names = ['feature','positions','numSets','genotype','maxCombos','phenotype'] #short names of columns, len(names) must == # of cols
        for row in reader: 
            #ignore first row with headers
            if(firstrow):
                firstrow = False
                continue
            completeRow = True
            feature = {}
            for i in range(len(names)):
                if row[i]!="": #if anything is empty, grab it from the last complete row
                    feature[names[i]] = row[i]
                else:
                    feature[names[i]] = prevRow[i]
                    completeRow = False # mark row as incomplete if it has any missing data
            features.append(feature) # add it to the list of features
            if(completeRow):
                #if the row has all the data, store it for later rows
                prevRow = row
    # print(features)
    ended = False
    
    # convert the list of dictionaries into 1 dictionary with the feature name as key and list of indexs for finding them
    keys = {}
    for i in range(len(features)):
        try:
            lst = keys[features[i]['feature']]
            keys[features[i]['feature']].append(i)
        except:
            keys[features[i]['feature']] = [i]
    # print(keys)
            
    # run until user stops it
    while True: 
        
        #print all the available features
        print("AVAILABLE FEATURES:")
        for key in keys:
            print(key)
            
        #get the user feature and check if it's valid
        selected = input("Please select a feature: ")
        if keys.get(selected) == None:
            print("Invalid input.")
            if(input("Would you like to run again? (y or n): ")=="n"): 
                break
            continue

        print("POSSIBLE GENOTYPES:")        
        genotypes = {}
        for i in keys[selected]:
            # print the genotypes and store into a dict
            print(features[i]['genotype'])
            genotypes[features[i]['genotype']] = features[i]['phenotype']
        
        # get the user genotype and check if it's valid
        typeSelected = input("Please input the genotype: ")
        pheno = genotypes.get(typeSelected)
        if(pheno!=None): #if it exists
            print(f"This corresponds to the physical attribute: {pheno}")
        else:
            print("Invalid input.")
        
        if(input("Would you like to run again? (y or n): ")=="n"): 
            break

if __name__ == "__main__":
    main()
