"""
Ask the user to input in a number represented by alphabet letter and a shift number
the program will decrypt letter using Caesar Cipher
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

decrypted_entry = (encrypted_number - shift_number) % 26 
print(f"The decrypted entry in ALPHABET TABLE is: {decrypted_entry}")
