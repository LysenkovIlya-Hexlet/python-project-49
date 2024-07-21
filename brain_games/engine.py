import random
import prompt

def welcome_user(game_intro):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game_intro)
    return name

def play_game(generate_question_and_answer):
    name = welcome_user('What is the result of the expression?')
    for _ in range(3):
        question, correct_answer = generate_question_and_answer()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        
        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
    
def generate_question_and_answer():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operation = random.choice(['+', '-', '*'])
    
    if operation == '+':
        answer = num1 + num2
    elif operation == '-':
        answer = num1 - num2
    elif operation == '*':
        answer = num1 * num2
    
    question = f"{num1} {operation} {num2}"
    return question, str(answer)
