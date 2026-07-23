"""
Ask user to input a file name and department name, 
program will check if the department is valid and 
check if the file is valid within the department inputted
program will print out the department name and file name accordingly
and if the user input 'quit', program will print out GOODBYE
"""


print("CHECK FILENAMES")

#Create 2 lists for valid file names and department names to check if user enter correctly 
valid_file_name = ["filea", "fileb", "filec", "filed", "filee"]
valid_dept_name = ["dep1", "dep2", "dep3"]

#Create a list for department name - file name mapping accordingly 

file_name_dept_mapping = [
    ("dep1", "filea"),
    ("dep1","fileb"),
    ("dep2","filec"),
    ("dep3","filea"),
    ("dep3","filec")
]
dept_name = input("Input a department (or quit to exit): ")

while dept_name != 'quit':
    if dept_name in valid_dept_name:
        file_name = input("Input a filename: ")

        while file_name == "":
            file_name = input("Input a filename: ")

        if (dept_name,file_name) in file_name_dept_mapping:
            print(f"{file_name} - is a valid filename for - {dept_name}")
        else:
            print(f"{file_name} - *is not* a valid filename for - {dept_name}")
            
    dept_name = input("Input a department (or quit to exit): ")

print("GOODBYE")