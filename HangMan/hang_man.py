def gallows(guessNumber):
        if guessNumber == 0:
            print '        '
            return 'You have made ' + str(guessNumber) + ' incorrect guesses.'
        if guessNumber == 1:
            print '        '
            print ' ______ '
            print '        '
            return 'You have had ' + str(guessNumber) + ' incorrect guesses.'
        elif guessNumber == 2:
            print '        '
            print ' ______ '
            print ' |      '
            print '        '
            return 'You have had ' + str(guessNumber) + ' incorrect guesses.'
        elif guessNumber == 3:
            print '        '
            print ' ______ '
            print ' |      '
            print ' |      '
            print '        '
            return 'You have had ' + str(guessNumber) + ' incorrect guesses.'
        elif guessNumber == 4:
            print '        '
            print ' ______ '
            print ' |      '
            print ' |      '
            print ' |      '
            print '        '
            return 'You have had ' + str(guessNumber) + ' incorrect guesses.'
        elif guessNumber == 5:
            print '        '
            print ' ______ '
            print ' |      '
            print ' |      '
            print ' |      '
            print '        '
            return 'You have had ' + str(guessNumber) + ' incorrect guesses.'
        elif guessNumber == 6:
            print '        '
            print ' ______ '
            print ' |      '
            print ' |      '
            print ' |      '
            print '        '
            return 'You have had ' + str(guessNumber) + ' incorrect guesses.'
        elif guessNumber == 7:
            print '        '
            print ' ______ '
            print ' |      '
            print ' |      '
            print ' |      '
            print ' |      '
            print '        '
            return 'You have had ' + str(guessNumber) + ' incorrect guesses.'
        elif guessNumber == 8:
            print '        '
            print ' ______ '
            print ' |    | '
            print ' |      '
            print ' |      '
            print ' |      '
            print '        '
            return 'You have had ' + str(guessNumber) + ' incorrect guesses.'
        elif guessNumber == 9:
            print '        '
            print ' ______ '
            print ' |    | '
            print ' |    0 '
            print ' |      '
            print ' |      '
            print '        '
            return 'You have had ' + str(guessNumber) + ' incorrect guesses.'
        elif guessNumber == 10:
            print '        '
            print ' ______ '
            print ' |    | '
            print ' |    0 '
            print ' |    | '
            print ' |      '
            print '        '
            return 'You have had ' + str(guessNumber) + ' incorrect guesses.'
        elif guessNumber == 11:
            print '        '
            print ' ______ '
            print ' |    | '
            print ' |    0 '
            print ' |   /| '
            print ' |      '
            print '        '
            return 'You have had ' + str(guessNumber) + ' incorrect guesses.'
        elif guessNumber == 12:
            print '        '
            print ' ______ '
            print ' |    | '
            print ' |    0 '
            print ' |   /|\\'
            print ' |      '
            print '        '
            return 'You have had ' + str(guessNumber) + ' incorrect guesses.'
        elif guessNumber == 13:
            print '        '
            print ' ______ '
            print ' |    | '
            print ' |    0 '
            print ' |   /|\\'
            print ' |   /  '
            print '        '
            return 'You have had ' + str(guessNumber) + ' incorrect guesses.'
        elif guessNumber == 14:
            print '        '
            print ' ______ '
            print ' |    | '
            print ' |    0 '
            print ' |   /|\\'
            print ' |   / \\'
            print '        '
            return 'You have had ' + str(guessNumber) + ' incorrect guesses.'

print 'Welcome to Hangman!'
print 'The game will begin now.'
word_to_guess = raw_input('Player 1, please enter a word for player 2 to guess: ')

letters_in_word = list(word_to_guess)

word_length = len(word_to_guess)

while (word_length > 0):
    letter_guessed = raw_input('Player 2, type a letter to guess: ')
    guessNumber = 0
    for letter in letters_in_word:
        if letter_guessed == letter:
            word_length -= 1
            print letter
    if letter_guessed != letter:
        guessNumber += 1
        print gallows(guessNumber)
        
        print word_length
