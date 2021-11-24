import random

points = 50

def start_game():
    """
    Starts a new game with an initial 50 points
    Displays game instructions
    """
    print("Welcome to the Greedy Gremlin!")
    print("How to play:")
    print("To win the game: Collect 500 points!")
    print("You will play several rounds to achieve that.")
    print("You will start with an initial number of 50 points.")
    print("You will be given a choice between three envelopes: red, green, blue.")
    print("One of them contains a positive number of points.")
    print("One contains a negative number of points.")
    print("One contains the Greedy Gremlin, who will take all your points for himself.")
    print("After choosing an envelope the content of one of the others will be revealed.")
    print("You can continue to open your envelope or skip the round\nat the cost of 50 points.")
    print("The game is lost if you open the envelope with the Greedy Gremlin\nor if your score turns negative.")
    print("-------------------------------------------")
    print(f"You have {points} points.")
    print("-------------------------------------------")
    start_new_round(points)

def start_new_round(points):
    """
    Starts a new round of choosing an envelope
    """
    pass

class Envelope:
    """
    Creates the envelopes
    Sets color, content
    Has a method to open the envelope and to skip the envelope
    """
    pass

def calculate_points():
    """
    Calculates the number of points after each round
    """
    pass

def play_new_round():
    """
    Allows the player that has a positive number of points to:
    Start a new round or exit the game
    """
    pass

def play_again():
    """
    Displays after a win or game over
    Allows the player to choose to start a new game or exit
    """
    pass

def exit():
    """
    Exits the game completely
    Displays Goodbye message
    """
    pass

def main():
    """
    Runs all program functions
    """
    start_game()

main()
