#ATM SYSTEM DEMO

def main():

    #Virtual database 
    balance = 10000
    password = "1234"
    user_input = ""
    chance = 3
    Attempts = 0


    #Ask user for pin
    while chance > Attempts:
        user_input = input("Enter your PIN: ")
        
        if user_input == password:
            print() #space
            print("Login successful!")
            break
        
        Attempts += 1

    while True:
    
    #Menu display

        print("\n+++ATM MENU+++")
        print("1. Withdraw")
        print("2. Deposit")
        print("3. Check balance")
        print("4. Exit")

    #Ask for user's input
        choice = int(input("\nPlease select from 1-4: "))

    #Process and output
        match choice:
            case 1:
                amount = int(input("Enter amount to withdraw: "))
                total = balance - amount
                print(f"Withdraw amount: {amount}")
            case 2:
                amount = int(input("Enter amount to deposit: "))
                total = balance + amount
                print(f"Deposit Sucessful! New balance: {total}")
            case 3:
                print(f"Total balance: {total}")
            case 4:
                print("Thankyou!")
                break
            case _:
                print("Invalid! please try again.")

if __name__ == "__main__":
    main()
