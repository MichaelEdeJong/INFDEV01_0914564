options = ["rock", "paper", "scissors", "lizard", "spock"]

first_player = "";
second_player = "";
print "Choose the following inputs: rock, paper, scissors, spock, lizard"

while True:
    first_player = raw_input("First player input:")
    if first_player in options:
        break

while True:
    second_player = raw_input("Second player input:")
    if second_player in options:
        break

if (first_player == "rock" and second_player == "scissors"):
     print "Rock crushes Scissors\nFirst player wins"
if (first_player == "rock" and second_player == "lizard"):
     print "Rock crushes Scissors\nFirst player wins"

if (first_player == "paper" and second_player == "rock"):
    print "Paper crushes Rock\nFirst player wins"
if (first_player == "paper" and second_player == "spock"):
    print "Paper crushes Spock\nFirst player wins"

if (first_player == "scissors" and second_player == "paper"):
    print "Scissors cuts Paper\nFirst player wins"
if (first_player == "scissors" and second_player == "lizard"):
    print "Scissors decapitates Lizard\nFirst player wins"

if (first_player == "lizard" and second_player == "spock"):
    print "Lizard poisons Spock\nFirst player wins"
if (first_player == "lizard" and second_player == "paper"):
    print "Lizard eats Paper\nFirst player wins"


if (second_player == "rock" and first_player == "scissors"):
     print "Rock crushes Scissors\nSecond player wins"
if (second_player == "rock" and first_player == "lizard"):
     print "Rock crushes Scissors\nSecond player wins"

if (second_player == "paper" and first_player == "rock"):
    print "Paper crushes Rock\nSecond player wins"
if (second_player == "paper" and first_player == "spock"):
    print "Paper crushes Spock\nSecond player wins"

if (second_player == "scissors" and first_player == "paper"):
    print "Scissors cuts Paper\nSecond player wins"
if (second_player == "scissors" and first_player == "lizard"):
    print "Scissors decapitates Lizard\nSecond player wins"

if (second_player == "lizard" and first_player == "spock"):
    print "Lizard poisons Spock\nSecond player wins"
if (second_player == "lizard" and first_player == "paper"):
    print "Lizard eats Paper\nSecond player wins"
else:
    print "It's a tie!"
