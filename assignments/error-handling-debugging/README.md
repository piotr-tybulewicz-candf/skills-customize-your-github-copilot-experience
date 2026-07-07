# 📘 Assignment: Error Handling & Debugging in Python

## 🎯 Objective

Learn how to identify, handle, and fix errors in Python programs. You'll practice reading error messages, using try/except blocks to handle exceptions gracefully, and debugging techniques to find and fix bugs in your code.

## 📝 Tasks

### 🛠️ Task 1: Understanding Error Messages

#### Description
You're given a Python script with intentional errors. Read the error messages carefully and fix the code by identifying what went wrong. No try/except blocks needed here—just fix the bugs!

#### Requirements
Your corrected program should:

- Run without any runtime errors
- Correctly perform mathematical operations (division, addition, etc.)
- Handle operations on different data types properly
- Print the correct output for each test case

### 🛠️ Task 2: Handle Exceptions with Try/Except

#### Description
Complete a program that accepts user input and performs operations on it. Use try/except blocks to catch and handle common exceptions like `ValueError`, `ZeroDivisionError`, and `IndexError`. When an exception occurs, display a friendly error message instead of crashing.

#### Requirements
Your program should:

- Accept various types of user input
- Use try/except blocks to catch at least 3 different exception types
- Display helpful error messages that guide the user to fix their input
- Continue running and ask for input again after an error (not crash)
- Successfully process valid input

### 🛠️ Task 3: Build a Robust Input Validator

#### Description
Create a program that validates and processes user data. Implement custom error checking, and use try/except blocks to create a robust application that handles edge cases gracefully.

#### Requirements
Your program should:

- Validate multiple inputs (age, email, phone number, etc.)
- Raise custom `ValueError` exceptions with descriptive messages when validation fails
- Use try/except to catch validation errors and re-prompt the user
- Continue until the user provides valid input for all fields
- Display a summary of the validated data

