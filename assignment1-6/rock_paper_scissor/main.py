import random

def play_game():
    options = ["rock", "paper", "scissors"]
    user_score = computer_score = 0
    print("🪨 Rock, 📄 Paper, ✂️ Scissors - Let's play!")
    
    while True:
        user_choice = input("Choose Rock, Paper or Scissors (or type 'exit' to quit): ").lower()
        
        if user_choice == 'exit':
            print(f"final score - you: {user_score}, computer:{computer_score} \nThanks for playing! 👋")
            break

        if user_choice not in options:
            print("❌ Invalid choice! Please choose rock, paper, or scissors.")
            continue

        computer_choice = random.choice(options)
        print(f"🤖 Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("😐 It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("✅ You win!")
            user_score += 1
        else:
            print("❌ You lose!")
            computer_score += 1


play_game()