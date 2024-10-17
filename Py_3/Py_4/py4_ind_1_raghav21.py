"""
Course Number: ENGR 13300
Semester: Fall 2024

Description:
    Performs calculations on given images

Assignment Information:
    Assignment:     8.3.1 Py4 Ind 1
    Team ID:        022-11
    Author:         Ankur Raghavan, raghav21@purdue.edu
    Date:           10/2/2024

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

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

# load images
def load_images(directory):
    paths = Path(directory) #make a new path with the given directory
    imgs = [] 
    for path in paths.iterdir(): #iterate through each path
        imgs.append((plt.imread(path),str(path).split("\\")[-1])) # read the image and add just the filename to the path, which is the section after the last backslash
    # print(imgs)
    return imgs

#analyze the red content of the image
def analyze_red_content(image):
    return np.average(image[:,:,0]) if image.ndim==3 else 0 # take the average of the first item in every pixel. 
    # if the image has more/less than 3 dimensions, ie. grayscale image, return 0

def calculate_brightness(image):
    if(image.ndim==2): # if the image is grayscale return 0
        return 0
    RED_MULT =  0.299 #define the multipliers for each value
    GREEN_MULT = 0.587
    BLUE_MULT = 0.114
    luminosity = 0.0
    numPixels = 0
    # print(image)
    for row in image:
        for item in row:
            numPixels+=1 #add to the pixel count to accurately divide at the end
            luminosity += item[0]*RED_MULT #multiply red by the intensity and add it
            luminosity += item[1]*GREEN_MULT # multiply green by the intensity and add it
            luminosity += item[2]*BLUE_MULT # multiply blue by the intensity and add it
    return luminosity/numPixels # return the average
            
#TODO: Does images have filenames in it (ie. output of load_images())?
def write_results(filename, images):
    with open(filename, "w") as file:
        try: #try each way
            for image, name in images: # will throw error if no name is inputted
                file.write(f"{name}: Brightness: {calculate_brightness(image):.2f}, Red Content: {analyze_red_content(image):.2f}")
        except:
            for image in images: # if no name, try to write it anyways, but without the name
                file.write(f"Brightness: {calculate_brightness(image[0]):.2f}, Red Content: {analyze_red_content(image[0]):.2f}")
    

def generate_visualizations(images):
 for image, name in images:
     plt.figure()  # Create a new figure

     if image.ndim == 2:  # Check if the image is grayscale
         # Plot histogram for grayscale image
         plt.hist(image.flatten(), bins=256, color='gray', alpha=0.7, label='Intensity')
         plt.title(f'Intensity Histogram - {name}')  # Set the title of the histogram

     elif image.ndim == 3:  # Check if the image is color
         # Plot histograms for each color channel and the total intensity
         plt.hist(image.flatten(), bins=256, color='orange', alpha=0.5, label='Total')
         ### Start of your code
         plt.hist(image[:,:,0].flatten(), bins=256, color='red', alpha=0.5, label='Red') #red
         plt.hist(image[:,:,1].flatten(), bins=256, color='green', alpha=0.5, label='Green') #green
         plt.hist(image[:,:,2].flatten(), bins=256, color='blue', alpha=0.5, label='Blue') #blue

         ### End of your code
         plt.title(f'Color Histogram - {name}')  # Set the title of the histogram
     plt.xlabel('Intensity')  # Label the x-axis
     plt.ylabel('Frequency')  # Label the y-axis
     plt.legend()  # Display the legend
     plt.savefig('Histogram.png')  # Show the plot

#TODO: Is there any requirement that a main file exists?
def main():
    imgs = load_images(input("Enter the path of the image folder: ")) #Take input and find the images accociated with them
    for image in imgs:
        print(f"{image[1]}: Brightness: {calculate_brightness(image[0]):.2f}, Red Content: {analyze_red_content(image[0]):.2f}") #match sample output
    write_results("results.txt", imgs) #save to file (not in sample output??)
    generate_visualizations(imgs) # make the histograms

if __name__ == "__main__":
    main()
