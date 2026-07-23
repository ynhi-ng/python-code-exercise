"""
Ask the user to input size of the alphabet, an encrypted letter number and a shift
the program will decrypt letter and print out three values center around from left to right
"""

print("CAESAR CYPHER DECRYPT")

valid_alphabet_size = False
valid_encrypted_number = False
valid_shift_number = False 

while not valid_alphabet_size:
    alphabet_size = int(input("Input size of the alphabet: "))
    if 1 <= alphabet_size <= 26:
        valid_alphabet_size = True
    else:
        valid_alphabet_size = False

#Valid end range is the end number based on the alphabet size where user can input number for encrypted letter
valid_end_range = alphabet_size - 1

while not valid_encrypted_number:
    encrypted_number = int(input("Input a number from ALPHABET TABLE: "))
    if 0 <= encrypted_number <= valid_end_range:
        valid_encrypted_number = True
    else:
        valid_encrypted_number = False

while not valid_shift_number:
    shift_number = int(input("Input a caesar shift: "))
    if 0 <= shift_number <= valid_end_range:
        valid_shift_number = True
    else:
        valid_shift_number = False
print() #Print out a blank line

#Create a variable name center number, which is the decrypted number. Left number and right number are 2 decrypted entries to the left and right
center_number = (encrypted_number - shift_number) % alphabet_size
left_number = (center_number - 2 ) % alphabet_size
right_number = (center_number + 2) % alphabet_size
print(f"The decrypted entries in ALPHABET TABLE are: {left_number} {center_number} {right_number}")