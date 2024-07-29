# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 23:01:34 2024

@author: Mansoor
"""

import random

class SnakeWaterGame:
    def __init__(self):
        self.choices = ['snake', 'water', 'gun']
        self.result_matrix = [
            ['D', 'W', 'L'],  # Choices: Snake
            ['L', 'D', 'W'],  # Choices: Water
            ['W', 'L', 'D']   # Choices: Gun
        ]
        self.result_mapping = {
            'D': "Match Draw",
            'W': "You Win",
            'L': "You Lose"
        }

    def get_computer_choice(self):
        return random.choice(self.choices)

    def get_user_choice(self):
        print("Choose an option:")
        for index, choice in enumerate(self.choices):
            print(f"{index}: {choice}")
        user_index = int(input("Enter your choice (0, 1, or 2): "))
        return user_index

    def determine_result(self, user_index, computer_choice):
        computer_index = self.choices.index(computer_choice)
        result_code = self.result_matrix[user_index][computer_index]
        return self.result_mapping[result_code]

    def play(self):
        computer_choice = self.get_computer_choice()
        user_index = self.get_user_choice()
        user_choice = self.choices[user_index]
        
        result = self.determine_result(user_index, computer_choice)
        print(f"{result}, Because You chose {user_choice} and Computer chose {computer_choice}")

if __name__ == "__main__":
    game = SnakeWaterGame()
    game.play()
