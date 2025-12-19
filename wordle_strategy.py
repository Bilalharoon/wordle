import numpy as np
import random
from typing import List, Tuple
from game import Wordle
import json
import time


class SimpleWordleAgent():
    # match green letters
    # find yellow letters in every other location
    # discard gray letters

    # this agent will try to narrow down the guesses based on the information
    def __init__(self, word_list):
        self.word_list = word_list
        self.banned_letters = []
    def play(self, guess_word, feedback) -> str:
        possible_words = []
        green_letters = list(filter(lambda x: x[1] == 2, feedback))
        yellow_letters = list(filter(lambda x: x[1] == 1, feedback))
        gray_letters = list(filter(lambda x: x[1] == 0, feedback))
        gray_letters = [l[0] for l in gray_letters]
        self.banned_letters += gray_letters
        # print(gray_letters) 

        for word in self.word_list:
            p_feedback = Wordle.get_feedback(word, guess_word)
            
            # green_feedback_letters = list(filter(lambda p: p[0][1]==2 and p[1][1] ==2, zip(p_feedback, feedback)))
            # for x,p in zip(feedback, p_feedback):
                # if x[1] == 2 and p[1] == 2:
                    # print(x, p)
            # print(word, feedback, not any(letter[0] in self.banned_letters for letter in p_feedback))
            if not any([letter[0] in self.banned_letters for letter in p_feedback]):
                # print(word, guess_word, feedback)
                if all([item in p_feedback for item in green_letters]):
                    possible_words.append(word)

            # print(green_feedback_letters, green_letters)
        if len(possible_words) < 1:
            return random.choice(self.word_list)
        self.word_list = possible_words[:]
        # print(f'list length {len(self.word_list)}')
        return random.choice(self.word_list)

               








if __name__ == '__main__':
    possible_word_list = []
    with open('./wordle-list', 'r') as file:
        possible_word_list = json.loads(file.read())
    game_won_count = 0
    for i in range(1000):
        guesses = []
        simpleAgent = SimpleWordleAgent(possible_word_list)
        print('\n')
        print('\n')
        print(f'game {i}')
        word = random.choice(possible_word_list)
        wrdle = Wordle(possible_word_list)
        initial_guess = wrdle.guess(word)
        while not wrdle.win_condition and wrdle.score > 0:
            feedback = wrdle.guess(word)
            guesses.append(word)
            word = simpleAgent.play(word, feedback)
            # print()
            # print(f'guessing word: {word}')
        if wrdle.win_condition:
            print(f'won game {i} with a score of {wrdle.score}')
            print(f'target: {wrdle.target_word}\tguesses:{guesses}')
            game_won_count += 1
        else:
            print('game lost')
            print(f'guesses: {guesses}')
    print(f'Games won out of 100: {game_won_count}')
    


# POP_SIZE = 50
# NUM_GEN = 100


# class WordleStrategy:
#     def __init__(self, initial_guess_idx, w_g, w_y, w_e):
#         self.initial_guess_idx = initial_guess_idx
#         self.w_g = w_g
#         self.w_y = w_y
#         self.w_e = w_e
#         self.fitness = 0.0

#     def caclulate_guess(self, previous_feedback, possible_words):
#         if len(previous_feedback) == 0:
#             return self.initial_guess_idx