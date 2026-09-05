

import re

# Regular expression for finding email addresses
email_pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'

# Sample text
text = """
Hello, my name is Neelam.
You can contact me at neelam_23@gmail.com.
My friend Rahul uses rahul_23@gmail.com.
Our college email is student123@college.edu.
"""

# Finding all email addresses from the text
emails = re.findall(email_pattern, text)

print("Email addresses found:")
for email in emails:
    print(email)

# Taking an email from the user
email = input("\nEnter an email address to check: ")

# Checking whether the entered email is valid
if re.fullmatch(email_pattern, email):
    print("Valid email address")
else:
    print("Invalid email address")