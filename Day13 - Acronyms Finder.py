#!/usr/bin/env python3.10

import re

print()
print(" ACRONYM FINDER ".center(50,"-"))
user_input = input("Enter a sentence containing one or more acronyms (in uppercase)\n-> ")

# pattern to search for (any word that is all uppercase)
acronym_pattern = re.compile(r"[A-Z]+")

# searches for all uppercase words in user_input and returns an iterator containing them
acronym_matches = acronym_pattern.finditer(user_input)

# list to put all acronyms found
acronyms = []

# extract acronyms from acronym_matches iterator and add them to acronyms list 
for acronym in acronym_matches:
    start, stop = acronym.span()
    acronym_word = user_input[start:stop]
    acronyms.append(acronym_word)

print()
print(f"Here is the list of acronyms in your sentence\n{acronyms}")