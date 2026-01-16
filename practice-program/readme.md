# Password Verification Program

## Program Summary
This program allows a user to enter a password and performs a security check in two steps:

1. **Password Length Check**  
   - The program asks the user to enter a password.  
   - If the password is **less than 9 characters**, it prints `Password too short.` and exits.  

2. **Random Letter Verification**  
   - If the password is long enough, the program randomly selects **three positions** in the password.  
   - The user is asked to enter the letter at each of these positions.  
   - If the user enters any letter incorrectly, the program immediately prints `Security check failed.` and exits.  
   - If all three letters are correct, the program prints `Security check passed.`  

The program uses Python’s `random` module to select positions and basic input/output functions to interact with the user.

---

## How to Use
1. Run the program in Python.  
2. Enter your password when prompted:  
   ```text
   Enter your password:
   --------------------------------------------------------------------------------------------------------------------

# Beckett Pizza Plaza 4-for-3 Offer Program

## Program Summary
This program calculates the total price for a customer ordering four pizzas at Beckett Pizza Plaza (BPP) under the "Four-for-Three" offer.

**How it works:**
1. The user enters the price of **four pizzas**.
2. The program validates each input to ensure it is a **positive number**.
3. The **cheapest pizza is free**, and the total is calculated based on the other three.
4. The program calculates and displays the **discount percentage** and **total amount to pay**.

---

## How to Use
1. Run the program in Python.
2. Enter the price of each pizza when prompted:  
   ```text
   Enter Price of Pizza #1:
   