# User class and Database class to manage users in a simple in-memory database 

class User:
    # User class with user_id and name / Data Model
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

class Database:
    # Store and add remove users / search for users in database / Logic
    def __init__(self):
        self.users = [User(749, "John Will"), User(783, "Peter Cage")] 

    def add_user(self, user): # Add function
        self.users.append(user)

    def search_user(self, user_id): # Search function
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None  
    
    def delete_user(self, user_id): # Deletion function
        for user in self.users:
            if user.user_id == user_id:
                self.users.remove(user)
                return True
        return False
    
# UI function to display users
def main():
    db = Database()

    while True:
        # UI Menu display
        print("\n ++++++ Municipality of Kruzov ++++++")
        print("\n1. Search User")
        print("2. Add User")
        print("3. Delete User")
        print("4. Exit")
        
        try: # To catch invalid input to prevent crashing the program
            choice = int(input("\nPlease select from 1-4: "))

        except ValueError: # Output if user input invalid
            print("Invalid input. Please enter a number between 1 and 4.")
            continue # Then proceed to the program again without crashing

        # Searching user logic
        if choice == 1:
            user_id = int(input("Enter user ID to search: "))
            user = db.search_user(user_id)
            if user:
                print(f"User found: {user.name}")
            else:
                print("User not found.")

        # Adding a user logic
        elif choice == 2:
            user_id = int(input("Enter user ID to add: "))
            name = input("Enter user name to add: ")
            user = User(user_id, name)
            db.add_user(user)
            print("User added successfully.")

        # Deleting a user logic
        elif choice == 3:
            user_id = int(input("Enter user ID to delete: "))
            if db.delete_user(user_id):
                print("User deleted successfully.")
            else:                
                print("User not found.")
        
        elif choice == 4:
            print("...")
            break
        else:
            print("Invalid please select from 1-4.")

if __name__ == "__main__":
    main()
    