HARDCODED_USERNAME = "admin"
HARDCODED_PASSWORD = "password123"

def authenticate():
    username = input("Username: ")
    password = input("Password: ")
    
    if username == HARDCODED_USERNAME and password == HARDCODED_PASSWORD:
        print("Authentication successful!")
        return True
    else:
        print("Invalid credentials!")
        return False
