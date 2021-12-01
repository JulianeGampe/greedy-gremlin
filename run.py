import random
from prompt_toolkit import prompt 
from prompt_toolkit.completion import WordCompleter
from colorama import Fore

points = 50

def menu():
    """
    Displays the welcome message and asks what the user would like to do
    """
    print("Welcome to the Greedy Gremlin!")
    print("What would you like to do?")
    print("Read game instructions, start playing, exit the game")
    
    menu_completer = WordCompleter(["read", "play", "exit"])

    while True:
        menu_choice = prompt("read, play, exit: ", completer=menu_completer).lower()

        if validate_read_play_exit(menu_choice):
            break
    
    if menu_choice == "read":
        instructions()
    elif menu_choice == "play":
        start_game()
    elif menu_choice == "exit":
        exit()


def validate_read_play_exit(menu_choice):
    """
    Checks if the entry made was "read", "play" or "exit"
    If not it raises a value error
    """
    try:
        if menu_choice != "read" and menu_choice != "play" and menu_choice != "exit":
            raise ValueError

    except:
        print("Please enter 'read', 'play' or 'exit'")
        return False
    
    return True

def instructions():
    """
    Displays the game instructions
    Asks if the user wants to play or exit
    """
    print("-------------------------------------------")
    print("How to play:")
    print("To win the game: Collect 500 points!")
    print("You will play several rounds to achieve that.")
    print("You will start with an initial number of 50 points.")
    print("You will be given a choice between three envelopes:")
    print(f"{Fore.RED}red{Fore.RESET}, {Fore.GREEN}green{Fore.RESET}, {Fore.BLUE}blue{Fore.RESET}.")
    print("One of them contains a positive number of points.")
    print("One contains a negative number of points.")
    print("One contains the Greedy Gremlin, who will take all your points for himself.")
    print("After choosing an envelope the content of one of the others will be revealed.")
    print("You can continue to open your envelope or skip the round\nat the cost of 50 points.")
    print("The game is lost if you open the envelope with the Greedy Gremlin\nor if your score turns negative.")
    print("-------------------------------------------")

    instructions_completer = WordCompleter(["play", "exit"])

    while True:
        instructions_choice = prompt("Would you like to play the game or exit? play/exit: ", completer=instructions_completer).lower()

        if validate_play_exit(instructions_choice):
            break
        
    if instructions_choice == "play":
        start_game()
    elif instructions_choice == "exit":
        exit()


def start_game():
    """
    Starts a new game with an initial 50 points
    """
    print("-------------------------------------------")
    print(f"You have {points} points.")
    print("-------------------------------------------")
    start_new_round(points)

def start_new_round(points):
    """
    Starts a new round of choosing an envelope
    """

    color_completer = WordCompleter(["red", "green", "blue"])

    while True:
        print("Which envelope would you like to open?")
        print(f"{Fore.GREEN}green{Fore.RESET}/{Fore.RED}red{Fore.RESET}/{Fore.BLUE}blue{Fore.RESET}")
        color_one = prompt("", completer=color_completer).lower()

        if validate_color(color_one):
            break
         
    if color_one == "red":
        color_one = f"{Fore.RED}red{Fore.RESET}"
        color_two = f"{Fore.BLUE}blue{Fore.RESET}"
        color_three = f"{Fore.GREEN}green{Fore.RESET}"
    elif color_one == "blue":
        color_one = f"{Fore.BLUE}blue{Fore.RESET}"
        color_two = f"{Fore.RED}red{Fore.RESET}"
        color_three = f"{Fore.GREEN}green{Fore.RESET}"
    elif color_one == "green":
        color_one = f"{Fore.GREEN}green{Fore.RESET}"
        color_two = f"{Fore.BLUE}blue{Fore.RESET}"
        color_three = f"{Fore.RED}red{Fore.RESET}"   
        
 
    positive_amount = random.randint(50, 100)
    negative_amount = random.randint(-100, -20)
    greedy_gremlin = "Greedy Gremlin"
    
    envelope_content = [positive_amount, negative_amount, greedy_gremlin]
    content_one = random.choice(envelope_content)
    envelope_content.remove(content_one)
    content_two = random.choice(envelope_content)
    envelope_content.remove(content_two)
    content_three = envelope_content[0]
    
    chosen_envelope = Envelope(color_one, content_one)
    print(chosen_envelope.color)
    print(chosen_envelope.content)
    second_envelope = Envelope(color_two, content_two)
    print(second_envelope.color)
    print(second_envelope.content)
    third_envelope = Envelope(color_three, content_three)
    print(third_envelope.color)
    print(third_envelope.content)

    print(f"You have chosen the {chosen_envelope.color} envelope.")
    print(second_envelope.open())
    print(f"Would you still like to open the {chosen_envelope.color} envelope?")

    open_skip_completer = WordCompleter(["open", "skip"])

    while True:
        choice = prompt("If not you can skip this round at the cost of 50 points. Enter 'open' or 'skip': ", completer=open_skip_completer).lower()

        if validate_open(choice):
            break

    if choice == "open":
        print(chosen_envelope.open())
        if chosen_envelope.content != "Greedy Gremlin":
            calculate_points(points, chosen_envelope.content)
        else:
            print("-------------------------------------------")
            print("GAME OVER")
            print("-------------------------------------------")
            play_again() 
    else:
        print(chosen_envelope.skip())
        calculate_points(points, -50)
        

