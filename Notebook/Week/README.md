# Password Security Checker

This program checks if a password is secure by verifying its length and asking for three random letters from it.

All attempts are recorded in a log file.

## How to Run

Open terminal inside the project folder and run:
## How it Works

1. The user enters a password.
2. If the password is shorter than 9 characters, the program exits.
3. If long enough, the program asks for 3 random letters from different positions.
4. If any answer is wrong, the program exits.
5. If all are correct, security is passed.
6. All attempts are saved in `log.txt`.

## Menu

1. New Password Check  
2. View Log File  
3. Exit  

## Files