#!/usr/bin/env python3.10

import re

print()
print(" EMAIL ADDRRESS CHECKER ".center(50, "-"))
no_of_email = int(input("How many emails would you like to enter: "))

# list to keep all emails the user inputs
emails = []

for no in range(no_of_email):
    email = input("Enter email: ")
    emails.append(email)

# concatenates all emails in email listto one string to perform some regex search
emails_string = "\n".join(emails)

# pattern to search for in the email string
student_email_pattern = re.compile(r"\w+(@student.college.edu)")
professor_email_pattern = re.compile(r"\w+(@prof.college.edu)")

# returns an iterator containing matches found from email string
student_matches = student_email_pattern.finditer(emails_string)
professor_matches = professor_email_pattern.finditer(emails_string)

# turns iterator to list and finds the number of emails in them
student_no_of_email = len(list(student_matches))
professor_no_of_email = len(list(professor_matches))

print()
print(f"Student Email Number: {student_no_of_email}\nProfessor Email Number: {professor_no_of_email}")