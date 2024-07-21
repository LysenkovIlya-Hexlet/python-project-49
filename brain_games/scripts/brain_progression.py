import random
from brain_games.cli import welcome_user, ask_question

def generate_question_and_answer():
    progression_length = random.randint(5, 10)  # Длина прогрессии от 5 до 10
    start = random.randint(1, 20)  # Начальное число прогрессии
    step = random.randint(1, 10)  # Шаг прогрессии

    progression = [start + step * i for i in range(progression_length)]
    missing_index = random.randint(0, progression_length - 1)
    missing_number = progression[missing_index]
    progression[missing_index] = '..'  # Заменяем число на ..

    question = ' '.join(map(str, progression))
    return question, str(missing_number)

def main():
    name = welcome_user('What number is missing in the progression?')
    for _ in range(3):
        question, correct_answer = generate_question_and_answer()
        user_answer = ask_question(question)
        
        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')

if __name__ == '__main__':
    main()
