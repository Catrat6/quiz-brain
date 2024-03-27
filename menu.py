from quiz_brain import load_high_score
from data import quiz_library

class Menu:

    def __init__(self):
        self.high_score = load_high_score()


    def menu_options(self):
        print('''
        Welcome to the Quiz Brain Menu! 
        enter the number of the option you would like to choose:
        1. See a list of current Quiz's
        2. See the current High Score
        3. Reset the current High Score to 0
        4. Exit menu and start game
        ''')


    def current_quiz_list(self):
        a = quiz_library.keys()

        print("These are the current Quiz's stored in your library:")
        for each in a:
            print(each)

    def current_high_score(self):
        print(self.high_score)

    def reset_high_score(self):
        print(f"Your current high score is {self.high_score}")
        will = input("Will you reset it? (yes/no)\n").lower()

        if will == "yes" or will == "ye" or will == "y":
            with open("high_score.txt", "w") as file:
                file.write(str(0))

