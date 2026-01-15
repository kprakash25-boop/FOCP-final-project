import sys
import random
import datetime

# --------------------------------------------------
# Command line file argument
# --------------------------------------------------
if len(sys.argv) != 2:
    print("Usage: python password_check.py log.txt")
    exit()

log_file = sys.argv[1]

# --------------------------------------------------
# Functions
# --------------------------------------------------

def save_log(message):
    with open(log_file, "a") as file:
        file.write(message + "\n")


def get_password():
    return input("Enter your password: ")


def check_length(password):
    if len(password) < 9:
        print("Password too short.")
        save_log("FAILED - Password too short")
        return False
    return True


def ask_random_letter(password, number):
    position = random.randint(1, len(password))
    user_input = input(f"Enter letter at position {position}: ")

    correct_letter = password[position - 1]

    if user_input == correct_letter:
        print("Correct")
        save_log(f"Check {number}: position {position} correct")
        return True
    else:
        print("Security check failed.")
        save_log(f"Check {number}: position {position} FAILED")
        return False


def show_menu():
    print("\nPassword Security System")
    print("========================")
    print("1. New Password Check")
    print("2. View Log File")
    print("3. Exit")


def view_log():
    try:
        with open(log_file, "r") as file:
            print("\n--- LOG FILE ---")
            print(file.read())
    except:
        print("No log file found.")


def run_security_check():
    password = get_password()

    if not check_length(password):
        return

    save_log("Password accepted, length OK")

    for i in range(1, 4):
        if not ask_random_letter(password, i):
            save_log("Security check FAILED")
            return

    print("Security check passed.")
    save_log("Security check PASSED")


# --------------------------------------------------
# Main Program Loop
# --------------------------------------------------

while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        run_security_check()

    elif choice == "2":
        view_log()

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")