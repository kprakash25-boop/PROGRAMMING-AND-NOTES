import random
# The random module is used to select random positions from the password

# --------------------------------------------------
# PROGRAM START
# --------------------------------------------------

# Ask the user to enter their password
password = input("Enter your password: ")
# The password entered by the user is stored as a string

# --------------------------------------------------
# PASSWORD LENGTH CHECK
# --------------------------------------------------

# Check if the password is long enough
if len(password) < 9:
    # len() counts the number of characters in the password
    
    print("Password too short.")
    # Inform the user that the password does not meet requirements
    
    exit()

# Ask for three random letters
for i in range(3):
    position = random.randint(1, len(password))
    # Randomly choose a position within the password length
    
    guess = input(f"Enter letter at position {position}: ")

    # Check if the entered letter matches the password
    if guess == password[position - 1]:
        print("Correct")
        # Inform the user that the answer is correct
        
    else:
        # This block runs if the user makes a mistake
        
        print("Security check failed.")
        # Display failure message
        
        exit()
        # Exit immediately if any answer is wrong

# --------------------------------------------------
# SUCCESS MESSAGE
# --------------------------------------------------

# If all three checks were correct
print("Security check passed.")
# Final confirmation message

# --------------------------------------------------
# PROGRAM END
# --------------------------------------------------