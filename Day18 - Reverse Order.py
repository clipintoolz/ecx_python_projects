#!/usr/bin/env python3.10

import re

def reverse_order(sentence: str) -> None:
    """reverses each word in a sentence but not punctuations

    Args:
        sentence (str): word or sentence to reverse
    """
    
    # finds any word in the sentence and skips anything other than a letter
    pattern = re.compile(r"[a-zA-Z]+")
    matches = pattern.finditer(sentence)
    
    # storing the words from the sentence in a list for easy replacement
    sentence_list = list(sentence)
    
    # replaces the original word from sentence list with reversed word
    for match in matches:
        start, stop = match.span()
        word_to_replace = sentence_list[start:stop]
        reversed_word = word_to_replace[::-1]
        sentence_list[start:stop] = reversed_word
        
    print("".join(sentence_list))
    
    
print()
print(" STRING REVERSER ".center(50, "-"))
user_input = input("Enter a word or sentence to reverse\n-> ")
reverse_order(user_input)



    
