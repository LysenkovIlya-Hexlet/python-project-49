from brain_games.engine import play_game, generate_question_and_answer


def main():
    """Run the game using the play_game function."""
    play_game(generate_question_and_answer)


if __name__ == '__main__':
    main()
