def welcome_user(game_intro: str) -> str:
    """Print the game introduction and ask for the user's name."""
    print(game_intro)
    print("May I have your name?")
    user_name = input()
    print(f"Hello, {user_name}!")
    return user_name


def ask_question(question: str) -> str:
    """Ask the user a question and return their answer."""
    print(question)
    return input('Your answer: ')
