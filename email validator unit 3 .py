import re

# Regular expression pattern for validating an email address
pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

# Get email input from the user
email = input("Enter an email address to validate: ")

# Validate the email using re.match
if re.match(pattern, email):
  print("Valid Email Address!")
else:
  print("Invalid Email Address!")
