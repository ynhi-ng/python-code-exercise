
#Define the alphabet 
alphabet_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#Create a dictionary to store alphabet letter and its index accordingly
alphabet_character_index ={}
for char_index in range(len(alphabet_table)):
    alphabet_character_index[alphabet_table[char_index]] = char_index



def caesar_cypher(encrypted_text:str,shift:int)->list:
    """
    This function return a list of decrypted character using caesar cipher shift number
    Parameters:
        encrypted_text: string value the encrypted text consists of English letter A-Z
        shift: integer value of the caesar shift number 
    Return:
        list of decrypted character
    """
    decrypted_char_ls = []
    for char in encrypted_text:
        encrypted_char_index = alphabet_character_index[char]
        decrypted_index = (encrypted_char_index - shift) % 26
        decrypted_char = alphabet_table[decrypted_index]
        
        #add the decrypted character to a list 
        decrypted_char_ls.append(decrypted_char)

        #update the shift number
        shift = decrypted_index
    return decrypted_char_ls


def vigenere_cipher(encrypted_text:str,key:str)->list:
    """
    This function return a list of decrypted character using vigenere string as a key 
    Parameters:
        encrypted_tet : string value : the encrypted text consists of English letter A-Z
        key : string value  : vigenere key, which consists of English letter A-Z
    Return: 
        list of decrypted character
    """
    decrypted_char_ls = []
    for char in range(len(encrypted_text)):
        encrypted_char = encrypted_text[char]
        encrypted_char_index = alphabet_character_index[encrypted_char]

        key_char = key[char % len(key)]
        key_char_index = alphabet_character_index[key_char]

        decrypted_index = (encrypted_char_index - key_char_index) % 26
        decrypted_char = alphabet_table[decrypted_index]

        #add decrypted character to a list
        decrypted_char_ls.append(decrypted_char)

    return decrypted_char_ls




def decrypt_cypher(encrypted_text:str,decryption_key:object)->list:
    """
    This function return a list of decrypted character using a either caesar cipher shift number or vigenere string, depending on description key from user
    Parameters:
        encrypted_text : string value : the encrypted text consists of English letter A-Z
        decryption_key : ( integer or str ) int for the caesar shift number / or str for vigenere key
    Return: 
        list of decrypted character
    """
    #change the variable type to string to check if it contains letter
    decryption_key = str(decryption_key)

    if decryption_key.isalpha():
        decryption_key = decryption_key.upper()
        return vigenere_cipher(encrypted_text,decryption_key)
    else:
        caesar_shift = int(decryption_key)
        return caesar_cypher(encrypted_text,caesar_shift)
        
        

# Decrypt text
if __name__ == "__main__":
    # Display preamble
    print("DECRYPT STRING")

    # Get encrypted text and handle cases where encrypted has space and user input lower case
    encrypted_text = input("Input encrypted string: ")
    encrypted_text = encrypted_text.upper()
    encrypted_text = "".join(encrypted_text.split()) 

    # Handle case if user input empty string, program will exist, else it will prompt user to input description key
    if encrypted_text == "":
        print("Empty encrypted string.")
    else:
        decryption_key = input("Input key: ")

        decrypted_char = decrypt_cypher(encrypted_text,decryption_key)

        print("The decrypted string is:")
        for char in decrypted_char:
            print(char)