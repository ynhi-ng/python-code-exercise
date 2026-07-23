"""
Ask user to input a string and a Caesar shift number from 0 to 25,
the program will decrypt the first letter of the string using the initial shift,
the second letter of the string will use the shift of the first character and continue with this logic until the end of the encrypted input string,
if the string is empty the program will exit
"""

print("DECRYPT STRING")

#Define the alphabet 
alphabet_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#Create a dictionary to store alphabet letter and its index accordingly
alphabet_character_index ={}
for char_index in range(len(alphabet_table)):
    alphabet_character_index[alphabet_table[char_index]] = char_index


#Handle cases when user input space and lower case character for the encrypted string
encrypted_string = input("Input encrypted string: ")
encrypted_string = encrypted_string.upper()
encrypted_string = "".join(encrypted_string.split()) 



if encrypted_string == "":
    print("Empty encrypted string.")
else:
    caesar_shift_number = int(input("Input caesar shift: "))

    
    if 0 <= caesar_shift_number <= 25:
        print("The decrypted string is:")

        #Loop through the encrypted string and find its index in alphabet, and use the index to decrypt the letter 
        for char in encrypted_string:
            encrypter_char_index = alphabet_character_index[char]
            decrypted_index = (encrypter_char_index - caesar_shift_number ) % 26
            decrypted_character = alphabet_table[decrypted_index]
            print(decrypted_character)

            #Update the shift number 
            caesar_shift_number = decrypted_index
    else:
        print("Invalid caesar shift.")