import prompt

def welcome_user(game_intro):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game_intro)
    return name
def ask_question(question: str) -> str:
    print(question)
    return input('Your answer: ')