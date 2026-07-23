"""
Ask the user to input an encrypted string, and the Vigenere key(str) to decrypt the string.
If the user enter a non-empty encrypted string and Vigenere key, program will print out decrypted character
following Vigenre cipher, if the user enter an empty string, program will exit
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
    vigenere_key = input("Input vigenère key: ")

    if vigenere_key == "":
        print("Invalid vigenère key.")
    else:
        print("The decrypted string is:")
        #Loop through the index of encrypted string, find the character and its index in the alphabet, and find vigenere key index in the alphabet

        for char in range(len(encrypted_string)):

            encrypted_char = encrypted_string[char]
            encrypted_char_index = alphabet_character_index[encrypted_char]
            
            #Vigenere key char formula to the letter will wrap around if vigenere key is shorter than encrypted string
            vigenere_key_char = vigenere_key[char % len(vigenere_key)]
            vigenere_key_char_index = alphabet_character_index[vigenere_key_char]

            decrypted_char_index = (encrypted_char_index - vigenere_key_char_index) % 26
            decrypted_char = alphabet_table[decrypted_char_index]

            print(decrypted_char)