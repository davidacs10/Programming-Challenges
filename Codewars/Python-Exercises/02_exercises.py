"""Can you find the needle in the haystack?
Write a function that takes an full of junk but containing one findNeedle()array"needle"
After your function finds the needle it should return a message (as a string) that says:
"found the needle at position " plus the it found the needle, so: index"""

def find_needle(haystack):
    needle = haystack.index("needle")
    return f"found the needle at position {needle}"

haystack = ["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]
print(find_needle(haystack))

"""Rock Paper Scissors
Let's play! You have to return which player won! In case of a draw return Draw!."""

def rps(p1, p2):
    if p1 == p2:
        return "Draw!"
    elif p1 == "rock" and p2 == "scissors":
        return "Player 1 won!"
    elif p1 == "scissors" and p2 == "paper":
        return "Player 1 won!"
    elif p1 == "paper" and p2 == "rock":
        return "Player 1 won!"        
    else:
        return "Player 2 won!"

print(rps("rock", "paper"))

def rps(p1, p2):
    beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    if beats[p1] == p2:
        return "Player 1 won!"
    if beats[p2] == p1:
        return "Player 2 won!"
    return "Draw!"

print(rps("paper", "rock"))