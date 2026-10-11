
# PLP Python Week 8 Final Project
# Personal Mini-Toolkit

import random


# Tool 1: Simple Calculator
# This tool performs basic arithmetic calculations.
def calculator():
    print("\n===== SIMPLE CALCULATOR =====")

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        operation = input("Choose an operation (1-4): ")

        if operation == "1":
            result = num1 + num2
            print(f"Result: {result}")

        elif operation == "2":
            result = num1 - num2
            print(f"Result: {result}")

        elif operation == "3":
            result = num1 * num2
            print(f"Result: {result}")

        elif operation == "4":
            if num2 != 0:
                result = num1 / num2
                print(f"Result: {result}")
            else:
                print("Sorry, you cannot divide by zero.")

        else:
            print("Invalid operation. Please choose 1-4.")

    except ValueError:
        print("Invalid number. Please enter numbers only.")


# Tool 2: To-Do List Manager
# This tool allows users to add, view, and remove tasks.
def todo_manager(tasks):
    while True:
        print("\n===== TO-DO LIST MANAGER =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Return to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter a new task: ").strip()

            if task:
                tasks.append(task)
                print(f"Task '{task}' added successfully!")
            else:
                print("Task cannot be empty.")

        elif choice == "2":
            if tasks:
                print("\nYour Tasks:")
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")
            else:
                print("Your to-do list is empty.")

        elif choice == "3":
            if tasks:
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")

                try:
                    number = int(input("Enter task number to remove: "))

                    if 1 <= number <= len(tasks):
                        removed = tasks.pop(number - 1)
                        print(f"Task '{removed}' removed successfully!")
                    else:
                        print("Invalid task number.")

                except ValueError:
                    print("Please enter a valid number.")
            else:
                print("There are no tasks to remove.")

        elif choice == "4":
            print("Returning to the main menu.")
            break

        else:
            print(f"Sorry, '{choice}' is not a valid choice.")


# Tool 3: Number Guessing Game
# This tool lets users guess a random number from 1 to 10.
def guessing_game():
    secret_number = random.randint(1, 10)
    attempts = 0

    print("\n===== NUMBER GUESSING GAME =====")
    print("I'm thinking of a number between 1 and 10.")

    while True:
        try:
            guess = int(input("Enter your guess (1-10): "))

            if guess < 1 or guess > 10:
                print("Please enter a number between 1 and 10.")
                continue

            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")

            elif guess > secret_number:
                print("Too high! Try again.")

            else:
                print(f"Congratulations! You guessed correctly in {attempts} attempts!")
                break

        except ValueError:
            print("Invalid input. Please enter a whole number.")


# Welcome message
print("Welcome to the Personal Mini-Toolkit!")

# Store tasks while the program is running
tasks = []

# Keep displaying the main menu until the user quits
while True:
    print("\n===== MAIN MENU =====")
    print("1. Simple Calculator")
    print("2. To-Do List Manager")
    print("3. Number Guessing Game")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        calculator()

    elif choice == "2":
        todo_manager(tasks)

    elif choice == "3":
        guessing_game()

    elif choice == "4":
        print("Thank you for using the Personal Mini-Toolkit. Goodbye!")
        break

    else:
        print(f"Sorry, '{choice}' is not a valid choice. Please try again.")
