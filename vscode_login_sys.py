def login():
    while True:
        username = str(input("What is your username: "))
        password = str(input("What is your password? "))
        if username == "adnan" and password == "vscode77":
            print("Welcome to Replit")
            break
            exit()
        else:
            print("Whoops! I don't recognize that username or password. Try again!")


print("Replit Login System!")
login()
