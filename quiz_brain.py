import os
def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
def load_high_score():
    with open("high_score.txt", "r") as file:
        return int(file.read())

class QuizBrain:

    def __init__(self, q_list):
        self.q_num = 0
        self.question_list = q_list
        self.score = 0



    def welcome(self):
        a = self.question_list[1]
        b = self.question_list
        c = load_high_score()
        print("Welcome to QuizBrain")
        print(f"The current high score is: {c}")
        print(f'Todays topic will be "{a.category}" and has a difficulty ranking of "{a.difficulty}"')
        print(f" there are {len(b)} questions")
        print("""
        RULES:
        1. You will get one point for each correct answer and will loose one point for each wrong answer.
        2. Your score can not go lower than 0
        3. A score of zero will NOT end the game, you may still continue.
        """)



    def still_has_questions(self):
        if self.q_num == len(self.question_list):
            return False
        else:
            return True


    def next_question(self):
        a = self.question_list[self.q_num]
        self.q_num += 1
        user_answer = input(f"Q.{self.q_num}: {a.question} (True/False)\n")
        self.check_answer(user_answer, a.answer)
        input("Press enter to continue")
        clear_terminal()

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print('Correct!')
            self.score += 1
            print(f'Your current score is {self.score}')
        else:
            print(f'Wrong, the correct answer is: {correct_answer}')
            if self.score > 0:
                self.score -= 1
            print(f'Your current score is {self.score}')

    def final_readout(self):
        print('Quiz Completed')
        print(f'Your final score is {self.score}/{len(self.question_list)}')



    def save_high_score(self):
        a = load_high_score()

        if self.score > a:
            with open("high_score.txt", "w") as file:
                file.write(str(self.score))
                print(f"You have the new high score of {self.score}, your score has been permanently saved")
                input("Press Enter to Continue")
        else:
            print(f"The high score is {a}, you did not beat it. Try harder next time")
            input("Press Enter to continue")

