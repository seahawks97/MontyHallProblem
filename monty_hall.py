
import random

# Create the hall. Keys are door numbers, values are what is behind
hall = {1: '', 2: '', 3: ''}


def create_hall():
    """
    Creates the hall with required setup for problem.
    Selects a random door and sets it to 'Car', then sets other doors
    to "Shit".
    The "Car" and "Shit" doors are changed throughout each simulation.
    :return: none
    """
    # Populate the hall with doors
    # Select 1 random door to have a car
    car_key = random.choice(list(hall.keys()))
    hall[car_key] = 'Car'

    # Remaining doors get shit
    for key in hall.keys():
        if key != car_key:
            hall[key] = 'Shit'

    # print('Hall created!')


def stick_with_initial(sims):
    """
    Once a door is revealed to be "Shit", the decision is to stay with
    the door you initially picked (which was randomly selected).
    :param sims: number of simulations to run
    :type sims: int
    :return: none
    """
    car_count = 0
    shit_count = 0

    for i in range(sims):
        create_hall()
        initial = random.choice(list(hall.keys()))
        if hall[initial] == 'Car':
            # print('You won a car!')
            car_count += 1
        else:
            # print('You got shit!')
            shit_count += 1

    print_results(car_count, shit_count, sims)


def switch(sims):
    """
    Once a door is revealed to be "Shit", the decision is to switch
    doors to the other, unrevealed door.
    :param sims: number of simulations to run
    :type sims: int
    :return: none
    """
    car_count = 0
    shit_count = 0

    for i in range(sims):
        create_hall()
        choice = random.choice(list(hall.keys()))

        # Find a shit door
        for door in hall.keys():
            if door != choice and hall[door] == 'Shit':
                # print('Door', door, 'has shit!')
                break

        # Find other door
        known_list = [choice, door]
        other = int(list(set(hall.keys()) - set(known_list))[0])
        # print(known_list, '\n', other)

        # Perform switch
        choice = other
        # print(choice)

        if hall[choice] == 'Car':
            # print('You won a car!')
            car_count += 1
        else:
            # print('You got shit!')
            shit_count += 1

    print_results(car_count, shit_count, sims)


def print_results(cc, sc, sims):
    """
    Prints results once a series of simulations has been completed for
    both tests.
    :param cc: car_count, the number of times a car was found
    :type cc: int
    :param sc: shit_count, the number of times shit was found
    :type sc: int
    :param sims: number of simulations that were ran, used in
    calculating percentage
    :type sims: int
    :return: none
    """
    print('You got a car', cc, 'times, or', cc * 100 /
          sims, '% of the time.')
    print('You got shit', sc, 'times, or', sc * 100 /
          sims, '% of the time.')


def get_sim_num():
    """
    Get number of simulations to run and validates input.
    :return: none
    """
    while True:
        simulations = input('Type the number of simulations you want '
                            'to run.\nThe higher the number, the more '
                            'accurate the numbers will be: ')

        try:
            simulations = int(simulations)
            if simulations > 0:
                return simulations
            else:
                print('Please type a positive number.\n')
        except ValueError:
            print('Please type a number.\n')


def get_selection():
    """
    The user selects whether to stick with the initial door that was
    randomly selected or to choose the other, unrevealed door. This
    decision is used throughout the whole set of simulations.
    :return: sel
    :rtype sel: str
    """
    while True:
        sel = input('\nPick 1 or 2 and press <enter>:'
                    '\n1. Stick with initial door'
                    '\n2. Switch to other door\n')
        if sel == '1' or sel == '2':
            return sel
        else:
            print('Please type a valid input.')


def main():
    # Gets number of simulations to run
    simulations = get_sim_num()

    # Choose whether to stay with initial or other door
    sel = get_selection()

    print('\nRunning', simulations, 'simulations...')

    if sel == '1':
        stick_with_initial(simulations)
    elif sel == '2':
        switch(simulations)


if __name__ == '__main__':
    main()
input('Press <enter> to exit. ')
