import random
print("Welcome to the Number Guessing Game!")

low = 1
high = 10

print("Think of a Number between 1 to 10 and computer will be guess it.")

if low <= high:
    guess = random.randint(low,high)
    print("Computer's Guess it: ", guess)

    while True:
        feedback = input('Is the guess to High (H), too Low(L), or correct (C)').strip().upper()

        if feedback == 'C':
            print('Yah! the Computer guess your number is Correctly.')
            break
        elif feedback == 'H':
            high = guess - 1 
            guess = random.randint(low,high)
            print("Computer's guess is: ", guess)
        elif feedback =="L":
            low = guess + 1
            guess = random.randint(low,high)
            print("Computer's guess is: ", guess)
        else:
            print("Invalid input. Please enter H,L or C.")
if low > high:
    print("The number is not in the range. Please try again.")
    