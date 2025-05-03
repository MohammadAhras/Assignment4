import random
print("Welcome to the Hangman")

stages = ['''
---------
    |        |
    |
    |
    |
    |
    --------
''',
'''
    -------
    |       |
    |       O
    |
    |
    |
    --------
    ''',
    '''
    -------
    |       |
    |       O
    |       |
    |
    |
    --------
    ''',
    '''
    --------
    |       |
    |       O
    |      /|
    |
    |
    ---------
    ''',
    '''

    ---------
    |       |
    |       O
    |      /|\\
    |
    |
    --------
    ''',
    '''
    |       |
    |       O
    |      /|\\
    |       /
    |
    ''',
    '''
    --------
    |       |
    |       O
    |      /|\\
    |      / \\
    |
    --------
    ''']

words = ['apple','banana', 'kiwi', 'grapes', 'peace', 'mango', 'berry', 'plum', 'orange']

choosen_word = random.choice(words)
word_display = ['_' for _ in choosen_word]
guest_letter = []
lives = len(stages)

print("Welcome to Hangman!")
print("Guess the Fruits word.")

while True:
    print(" ".join(word_display))
    guess = input("Guess a Letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a valid letter.\n")
        if guess in guest_letter:
            print("You already guessed that letter. try again.\n")
            continue

        guest_letter.append(guess)

        if guess in choosen_word:
            print(f"Good Guess! '{guess}' is in the word")
            for index, letter in enumerate (choosen_word):
                if letter == guess:
                    word_display[index] = guess
        else:
            print(f"Sorry, '{guess}' is not in the word")
            print(stages[len(stages) - lives - 1])
            lives -= 1
            print(f"You have {lives} lives left.")

            if lives == 0:
                print(stages[lives])
                print(f"You Lose! The word was '{choosen_word}'.")
                break

