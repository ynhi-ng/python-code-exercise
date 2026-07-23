"""
Ask user to input a file name , program will accept user inputted filenames until quit 
is entered, program will print out the file name is valid or not,
and print GOODBYE if user input 'quit'
"""


print("CHECK FILENAMES")

#Create a list for valid file names only to check if user enter correctly 
valid_file_name = ["filea", "fileb", "filec", "filed", "filee"]

file_name = input("Input a filename (or quit to exit): ")


while file_name != 'quit':
    if file_name in valid_file_name:
        print(f"{file_name} - is a valid filename.")
    else:
        print(f"{file_name} - *is not* a valid filename.")
    
    file_name = input("Input a filename (or quit to exit): ")

print("GOODBYE")