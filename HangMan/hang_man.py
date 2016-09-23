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

MAX_WRONG = 14
wrong = 0
word_guessed = "_" * word_length
used = []

while (wrong < MAX_WRONG) and (word_guessed != word_to_guess):
    print gallows(wrong)
    print "You've used the following letters: ", used
    print "The word: ", word_guessed

    letter_guessed = raw_input('Player 2, type a letter to guess: ')

    while (letter_guessed in used):
        print "You've already guessed the letter: ", letter_guessed
        letter_guessed = raw_input('Player 2, type a letter to guess: ')

    used.append(letter_guessed)

    if (letter_guessed in word_to_guess):
        letters_left = len(word_to_guess) - 1
        print 'Correct!'

        new = ""
        for i in range(word_length):
            if letter_guessed == letters_in_word[i]:
                new += letter_guessed
            else:
                new += word_guessed[i]
        word_guessed = new
    else:
        print "Sorry, ",letter_guessed, "isn't in the word."
        wrong = wrong + 1

if wrong == 14:
    print gallows(wrong)
    print 'You lost. Too bad.'
else:
    print 'Congratulations, you won.'
