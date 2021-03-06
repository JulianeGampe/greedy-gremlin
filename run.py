import random
import time
from os import system, name
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from colorama import Fore


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
        sentence = ""
        if self.content == "Greedy Gremlin":
            sentence = f"the {self.content}."
        else:
            sentence = f"{self.content} points."
        return f"The {self.color} envelope contains {sentence}"

    def skip(self):
        """
        Displays the message that the envelope will not be opened
        Displays that 50 points are deducted
        """
        return ("You have chosen to skip the round.\n"
                "Your envelope will not be opened.\n"
                "50 points will now be deducted from your score.")


def clear():
    """
    Clears the screen in Heroku
    Code taken from: https://www.geeksforgeeks.org/clear-screen-python/0
    """
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")


def menu():
    """
    Displays the welcome message and asks what the user would like to do
    """
    clear()
    print("Welcome to the Greedy Gremlin!")
    time.sleep(1)
    print("What would you like to do?")
    time.sleep(1)
    print("Read game instructions, start playing, exit the game")
    time.sleep(1)

    menu_completer = WordCompleter(["read", "play", "exit"])

    while True:
        menu_choice = prompt(
            "read, play, exit: ", completer=menu_completer
            ).lower()

        if validate_read_play_exit(menu_choice):
            break

    if menu_choice == "read":
        instructions()
    elif menu_choice == "play":
        start_game()
    elif menu_choice == "exit":
        exit_game()


def validate_read_play_exit(menu_choice):
    """
    Checks if the entry made was "read", "play" or "exit"
    If not it raises a value error
    """
    try:
        if (
            menu_choice != "read" and menu_choice != "play" and
            menu_choice != "exit"
        ):
            raise ValueError
    except ValueError:
        print("Please enter 'read', 'play' or 'exit'")
        return False

    return True


def instructions():
    """
    Displays the game instructions
    Asks if the user wants to play or exit
    """
    clear()
    print("-------------------------------------------")
    print("How to play Greedy Gremlin:")
    time.sleep(1)
    print("To win the game: Collect 500 points!")
    time.sleep(1.5)
    print("You will play several rounds to achieve that.")
    time.sleep(1.5)
    print("You will start with an initial number of 50 points.")
    time.sleep(1.5)
    print("You will be given a choice between three envelopes:")
    time.sleep(1.5)
    print(f"{Fore.RED}red{Fore.RESET}")
    print(f"{Fore.GREEN}green{Fore.RESET}")
    print(f"{Fore.BLUE}blue{Fore.RESET}")
    time.sleep(1.5)
    print("One of them contains a positive number of points.")
    time.sleep(1.5)
    print("One contains a negative number of points.")
    time.sleep(1.5)
    print("One contains the Greedy Gremlin ????")
    time.sleep(1.5)
    print("who will take all your points for himself.")
    time.sleep(1.5)
    print("After choosing an envelope the content of one of the others")
    time.sleep(1.5)
    print("will be revealed.")
    time.sleep(1.5)
    print("You can continue to open your envelope")
    time.sleep(1.5)
    print("or skip the round at the cost of 50 points.")
    time.sleep(1.5)
    print("The game is lost if you open the envelope with the Greedy Gremlin")
    time.sleep(1.5)
    print("or if your score turns negative.")
    time.sleep(1.5)
    print("-------------------------------------------")
    time.sleep(1.5)

    instructions_completer = WordCompleter(["play", "exit"])

    while True:
        print("Would you like to play the game or exit?")
        instructions_choice = prompt(
            "play/exit: ", completer=instructions_completer
            ).lower()

        if validate_play_exit(instructions_choice):
            break

    if instructions_choice == "play":
        start_game()
    elif instructions_choice == "exit":
        exit_game()


def start_game():
    """
    Starts a new game with an initial 50 points
    """
    clear()

    start_points = 50

    print("-------------------------------------------")
    print(f"You have {start_points} points.")
    print("-------------------------------------------")
    time.sleep(1)
    start_new_round(start_points)


