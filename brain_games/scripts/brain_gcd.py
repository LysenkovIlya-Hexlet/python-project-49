import random
import math
from brain_games.engine import play_game


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def generate_question_and_answer():
    """Generate a question and its answer for the GCD game."""
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = f"{num1} {num2}"
    answer = str(math.gcd(num1, num2))
    return question, answer


def main():
    """Run the GCD game."""
    print(DESCRIPTION)
    play_game(generate_question_and_answer)


if __name__ == '__main__':
    main()
