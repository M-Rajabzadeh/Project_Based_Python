import random

def get_user_guess():
    while True:
        user_input = input('Guess a number between 1 and 100 (or press "q" to quit): ')
        if user_input == 'q':
            return None
        elif user_input.isdigit():
            guess = int(user_input)
            if 1 <= guess <= 100:
                return guess
            else:
                print('Your number is out of range. Please input a number between 1 and 100.')
        else:
            print('Invalid input. Please enter a number.')

def play_game():
    score = 100
    random_num = random.randint(1, 100)
    while True:
        user_guess = get_user_guess()
        if user_guess is None:
            print('Goodbye')
            return False
        elif user_guess < random_num:
            print('Too low! Try again.')
        elif user_guess > random_num:
            print('Too high! Try again.')
        else:
            print(f'Congratulations! You guessed the correct number {random_num} and your score is {score}')
            break
        score -= 10
        score = max(score, 0)
    return True

def main():
    while True:
        game_result = play_game()
        if not game_result:
            break
        play_again = input('Do you want to play again? (y/n): ').lower()
        if play_again != 'y':
            print('Thank you for playing! Goodbye!')
            break

if __name__ == "__main__":
    main()
