# Bank Account Simulator

## Overview
This project is a simple **Bank Account Simulator** written in Python. It allows users to create accounts, deposit money, withdraw money, and check balances through a console-based menu. The program demonstrates **Object-Oriented Programming (OOP)** concepts such as classes, objects, methods, and encapsulation.

## Features
- Create a new bank account with a unique account number  
- Deposit money into an account  
- Withdraw money from an account (with balance validation)  
- Check account balance  
- Console menu with continuous options until the user exits  

## How It Works
- Each account is represented by a `BankAccount` object.  
- The `Bank` class manages multiple accounts using a dictionary, where account numbers are keys.  
- A simple text-based menu runs inside a `while True` loop to continuously interact with the user.  

## Example
Welcome to the Bank Simulator!
Choose an option:
Create Account
Deposit
Withdraw
Check Balance
Exit
Enter choice: 1
Input your name: Terriauna
Your account was created! Your account number is 4827

## Concepts Practiced
- Object-Oriented Programming (classes, objects, methods, attributes)  
- Dictionaries for data storage  
- Loops and input handling  
- Basic error handling (e.g., insufficient funds, invalid account number)  

## How to Run
1. Clone the repository:  
   ```bash
   git clone git@github.com:USERNAME/bank-account-simulator.git
   cd bank-account-simulator
2. Run the python file:
    python3 bankAccount.py
