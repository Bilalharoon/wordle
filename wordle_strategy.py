import numpy as np
import random
from typing import List, Tuple
from game import Wordle
import json
import time


class SimpleWordleAgent():
    # this agent will try to narrow down the guesses based on the information
    def __init__(self, word_list):
        self.word_list = word_list
    def play(self, guess_word, feedback) -> str:
        possible_words = []
        green_letters = list(filter(lambda x: x[1] == 2, feedback))

        # if there are no green letters than pick randomly again
        if len(green_letters) < 1:
            print('no green letters found')
            return random.choice(self.word_list)

        for word in self.word_list:
            p_feedback = Wordle.get_feedback(word, guess_word)
            green_feedback_letters = list(filter(lambda p: p[1]==2, p_feedback))
            green_letters = list(filter(lambda x: x[1]==2, feedback))
            if green_letters == green_feedback_letters:
                possible_words.append(word)
        self.word_list = possible_words[:]
        # print(f'list length {len(self.word_list)}')
        return random.choice(self.word_list)

               








if __name__ == '__main__':
    possible_word_list = []
    with open('./wordle-list', 'r') as file:
        possible_word_list = json.loads(file.read())
    for i in range(10):
        simpleAgent = SimpleWordleAgent(possible_word_list)
        print('\n')
        print('\n')
        print(f'game {i}')
        word = random.choice(possible_word_list)
        wrdle = Wordle(possible_word_list)
        # print(f'target word: {wrdle.target_word}')
        # print()
        # print(f'initial word guess: {word}')
        initial_guess = wrdle.guess(word)
        while not wrdle.win_condition and wrdle.score > 0:
            feedback = wrdle.guess(word)
            word = simpleAgent.play(word, feedback)
            # print()
            # print(f'guessing word: {word}')
        if wrdle.win_condition:
            print(f'won game {i} with a score of {wrdle.score}')
        else:
            print(f'lost game')

    


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