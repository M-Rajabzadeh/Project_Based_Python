import random

class RockPaperScissors():
    """
    Main class for the game Rock, Paper, Scissors
    """

    def __init__(self) -> None:
        self.choices: list[str] = ['rock', 'paper', 'scissors']

    def get_user_choice(self) -> str:
        """
        Prompts the user to enter their choice and validates it.

        Returns:
            str: The user's valid choice.
        """
        user_choice: str = input('Enter your choice (rock, paper, scissors): ')
        if user_choice.lower() in self.choices:
            return user_choice.lower()
        else:
            print('Invalid input. Please enter rock, paper, or scissors.')
            return self.get_user_choice()

    def computer_choice(self) -> str:
        """
        Randomly selects and returns the computer's choice.

        Returns:
            str: The computer's choice.
        """
        return random.choice(self.choices)

    def compare(self, user_choice: str, computer_choice: str) -> str:
        """
        Compares the user's choice with the computer's choice.

        Parameters:
            user_choice (str): The user's choice.
            computer_choice (str): The computer's choice.

        Returns:
            str: The result of the game.
        """
        if user_choice == computer_choice:
            return 'tie'
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            return "Congratulations, you won!"
        else:
            return "Sorry, you lost!"

    def play(self) -> None:
        """
        Controls the game flow.
        """
        user_choice: str = self.get_user_choice()
        computer_choice: str = self.computer_choice()
        result: str = self.compare(user_choice, computer_choice)
        print(f'You chose {user_choice} and the computer chose {computer_choice}. {result}')
        play_again: str = input('Do you want to play again? (y/n): ').lower()
        if play_again == 'y':
            self.play()
        else:
            print('Thank you for playing! Goodbye!')

if __name__ == '__main__':
    game = RockPaperScissors()
    game.play()
