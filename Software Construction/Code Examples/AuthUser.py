
users = {}

def register():
    username = input("Enter username: ")
    password = input("Enter password: ")
    users[username] = password
    print("Registration successful!")

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in users and users[username] == password:
        print("Login successful!")
    else:
        print("Invalid credentials")
# Main program
while True:
    print("\n1. Register\n2. Login\n3. Exit")
    choice = input("Enter choice: ")
    
    if choice == '1':
        register()
    elif choice == '2':
        login()
    elif choice == '3':
        break
    else:
        print("Invalid option")
