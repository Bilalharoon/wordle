
class Wordle:
    word_list:list[str] = [] # pull from somewhere else later
    num_of_guesses:int = 6
    user_guesses_matrix:list[dict[str:int]] = [] # 0 for incorrect, 1 for correct but wrong place, 2 for correct
    user_guess:list[str] = None
    target_word:str = 'blower'
    current_guess_num = 0

    def guess(self, word):
        if len(word) > 6:
            print('word must be less than 6 chars')
            return
        if word == self.target_word:
            print('you win')
            return

        wrd_dict = {}
        for i,j in zip(word, self.target_word):
            if i == j:
                wrd_dict[i] = 2
            elif i in self.target_word:
                wrd_dict[i] = 1
            else:
                wrd_dict[i] = 0
        self.user_guesses_matrix.append(wrd_dict)
        print(self.user_guesses_matrix)
        

wrdle = Wordle()
wrdle.guess('crack')
wrdle.guess('bronze')

