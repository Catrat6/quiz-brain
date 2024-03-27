from question_model import Question
from data import quiz_library
from quiz_brain import QuizBrain
from menu import Menu
import random
import os
# This is a change
def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def fresh_list():
    question_bank = []

    random_set = random.choice(list(quiz_library.values()))

    for question in random_set:
        question_bank.append(Question(question['type'], question['difficulty'], question['category'], question['question'], question['correct_answer'], question['incorrect_answers']))

    return question_bank

while True:
    play_count = 0

    play = input("Would you like to play Quiz Brain? (yes/no)\n")

    question_bank = fresh_list()

    quiz_time = QuizBrain(question_bank)

    if play == 'yes' or play == 'ye' or play == 'y':
        clear_terminal()
        quiz_time.welcome()
        menu = input("Would you like to see the menu for options?")
        clear_terminal()
        if menu == "yes" or menu == "ye" or menu == "y":
            while True:
                clear_terminal()
                menu = Menu()
                menu.menu_options()
                choice = int(input("Make your selection:\n"))
                if choice == 1:
                    menu.current_quiz_list()
                    input("Press Enter to Continue")
                elif choice == 2:
                    menu.current_high_score()
                    input("Press Enter to Continue")
                elif choice == 3:
                    menu.reset_high_score()
                    input("Press Enter to Continue")
                elif choice == 4:
                    break

        while quiz_time.still_has_questions():
            quiz_time.next_question()
        quiz_time.final_readout()
        quiz_time.save_high_score()

    else:
        input('Game Over')
        break








