import random

def welcome_user():
    print("Welcome to the Brain Games!")  # Отладочное сообщение
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    return name

def ask_question():
    number = random.randint(1, 100)
    correct_answer = 'yes' if number % 2 == 0 else 'no'
    print(f"Question: {number}")
    user_answer = input("Your answer: ").strip().lower()
    return user_answer, correct_answer

def main():
    print("In the main function...")  # Отладочное сообщение
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    
    for _ in range(3):
        user_answer, correct_answer = ask_question()
        
        if user_answer != correct_answer:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
        
        print("Correct!")
    
    print(f"Congratulations, {name}!")

if __name__ == "__main__":
    main()
