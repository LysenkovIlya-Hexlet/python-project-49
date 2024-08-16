import prompt

def welcome_user(game_intro):
    print(game_intro)
    print("May I have your name?")
    user_name = input()
    print(f"Hello, {user_name}!")
    return user_name
    
def ask_question(question: str) -> str:
    print(question)
    return input('Your answer: ')