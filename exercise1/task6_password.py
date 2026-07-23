"""
Ask user to input a file name and department name, 
program will check if the department is valid and,
check if the file is valid within the department inputted,
program will print out the department name and file name accordingly,
If the file name requires password, there will be 3 attempts given for users, attempts will reset after 3 times,
and if the user input 'quit', program will print out GOODBYE
"""


print("CHECK FILENAMES")

#Create 2 lists for valid file name and department name to check if user enter correctly 
valid_file_name = ["filea", "fileb", "filec", "filed", "filee"]
valid_dept_name = ["dep1", "dep2", "dep3"]

#Create a list for department name - file name mapping accordingly 

dept_file_mapping = [
    ("dep1", "filea"),
    ("dep1","fileb"),
    ("dep2","filec"),
    ("dep2","filed"),
    ("dep3","filea"),
    ("dep3","filec")
]

#Create a dictionary to store file and password mapping (if file has password)

file_password_mapping = {
    ("dep1","fileb"):"pass1",
    ("dep2","filed") : "pass2"
}

dept_name = input("Input a department (or quit to exit): ")


while dept_name != 'quit':
    if dept_name in valid_dept_name:
        file_name = input("Input a filename: ")

        while file_name == "":
            file_name = input("Input a filename: ")

        #if the department and file name require password will proceed to ask for user input, and user has 3 attempts   

        if (dept_name,file_name) in file_password_mapping:
            #initiate a variable to store password attempt
            attempt_remain = 3
            print(f"{attempt_remain} password attempts remain.")

            is_password_correct = False
            while not is_password_correct and attempt_remain > 0:
                password = input("Input password: ")
                if password == file_password_mapping[(dept_name,file_name)]:
                    is_password_correct = True
                    break
                
                else:
                    attempt_remain -= 1
                    if attempt_remain > 0:
                        print(f"{attempt_remain} password attempts remain.")
        
        #if the department and file name don't require password, will treate it as password is correct as default 
        else:
            is_password_correct = True

        if is_password_correct:
            if (dept_name, file_name) in dept_file_mapping:
                print(f"{file_name} - is a valid filename for - {dept_name}")
            else:
                print(f"{file_name} - *is not* a valid filename for - {dept_name}")


    dept_name = input("Input a department (or quit to exit): ")

print("GOODBYE") 