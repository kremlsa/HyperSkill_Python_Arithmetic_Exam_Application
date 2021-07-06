# write your code here
import random
import string


class EasyMode:
    equation = None

    def __init__(self):
        self.operations = ['+', '-', '*']
        self.digits = string.digits[2:]

    def get_question(self):
        self.equation = [random.choice(self.digits), random.choice(self.operations), random.choice(self.digits)]
        return " ".join(self.equation)

    def check_answer(self, answer_):
        if self.equation[1] == '+':
            if answer_ == int(self.equation[0]) + int(self.equation[2]):
                return True
            else:
                return False
        if self.equation[1] == '-':
            if answer_ == int(self.equation[0]) - int(self.equation[2]):
                return True
            else:
                return False
        if self.equation[1] == '*':
            if answer_ == int(self.equation[0]) * int(self.equation[2]):
                return True
            else:
                return False


class ExpertMode:
    equation = None

    def __init__(self):
        self.digits = [x for x in range(11, 30)]

    def get_question(self):
        self.equation = random.choice(self.digits)
        return self.equation

    def check_answer(self, answer_):
        if answer_ == self.equation * self.equation:
            return True
        else:
            return False


def check_format():
    while True:
        try:
            return int(input())
        except ValueError:
            print("Incorrect format.")
            continue


def check_mode():
    while True:
        choice_ = input()
        if choice_ == '1':
            return EasyMode()
        if choice_ == '2':
            return ExpertMode()
        else:
            print("Incorrect format.")
            continue


right_answers = 0
rounds = 5
print("""Which level do you want? Enter a number:
1 - simple operations with numbers 2-9
2 - integral squares of 11-29""")
mode = check_mode()

for _ in range(0, rounds):
    print(mode.get_question())
    answer = check_format()
    if mode.check_answer(answer):
        print("Right!")
        right_answers += 1
    else:
        print("Wrong!")
print("Your mark is {}/{}. Would you like to save the result? Enter yes or no.".format(right_answers, rounds))
answer = input()
if answer in ["yes", "YES", "Y", "y", "Yes"]:
    print("What is your name?")
    name = input()
    result = None
    if str(mode.__class__).__contains__("EasyMode"):
        result = "{}: {}/{} in level 1 (simple operations with numbers 2-9)."\
            .format(name, right_answers, rounds)
    if str(mode.__class__).__contains__("ExpertMode"):
        result = "{}: {}/{} in level 2 (integral squares of 11-29)."\
            .format(name, right_answers, rounds)
    with open("results.txt", "a") as file:
        file.write(result)
    print('The results are saved in "results.txt".\n')
