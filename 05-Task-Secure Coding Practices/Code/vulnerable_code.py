import os

# Hardcoded credentials
USERNAME = "admin"
PASSWORD = "12345"

# Unsanitized input
user_input = input("Enter your username: ")
os.system(f"echo Hello, {user_input}")