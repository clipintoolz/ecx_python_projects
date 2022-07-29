#!/usr/bin/env python3.10

import re

def letter_frequency_analysis(sentence: str) -> None:
    """analyzes a sentence and gets the frequency of each letter excluding punctuations and returns them in a dictionary format
    
    Example:
    ("It is good!") => {"I": 2, "t": 1, "s": 1, "g":1, "o":2, "d":1, "!":1}

    Args:
        sentence (str): sentence to analyze
    """
    
    # dictionary to store letters and their frequency
    letters = {}
    
    # searches for any letter 
    pattern = re.compile(r"[a-zA-Z]")
    matches = pattern.finditer(sentence)
    
    # counts how many times the letter appeared in the senctence and adds the letter to the dictionary as the key while the frequency as the value
    for match in matches:
        start, stop = match.span()
        letter = sentence[start:stop]
        frequency = sentence.count(letter)
        letters[letter] = frequency
    
    print(letters)
    

def word_frequency_analysis(sentence: str) -> None:
    """analyzes a sentence and gets the frequency of each word excluding punctuations and returns them in a dictionary format
    
    Example:
    ("It is not good, is it?") => {"It": 2, "is": 2, "not": 1, "good":1}

    Args:
        sentence (str): sentence to analyze
    """
    
    # dictionary to store words and their frequency
    words = {}
    
    # searches for any word
    pattern = re.compile(r"[a-zA-Z]+")
    matches = pattern.finditer(sentence)
    
    # counts how many times the word appeared in the senctence and adds the word to the dictionary as the key while the frequency as the value
    for match in matches:
        start, stop = match.span()
        word = sentence[start:stop]
        frequency = sentence.count(word)
        words[word] = frequency
    
    print(words)


print()
print(" FREQUENCY ANALYSIS ".center(50, "-"))
print("Select an option\n1. Frequency of letters in sentence\n2. Frequency of words in sentence")
user_input = int(input("-> "))
sentence = input("Enter sentence to analyze: ")

if user_input == 1:
    letter_frequency_analysis(sentence)
elif user_input == 2:
    word_frequency_analysis(sentence)
    