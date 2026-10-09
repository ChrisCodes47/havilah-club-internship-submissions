# Day 11 — Introduction to Python
# Task: Complete exercises on variables, data types, operators, and basic input/output.
# Submit this .py file with all working programs.

# ── Exercise 1: Variables and Data Types ─────────────────────────────────────
# Create variables of 4 different types: string, integer, float, and boolean.
# Print all of them with descriptive labels.

# TODO: your code here
my_string = "Python Code"
my_integer = 77
my_float = 74.3
my_boolean = False

print("String value:", my_string)
print("Integer value:", my_integer)
print("Float value:", my_float)
print("Boolean value:", my_boolean)


# ── Exercise 2: Temperature Converter ────────────────────────────────────────
# Ask the user to enter a temperature in Celsius, then print the Fahrenheit equivalent.
# Also convert in the opposite direction (Fahrenheit to Celsius).

# TODO: your code here
celsius_input = float(input("Enter a temperature in Celsius: "))
fahrenheit_calc = (celsius_input * 9/5) + 32
print(f"{celsius_input}°C is equal to {fahrenheit_calc}°F")

fahrenheit_input = float(input("\nEnter a temperature in Fahrenheit: "))
celsius_calc = (fahrenheit_input - 32) * 5/9
print(f"{fahrenheit_input}°F is equal to {celsius_calc}°C")


# ── Exercise 3: Age Calculator ────────────────────────────────────────────────
# Ask for the user's name and birth year.
# Calculate and print their current age and the year they will turn 30.

# TODO: your code here

from datetime import date

name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))

current_year = date.today().year
current_age = current_year - birth_year
year_turning_30 = birth_year + 30

print(f"{name}, you are turning {current_age} this year.")
print(f"You will turn 30 in the year {year_turning_30}.")