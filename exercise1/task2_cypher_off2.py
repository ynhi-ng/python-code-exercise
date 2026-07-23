"""
Ask the user to input in a number represented by alphabet letter and a shift number,
program will decrypt letter and print the 2 decrypted entries to the left and right of what the inputted shift asks for
"""

print("CAESAR CYPHER DECRYPT")

valid_encrypted_number = False
valid_shift_number = False 

while not valid_encrypted_number:
    encrypted_number = int(input("Input a number from ALPHABET TABLE: "))
    if 0 <= encrypted_number <= 25:
        valid_encrypted_number = True
    else:
        valid_encrypted_number = False

while not valid_shift_number:
    shift_number = int(input("Input a caesar shift: "))
    if 0 <= shift_number <= 25:
        valid_shift_number = True
    else:
        valid_shift_number = False
print() # Print out a blank line 

#Create a variable name center number, which is the decrypted number. Left number and right number are 2 decrypted entries to the left and right 
center_number = (encrypted_number - shift_number) % 26 
left_number = (center_number - 2 ) % 26
right_number = (center_number + 2) % 26 
print(f"The decrypted entries in ALPHABET TABLE are: {left_number} {center_number} {right_number}")
