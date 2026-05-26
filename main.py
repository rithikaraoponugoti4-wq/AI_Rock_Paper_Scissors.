import random

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0
draws = 0
round_number = 1

user_history = []


def get_ai_move():
    """
    Simple AI logic:
    The computer checks the user's most used move
    and chooses the move that can beat it.
    """

    if len(user_history) < 3:
        return random.choice(choices)

    most_used = max(set(user_history), key=user_history.count)

    if most_used == "rock":
        return "paper"
    elif most_used == "paper":
        return "scissors"
    else:
        return "rock"


def decide_winner(user, computer):
    if user == computer:
        return "draw"

    if user == "rock" and computer == "scissors":
        return "user"
    elif user == "paper" and computer == "rock":
        return "user"
    elif user == "scissors" and computer == "paper":
        return "user"
    else:
        return "computer"


def display_score():
    print("\nScore Board")
    print("----------------------")
    print(f"User Score     : {user_score}")
    print(f"Computer Score : {computer_score}")
    print(f"Draws          : {draws}")
    print("----------------------")


print("====================================")
print(" AI-Based Rock Paper Scissors Game ")
print("====================================")
print("Enter rock, paper, or scissors")
print("Enter quit to stop the game")

while True:
    print(f"\nRound {round_number}")

    user_choice = input("Enter your choice: ").lower()

    if user_choice == "quit":
        break

    if user_choice not in choices:
        print("Invalid input. Please enter rock, paper, or scissors.")
        continue

    user_history.append(user_choice)

    computer_choice = get_ai_move()

    print(f"You chose      : {user_choice}")
    print(f"Computer chose : {computer_choice}")

    result = decide_winner(user_choice, computer_choice)

    if result == "draw":
        print("Result: It's a draw!")
        draws += 1
    elif result == "user":
        print("Result: You won this round!")
        user_score += 1
    else:
        print("Result: Computer won this round!")
        computer_score += 1

    display_score()
    round_number += 1

print("\n====================================")
print(" Final Game Result ")
print("====================================")

display_score()

if user_score > computer_score:
    print("Final Winner: You won the game!")
elif computer_score > user_score:
    print("Final Winner: Computer won the game!")
else:
    print("Final Result: The game is a tie!")

print("Thank you for playing!")