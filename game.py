import json
import random
class Wordle:

    def __init__(self, word_list, target_word=None):
        self.word_list = word_list
        self.target_word = target_word if target_word else random.choice(word_list)
        self.win_condition = False
        self.score = 6

    @classmethod
    def get_feedback(self, word, target_word):
        guess_list = list(word)
        target_list = list(target_word)
        feedback:list[tuple] = []
        target_counts = {l: target_word.count(l) for l in target_word}
        
        for i in range(5):
            letter = guess_list[i]
            target_letter = target_list[i]
            if letter == target_letter:
                feedback.append((letter, 2))
                target_counts[letter] -= 1
            elif letter in target_word and target_counts.get(letter, 0) > 0:
                feedback.append((letter, 1))
                target_counts[guess_list[i]] -= 1
            else:
                feedback.append((letter, 0))
        return feedback


    def guess(self, word: str) -> list[tuple[str, int]]:

        if self.win_condition or self.score < 0:
            return []

        if word == self.target_word:
            self.win_condition = True
            self.score -= 1
            return [(l, 2) for l in word]

        feedback = self.get_feedback(word, self.target_word)
        self.score -= 1
        return feedback

    def get_status(self) -> tuple[bool, bool, int]:
        is_won = self.win_condition
        is_lost = (self.score < 0 and not is_won)
        return is_won, is_lost, self.score



    
        
if __name__ == '__main__':
    possible_world_list = []
    with open('./wordle-list', 'r') as file:
        possible_world_list = json.loads(file.read())

    
    for i in range(1000):
        wrdle = Wordle(possible_world_list)
        guesses = []
        while not wrdle.win_condition and wrdle.score > 0:
            guess_word = random.choice(wrdle.word_list)
            wrdle.guess(guess_word)
            guesses.append(guess_word)
        is_won, is_lost, score = wrdle.get_status()
        if is_won:
            print(f'game {i} won with a score of {score}')
            print(f'target: {wrdle.target_word}\tguesses: {guesses}')

