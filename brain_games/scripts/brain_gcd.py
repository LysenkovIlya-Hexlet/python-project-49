import random
import math
from brain_games.cli import welcome_user, ask_question
from brain_games.engine import play_game

DESCRIPTION = 'Find the greatest common divisor of given numbers.'

def generate_question_and_answer():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = f"{num1} {num2}"
    answer = str(math.gcd(num1, num2))
    return question, answer

def main():
    print(DESCRIPTION)
    play_game(generate_question_and_answer)

if __name__ == '__main__':
    main()