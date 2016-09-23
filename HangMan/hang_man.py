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

guessNumber = 0

letters_guessed_list = []

while (word_length > 0):
    letter_guessed = raw_input('Player 2, type a letter to guess: ')

    for letter in letters_in_word:
        if letter_guessed == letter:
            x = int(letters_in_word.index(letter))
            letters_guessed_list.insert(x, letter)
            word_length = word_length - 1
            print 'Correct! %s more letters to go.' %(word_length)
            break
    if letter_guessed != letter:
        guessNumber = guessNumber + 1
        if guessNumber == 14:
            print gallows(guessNumber)
            print 'You lost. Too bad.'
            break
    letters_guessed_list.sort(key=lambda (x,y): letters_in_word.index(x))
    print gallows(guessNumber)
    print letters_guessed_list
if word_length == 0 and guessNumber < 13:
    print 'Congratulations, you won.'
