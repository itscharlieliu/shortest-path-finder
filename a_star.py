from typing import List

from board import Board
from coord import Coord
from search_node import SearchNode


def a_star(board: Board, start: Coord, end: Coord):
    """
    https://www.geeksforgeeks.org/a-search-algorithm/
    :param board: The game board that we use to navigate
    :param start: The coordinate to start at
    :param end: The coordinate where we want to reach
    """
    # TODO change this to tree for optimization
    open_list: List[SearchNode] = []
    closed_list: List[SearchNode] = []

    # Initialize open list
    open_list.append(board.get_at(Coord(0, 0)))

    while len(open_list) > 0:
        # find the min in the list and remove it
        min_open = open_list.index(min(open_list))
        curr = open_list.pop(min_open)

        successors: List[SearchNode] = board.generate_successors(curr.coord)

        # For testing
        for i in successors:
            print(i.__repr__(), end="\n")
