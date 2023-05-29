import random
import string

def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Generate a password with the default length of 8 characters
password = generate_password()
print(password)

# Generate a password with a specified length of 12 characters
password = generate_password(length=12)
print(password)