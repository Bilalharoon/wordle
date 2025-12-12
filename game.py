
class Wordle:
    word_list:list[str] = [] # pull from somewhere else later
    num_of_guesses:int = 6
    user_guesses_matrix:list[list[tuple]] = [] # 0 for incorrect, 1 for correct but wrong place, 2 for correct
    user_guess:list[str] = []
    target_word:str = 'black'
    current_guess_num = 0
    win_condition = False
    score = 6
    def guess(self, word):
        if word == self.target_word:
            self.win_condition = True
            print('you win')
            return

        word_list:list[tuple] = []
        for i,j in zip(word, self.target_word):
            if i == j:
                word_list.append((i, 2))
            elif i in self.target_word:
                word_list.append((i, 1))
            else:
                word_list.append((i, 0))
        self.user_guesses_matrix.append(word_list)
        self.score -= 1
        print(self.user_guesses_matrix)

    def prompt_guess(self):
        if len(self.user_guess) == 6:
            self.win_condition = True
            print('game over')
            return
        guess = input('Guess the five letter word: ')    
        if len(guess) != 5:
            print('you need to input a five letter word')
            self.prompt_guess()
        else:
            self.user_guess.append(guess)
            self.guess(guess) 



    
        
if __name__ == '__main__':
    wrdle = Wordle()
    while wrdle.win_condition == False:
        wrdle.prompt_guess()

