import random

def play_rock_paper_scissors():
  """Plays a game of Rock-Paper-Scissors against the computer."""

  user_choice = input("Choose Rock, Paper, or Scissors: ").lower()
  possible_actions = ["rock", "paper", "scissors"]
  
  while user_choice not in possible_actions:
    print("Invalid choice. Please choose from Rock, Paper, or Scissors.")
    user_choice = input("Choose again: ").lower()

  computer_choice = random.choice(possible_actions)
  print(f"You chose {user_choice}, computer chose {computer_choice}.\n")

  if user_choice == computer_choice:
    print(f"Both players selected {user_choice}. It's a tie!")
  elif user_choice == "rock":
    if computer_choice == "scissors":
      print("Rock smashes scissors! You win!")
    else:
      print("Paper covers rock! You lose.")
  elif user_choice == "paper":
    if computer_choice == "rock":
      print("Paper covers rock! You win!")
    else:
      print("Scissors cuts paper! You lose.")
  elif user_choice == "scissors":
    if computer_choice == "paper":
      print("Scissors cuts paper! You win!")
    else:
      print("Rock smashes scissors! You lose.")

play_rock_paper_scissors()
