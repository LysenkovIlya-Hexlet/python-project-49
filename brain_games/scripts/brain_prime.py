import random
import prompt
from brain_games.cli import welcome_user, ask_question

def is_prime(number: int) -> bool:
    """Check if a number is a prime number."""
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_question_and_answer():
    """Generate a question and its answer for the game."""
    number = random.randint(1, 100)
    correct_answer = 'yes' if is_prime(number) else 'no'
    question = str(number)
    return question, correct_answer

def main():
    """Run the prime number game."""
    welcome_user('Answer "yes" if given number is prime. Otherwise answer "no".')
    for _ in range(3):
        question, correct_answer = generate_question_and_answer()
        user_answer = ask_question(f'Question: {question}')
        
        if user_answer.lower() == correct_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again!")
            return
 print(f'Congratulations, {name}!')

if __name__ == '__main__':
    main()
