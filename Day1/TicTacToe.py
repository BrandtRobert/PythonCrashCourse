
def main():
    def check_letters(word, correct_letters, letter_guessed):
        correct_guess = False
        for index, letter in enumerate(word):
            if letter_guessed == letter:
                correct_letters[index] = letter
                correct_guess = True
        return correct_guess


    word = 'hello'.lower()
    game_over = False
    correct_letters = ['_'] * len(word)
    strikes = 3
    while not game_over:
        letter_guessed = input('Guess a letter: ')

        correct_guess = check_letters(word, correct_letters, letter_guessed)

        if not correct_guess:
            print("You didn't guess correctly")
            strikes = strikes - 1
            print(strikes)
        if strikes == 0:
            print('You lose')
            game_over = True
        if '_' not in correct_letters:
            print(correct_letters)
            print('You win!')
            game_over = True

        if not game_over:
            print(correct_letters)

if __name__ == '__main__':
    main()