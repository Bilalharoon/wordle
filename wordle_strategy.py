import numpy as np
import random
from typing import List, Tuple
from game import Wordle
import json
import time

NUM_OF_GAMES = 1000
class SimpleWordleAgent():
    # match green letters
    # find yellow letters in every other location
    # discard gray letters

    # this agent will try to narrow down the guesses based on the information
    def __init__(self, word_list):
        self.word_list = word_list
        self.included_letters = []
        self.banned_letters = []
        self.guesses = []
    def play(self, guess_word, feedback) -> str:
        possible_words = []
        green_letters = list(filter(lambda x: x[1] == 2, feedback))
        yellow_letters = list(filter(lambda x: x[1] == 1, feedback))
        self.included_letters += list([l[0] for l in green_letters] + [l[0] for l in yellow_letters])
        self.included_letters = list(set(self.included_letters))
        gray_letters = list(filter(lambda x: x[1] == 0, feedback))
        # gray_letters = [l[0] for l in gray_letters if l not in self.included_letters]
        # print(gray_letters) 

        for word in self.word_list:
            p_feedback = Wordle.get_feedback(word, guess_word)
            
            # green_feedback_letters = list(filter(lambda p: p[0][1]==2 and p[1][1] ==2, zip(p_feedback, feedback)))
            # for x,p in zip(feedback, p_feedback):
                # if x[1] == 2 and p[1] == 2:
                    # print(x, p)
            # print(word, feedback, not any(letter[0] in self.banned_letters for letter in p_feedback))
            if all(letter in word for letter in self.included_letters) and (word not in self.guesses):
                # print(word, guess_word, feedback)
                if len(green_letters) > 0:
                    if all([item in p_feedback for item in green_letters]):
                        possible_words.append(word)
                else:
                    possible_words.append(word)

            # print(green_feedback_letters, green_letters)
        # if len(possible_words) < 1:
            # return random.choice(self.word_list)
        # print(len(possible_words))
        self.word_list = possible_words[:]
        # print(f'list length {len(self.word_list)}')
        word_choice = random.choice(self.word_list)
        self.guesses.append(word_choice)
        # print(self.guesses)
        return word_choice

               

if __name__ == '__main__':
    possible_word_list = []
    with open('./wordle-list', 'r') as file:
        possible_word_list = json.loads(file.read())
    game_won_count = 0
    for i in range(NUM_OF_GAMES):
        guesses = []
        simpleAgent = SimpleWordleAgent(possible_word_list)
        print('\n')
        print('\n')
        print(f'game {i}')
        # word = random.choice(possible_word_list)
        word = 'aides'
        simpleAgent.guesses.append(word)
        wrdle = Wordle(possible_word_list)
        print(f'target word: {wrdle.target_word}')
        initial_guess = wrdle.guess(word)
        feedback = wrdle.guess(word)
        while not wrdle.win_condition and wrdle.score > 0:
            guesses.append(word)
            # print(wrdle.target_word in simpleAgent.word_list)
            word = simpleAgent.play(word, feedback)
            feedback = wrdle.guess(word)
            # print()
            # print(f'guessing word: {word}')
        if wrdle.win_condition:
            print(f'won game {i} with a score of {wrdle.score}')
            game_won_count += 1
        else:
            print('game lost')
        print(f'target: {wrdle.target_word}\tguesses:{guesses}')
        # print(simpleAgent.included_letters)
    print(f'Games won out of {NUM_OF_GAMES}: {game_won_count}')
    


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