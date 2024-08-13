import bcrypt

def hash_password_fixed_salt(password):
    # Use a fixed salt (22 characters long, base64 encoded)
    fixed_salt = b'$2b$12$abcdefghijk1234567890uv'

    # Hash the password using the fixed salt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), fixed_salt)
    
    return hashed_password

# Example usage
password = input("Enter the password you wish to encrypt: ")
hashed_password = hash_password_fixed_salt(password)
print("Hashed password:", hashed_password.decode('utf-8'))
