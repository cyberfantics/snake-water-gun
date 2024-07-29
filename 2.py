# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 17:23:23 2024

@author: Mansoor
"""

import random

# Define choices
choices = ['snake', 'water', 'gun']

# Generate the computer's choice
computer_choice_index = random.randint(0, len(choices) - 1)
computer_choice = choices[computer_choice_index]

# Create a mapping from indices to choices
user_choice_mapping = {str(index): choice for index, choice in enumerate(choices)}

# Print choices for the user
print("Choose an option:")
print("\n".join(f"{key}: {value}" for key, value in user_choice_mapping.items()))

# Get the user's choice
user_choice_index = int(input("Enter your choice (0, 1, or 2): "))
user_choice = choices[user_choice_index]

# Define the result matrix and result mapping
result_matrix = [
    ['D', 'W', 'L'],  # Choices: Snake
    ['L', 'D', 'W'],  # Choices: Water
    ['W', 'L', 'D']   # Choices: Gun
]

# Define a lambda function to get the result
get_result = lambda u, c: result_matrix[u][c]

# Determine the result
result = get_result(user_choice_index, computer_choice_index)

# Map results to their meanings
result_mapping = {
    'D': "Match Draw",
    'W': "You Win",
    'L': "You Lose"
}

# Print the result
print(f"{result_mapping[result]}, Because You chose {user_choice} and Computer chose {computer_choice}")
