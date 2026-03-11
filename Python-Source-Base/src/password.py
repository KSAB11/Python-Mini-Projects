# Password manager

def password_database():

    password = ["096767", "876543", "123456", "123766", "qwerty", "abc123"]
    return password

def check_password(user_input, password):

    if user_input in password:
        return "Password is correct"
    else:
        return "Password is incorrect"
    
def user_input():
    user_input = input("Enter your password: ")
    return user_input

if __name__ == "__main__":
    password = password_database()
    user_input = user_input()
    result = check_password(user_input, password)
    print(result)