def start_new_round(points):
    """
    Starts a new round of choosing an envelope
    """

    color_completer = WordCompleter(["red", "green", "blue"])

    while True:
        print("Which envelope would you like to open?")
        time.sleep(1)
        print(f"{Fore.GREEN}green{Fore.RESET}")
        print(f"{Fore.RED}red{Fore.RESET}")
        print(f"{Fore.BLUE}blue{Fore.RESET}")

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

    positive_amount = random.randint(250, 400)
    negative_amount = random.randint(-100, -20)
    greedy_gremlin = "Greedy Gremlin"

    envelope_content = [positive_amount, negative_amount, greedy_gremlin]
    content_one = random.choice(envelope_content)
    envelope_content.remove(content_one)
    content_two = random.choice(envelope_content)
    envelope_content.remove(content_two)
    content_three = envelope_content[0]

    chosen_envelope = Envelope(color_one, content_one)
    second_envelope = Envelope(color_two, content_two)
    third_envelope = Envelope(color_three, content_three)

    clear()
    print(f"You have chosen the {chosen_envelope.color} envelope.")
    time.sleep(1)
    print(second_envelope.open())
    time.sleep(1)
    print(
        f"Would you still like to open the {chosen_envelope.color} envelope?"
        )
    time.sleep(1)

    open_skip_completer = WordCompleter(["open", "skip"])

    while True:
        print("If not you can skip this round at the cost of 50 points.")
        choice = prompt(
            "Enter 'open' or 'skip': ", completer=open_skip_completer
            ).lower()

        if validate_open(choice):
            break

    if choice == "open":
        print("-------------------------------------------")
        print(f"The envelope you did not choose is {third_envelope.color}.")
        time.sleep(1.5)
        print(third_envelope.open())
        time.sleep(1.5)
        print(f"The envelope you chose is {chosen_envelope.color}.")
        time.sleep(1)
        print("-------------------------------------------")
        print(chosen_envelope.open())
        time.sleep(1.5)
        if chosen_envelope.content != "Greedy Gremlin":
            calculate_points(points, chosen_envelope.content)
        else:
            print("-------------------------------------------")
            time.sleep(1)
            print("GAME OVER")
            print("   ????   ")
            time.sleep(1)
            print("-------------------------------------------")
            time.sleep(1)
            play_again()
    else:
        print(chosen_envelope.skip())
        time.sleep(1)
        calculate_points(points, -50)


def validate_color(color):
    """
    Checks if the entry made was "red", "blue" or "green"
    If not it raises a value error
    """
    try:
        if color != "red" and color != "blue" and color != "green":
            raise ValueError
    except ValueError:
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
    except ValueError:
        print("Please enter 'open' or 'skip'")
        return False

    return True


def calculate_points(points, new_points):
    """
    Calculates the number of points after each round
    Displays the result of the round
    """
    points = points + new_points
    missing_points = 500 - points

    if points >= 0 and points < 500:
        print("-------------------------------------------")
        print(f"You have {points} points.")
        time.sleep(1)
        print("-------------------------------------------")
        print(f"You still need {missing_points} points")
        print("to reach the goal of 500 points.")
        print("-------------------------------------------")
        time.sleep(1.5)
        play_new_round(points)
    elif points >= 500:
        print(f"You have {points} points.")
        time.sleep(1)
        print("-------------------------------------------")
        time.sleep(1)
        print("YOU WON! Congratulation!")
        print("       ????     ")
        time.sleep(1)
        print("-------------------------------------------")
        time.sleep(1)
        play_again()
    else:
        print("-------------------------------------------")
        print(f"Ahhh...you have {points} points.")
        print("GAME OVER")
        print("   ????   ")
        print("-------------------------------------------")
        time.sleep(1)
        play_again()


def play_new_round(points):
    """
    Allows the player that has a positive number of points to:
    Start a new round or exit the game
    """
    new_round_completer = WordCompleter(["play", "exit"])

    while True:
        print("Would you like to continue playing the next round")
        print("or exit the game completely?")
        new_round = prompt(
            "play/exit: ", completer=new_round_completer
            ).lower()

        if validate_play_exit(new_round):
            break

    if new_round == "play":
        print("-------------------------------------------")
        start_new_round(points)
    else:
        exit_game()


def play_again():
    """
    Displays after a win or game over
    Allows the player to choose to start a new game or exit
    """

    play_again_completer = WordCompleter(["play", "exit"])

    while True:
        print("Would you like to play again or exit the game?")
        another_game = prompt(
            "play/exit: ", completer=play_again_completer
            ).lower()

        if validate_play_exit(another_game):
            break

    if another_game == "play":
        clear()
        print("The Greedy Gremlin is waiting for your points. ????")
        time.sleep(3)
        start_game()
    else:
        exit_game()


def validate_play_exit(entry):
    """
    Checks if the entry made was "play" or "exit"
    If not it raises a value error
    """
    try:
        if entry != "play" and entry != "exit":
            raise ValueError
    except ValueError:
        print("Please enter 'play' or 'exit'")
        return False

    return True


def exit_game():
    """
    Exits the game completely
    Displays Goodbye message
    """
    clear()
    print("Thank you for playing!")
    print("The Greedy Gremlin will try to get your points the next time! ????")


menu()
