#!/usr/bin/env python3.10

import string


def cipher_encrypt(word: str, shift: int) -> str:
    """encrypts a word or sentence by moving backward or forward the alphabets by specified shift and replacing each letter in word or sentence with letter at shifted position

    Args:
        word (str): word to encrypt
        shift (int): number of times to move back or front (negative shift means backward and positive shift means forward)

    Returns:
        str: encrypted word or sentence
    """
    
    
    encrypted_word_list = []
    if shift == 0:
        return word
    
    elif shift > 0:        # If shift is positive then move forward the alphabet list
        for letter in word:
            if letter in string.ascii_lowercase:    # If letter is lowercase
                # If the shift is more than the alphabet then continue count from 1st alphabet like a cycle
                
                if shift <= (122 - ord(letter)):   # Get the unicoode code point instead of using alphabets string
                    letter = ord(letter) + shift
                    encrypted_word_list.append(str(chr(letter))) # converts unicode to string
                    
                else:
                    letter = (shift - (122 - ord(letter))) + 96
                    encrypted_word_list.append(str(chr(letter)))
                    
            elif letter in string.ascii_uppercase:     # If letter is uppercase
                if shift <= (90 - ord(letter)):
                    letter = ord(letter) + shift
                    encrypted_word_list.append(str(chr(letter)))
                    
                else:
                    letter = (shift - (90 - ord(letter))) + 64
                    encrypted_word_list.append(str(chr(letter)))
                    
            else:
                encrypted_word_list.append(letter)
                
    else:           
        shift *= -1       
        for letter in word:
            if letter in string.ascii_lowercase:    
                if shift <= (ord(letter) - 97):
                    letter = ord(letter) - shift
                    encrypted_word_list.append(str(chr(letter)))
                    
                else:
                    letter = 123 - (shift - (ord(letter) - 97))
                    encrypted_word_list.append(str(chr(letter)))
                    
            elif letter in string.ascii_uppercase:     
                if shift <= (ord(letter) - 65):
                    letter = ord(letter) - shift
                    encrypted_word_list.append(str(chr(letter)))
                    
                else:
                    letter = 91 - (shift - (ord(letter) - 65))
                    encrypted_word_list.append(str(chr(letter)))
                    
            else:
                encrypted_word_list.append(letter)

    encrypted_word = "".join(encrypted_word_list)
    return encrypted_word


def cipher_decrypt(word: str, encryption_shift: int) -> str:
    """decrypts a word or sentence by moving backward or forward the alphabets by encryption shift and replacing each letter in word or sentence with letter at shifted position

    Args:
        word (str): word to decrypt
        encrytion_shift (int): shift used by the encryption

    Returns:
        str: _description_
    """
    
    decrypted_word_list = []
    if encryption_shift == 0:
        return word
    
    elif encryption_shift < 0:
        encryption_shift *= -1
        for letter in word:
            if letter in string.ascii_lowercase:
                if encryption_shift <= (122 - ord(letter)):
                    letter = ord(letter) + encryption_shift
                    decrypted_word_list.append(str(chr(letter)))
                    
                else:
                    letter = (encryption_shift - (122 - ord(letter))) + 96
                    decrypted_word_list.append(str(chr(letter)))
                    
            elif letter in string.ascii_uppercase:
                if encryption_shift <= (90 - ord(letter)):
                    letter = ord(letter) + encryption_shift
                    decrypted_word_list.append(str(chr(letter)))
                    
                else:
                    letter = (encryption_shift - (90 - ord(letter))) + 64
                    decrypted_word_list.append(str(chr(letter)))
                    
            else:
                decrypted_word_list.append(letter)
                
    else:
        for letter in word:
            if letter in string.ascii_lowercase:
                if encryption_shift <= (ord(letter) - 97):
                    letter = ord(letter) - encryption_shift
                    decrypted_word_list.append(str(chr(letter)))
                    
                else:
                    letter = 123 - (encryption_shift - (ord(letter) - 97))
                    decrypted_word_list.append(str(chr(letter)))
                    
            elif letter in string.ascii_uppercase:
                if encryption_shift <= (ord(letter) - 65):
                    letter = ord(letter) - encryption_shift
                    decrypted_word_list.append(str(chr(letter)))
                    
                else:
                    letter = 91 - (encryption_shift - (ord(letter) - 65))
                    decrypted_word_list.append(str(chr(letter)))
                    
            else:
                decrypted_word_list.append(letter)

    decrypted_word = "".join(decrypted_word_list)
    return decrypted_word


print()
print(" CIPHER ENCRYPTION ".center(50, "-"))
user_selection = int(input(
    "Select an option\n1. Encrypt word or Sentence\n2. Decrypt word or sentence\n-> "))

if user_selection == 1:
    print()
    words = input("Enter a word or sentence to encrypt: ")
    shift = int(input("Enter shift: "))
    encrypted_word_list = []

    for word in words.split():
        encrypted_word = cipher_encrypt(word, shift)
        encrypted_word_list.append(encrypted_word)

    encrypted_words = " ".join(encrypted_word_list)
    print(encrypted_words)

elif user_selection == 2:
    print()
    words = input("Enter a word or sentence to decrypt: ")
    encryption_shift = int(input("Enter encryption shift: "))
    decrypted_word_list = []

    for word in words.split():
        decrypted_word = cipher_decrypt(word, encryption_shift)
        decrypted_word_list.append(decrypted_word)

    decrypted_words = " ".join(decrypted_word_list)
    print(decrypted_words)
