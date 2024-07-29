# -*- coding: utf-8 -*-
"""
Created on Thu Jul 259 17:54:07 2024

@author: Mansoor
"""

import random

def game_logic(user_choice, computer_choice, choices, user_choice_mapping):
    """
    Determines the result of the game based on user and computer choices.

    Args:
    - user_choice (int): Index of the user's choice.
    - computer_choice (int): Index of the computer's choice.
    - choices (list): List of possible choices.
    - user_choice_mapping (dict): Mapping of choice index to choice name.
    """
    # Result matrix: 'D' for Draw, 'W' for Win, 'L' for Lose
    result_matrix = [
        ['D', 'W', 'L'],  # Choices: Snake
        ['L', 'D', 'W'],  # Choices: Water
        ['W', 'L', 'D']   # Choices: Gun
    ]
    
    # Determine the result of the match
    if user_choice == computer_choice:
        result = "Match Draw"
    elif result_matrix[user_choice][computer_choice] == 'W':
        result = "You Win"
    else:
        result = "You Lose"
    
    # Print the result
    print(f"{result}, Because You chose {user_choice_mapping.get(str(user_choice))} and Computer chose {choices[computer_choice]}")

# Define the available choices
choices = ['snake', 'water', 'gun']

# Randomly select the computer's choice
computer_choice = random.randint(0, len(choices) - 1)

# Map user choice indices to choices
user_choice_mapping = {str(index): choice for index, choice in enumerate(choices)}

# Display options for the user
print("Choose an option:")
for key, value in user_choice_mapping.items():
    print(f'{key}: {value}')

# Get the user's choice
user_choice = int(input("Enter your choice (0, 1, or 2): "))

# Error handling for invalid user input
try:
    # Call the game logic function to determine the result
    game_logic(user_choice, computer_choice, choices, user_choice_mapping)
except Exception as e:
    print(f"Try Again, You Got Error: {e}")