def validate_color(color):
    """
    Checks if the entry made was "red", "blue" or "green"
    If not it raises a value error
    """
    try:
        if color != "red" and color != "blue" and color != "green":
            raise ValueError

    except:
        print("Please enter 'red', 'blue' or 'green'.")
        return False
        
    return True
           

def validate_open(choice):
    """
    Checks if the entry made was "open" or "skip"
    If not it raises a value error
    """
    try:
        if choice != "open" and choice != "skip":
            raise ValueError

    except:
        print("Please enter 'open' or 'skip'")
        return False
    
    return True

class Envelope:
    """
    Creates the envelopes
    Sets color, content
    Has a method to open the envelope and to skip the envelope
    """
    def __init__(self, color, content):
        self.color = color
        self.content = content 
        
    def open(self):
        """
        Opens the envelope and reveals the content
        """
        new_line = "\n"
        if self.content == "Greedy Gremlin":
            return f"The {self.color} envelope contains the {self.content}."
        else:
            return f"The {self.color} envelope contains {self.content} points."


    def skip(self):
        """
        Displays the message that the envelope will not be opened and 50 points are deducted
        """
        return "You have chosen to skip the round.\nYour envelope will not be opened.\n50 points will now be deducted from your score."
        

def calculate_points(points, new_points):
    """
    Calculates the number of points after each round
    Displays the result of the round
    """
    points = points + new_points

    if points >= 0 and points < 500:
        print("-------------------------------------------")
        print(f"You have {points} points. You need at least 500 points to win.")
        print("-------------------------------------------")
        play_new_round(points)
    elif points >= 500:
        print("-------------------------------------------")
        print("YOU WON! Congratulation!")
        print("-------------------------------------------")
        play_again()
    else:
        print("-------------------------------------------")
        print(f"Ahhh...you have {points} points. GAME OVER")
        print("-------------------------------------------")
        play_again()

def play_new_round(points):
    """
    Allows the player that has a positive number of points to:
    Start a new round or exit the game
    """
    new_round_completer = WordCompleter(["play", "exit"])

    while True:
        new_round = prompt("Would you like to continue playing the next round or exit the game? play/exit: ", completer=new_round_completer).lower()

        if validate_play_exit(new_round):
            break

    if new_round == "play":
        start_new_round(points)
    else:
        exit()

def play_again():
    """
    Displays after a win or game over
    Allows the player to choose to start a new game or exit
    """

    play_again_completer = WordCompleter(["play", "exit"])

    while True:
        another_game = prompt("Would you like to play again or exit the game? play/exit: ", completer=play_again_completer).lower()

        if validate_play_exit(another_game):
            break

    if another_game == "play":
        print("The Greedy Gremlin is waiting for your points.")
        start_game()
    else:
        exit()

def validate_play_exit(entry):
    """
    Checks if the entry made was "play" or "exit"
    If not it raises a value error
    """    
    try:
        if entry != "play" and entry != "exit":
            raise ValueError

    except:
        print("Please enter 'play' or 'exit'")
        return False
    
    return True


def exit():
    """
    Exits the game completely
    Displays Goodbye message
    """
    print("Thank you for playing! The Greedy Gremlin will try to get your points the next time!")


menu()
