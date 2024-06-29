import random

def simulate_monty_hall(change_choice, simulations):
    """
    Simulates the Monty Hall problem.

    Parameters:
    change_choice (bool): Whether the player changes their initial choice after the host opens a door.
    simulations (int): The number of simulations to run.

    Returns:
    float: The probability of winning the car by following the chosen strategy.
    """
    wins = 0

    for _ in range(simulations):
        # Hide the car behind one of the three doors
        doors = [0, 0, 1]  # 0 for goat, 1 for car
        random.shuffle(doors)

        # Player makes an initial choice
        initial_choice = random.choice([0, 1, 2])

        # Host opens one of the remaining doors that has a goat behind it
        remaining_doors = [i for i in range(3) if i != initial_choice and doors[i] == 0]
        door_opened_by_host = random.choice(remaining_doors)

        # Player either changes their choice or sticks with the initial choice
        if change_choice:
            final_choice = [i for i in range(3) if i != initial_choice and i != door_opened_by_host][0]
        else:
            final_choice = initial_choice

        # Check if the player wins
        if doors[final_choice] == 1:
            wins += 1

    return wins / simulations

if __name__ == "__main__":
    simulations = 10000

    win_rate_change = simulate_monty_hall(True, simulations)
    win_rate_no_change = simulate_monty_hall(False, simulations)

    print(f"Winning probability by changing choice: {win_rate_change * 100:.2f}%")
    print(f"Winning probability by not changing choice: {win_rate_no_change * 100:.2f}%")
