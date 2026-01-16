import random

# Ask the user to enter their password
password = input("Enter your password: ")

# Check if the password is long enough
if len(password) < 9:
    print("Password too short.")
    exit()

# Ask for three random letters
for i in range(3):
    position = random.randint(1, len(password))
    
    guess = input(f"Enter letter at position {position}: ")

    # Check if the entered letter matches the password
    if guess == password[position - 1]:
        print("Correct")
    else:
        print("Security check failed.")
        exit()

# If all three checks were correct
print("Security check passed.")