from random import randint
from typing import Tuple

from .sweeper import MineSweeper


def _get_coords_from_user(sweeper: MineSweeper) -> Tuple[int, ...]:
    error_msg = 'Invalid coordinates. Please try again.'
    while True:
        coords_as_str = input(
            f'Enter a cell (row [{1} - {sweeper.height}], col[{1} - {sweeper.width}]): ')
        try:
            coords = [int(c) for c in coords_as_str.split(',')]
        except ValueError:
            print(error_msg)
            continue
        if len(coords) != 2:
            print(error_msg)
            continue
        if not 1 <= coords[0] <= sweeper.height or not 1 <= coords[1] <= sweeper.width:
            print(error_msg)
            continue
        return tuple([c - 1 for c in coords])


def _place_mines(sweeper: MineSweeper, forbidden_coordinates: Tuple[int, ...], num_mines: int) -> None:
    mine_positions = set()
    while len(mine_positions) < num_mines:
        i = randint(0, sweeper.height - 1)
        j = randint(0, sweeper.width - 1)
        if (i, j) == forbidden_coordinates:
            continue
        mine_positions.add((i, j))
    sweeper.place_mines(mine_positions)


def run_mine_sweeper_cli(height: int = 6, width: int = 6, num_mines: int = 6) -> None:
    if num_mines >= height * width:
        raise ValueError("Too many mines")
    if num_mines < 1:
        raise ValueError("Too few mines")
    print('Welcome to MineSweeper!')
    sweeper = MineSweeper(height, width)
    mines_placed = False
    while not sweeper.game_is_over:
        print(f'\n{sweeper}\n')
        coords = _get_coords_from_user(sweeper)
        if not mines_placed:
            _place_mines(sweeper, coords, num_mines)
            mines_placed = True
        sweeper.click_cell(*coords)

    print(f'\n{sweeper}\n')
    print('Game over! Thank you for playing!')
