import random

print("Welcome to the number guessing!")

secret_number = random.randint(1, 10)
print("I have a secret number between 1 and 10. Can you guess it?")

while True:
    try:
        guess = int(input("Enter your number: "))
        if guess > secret_number:
            print("Too high! Try again.")
        elif guess < secret_number:
            print("Too low! Please try again.")
        else:
            print("🎉 Congratulations! You've guessed the number.")
            break
    except ValueError:
        print("❌ Invalid input. Please enter a number between 1 and 10.")