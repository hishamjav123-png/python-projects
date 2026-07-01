player = input("Rock, Paper or Scissors: ")
computer = "Rock"

print("Computer:", computer)

if player == computer:
    print("Draw")
elif player == "Paper":
    print("You win")
else:
    print("You lose")