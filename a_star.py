from typing import List

from board import Board
from coord import Coord
from search_node import SearchNode

DIAGONAL = 14.142135623730951
NON_DIAGONAL = 10


def a_star(board: Board, start: Coord, end: Coord):
    """
    https://www.geeksforgeeks.org/a-search-algorithm/
    :param board: The game board that we use to navigate
    :param start: The coordinate to start at
    :param end: The coordinate where we want to reach
    """
    end_node = board.get_at(end)

    # TODO change this to tree for optimization
    open_list: List[SearchNode] = []
    closed_list: List[SearchNode] = []

    # Initialize open list
    open_list.append(board.get_at(start))

    # test
    open_list.append(board.get_at(Coord(0, 1)))

    while len(open_list) > 0:
        print("running")
        # find the min in the list and remove it
        min_open = open_list.index(min(open_list))
        curr = open_list.pop(min_open)

        successors: List[SearchNode] = []

        curr_successor = board.get_at(Coord(curr.coord.x - 1, curr.coord.y - 1))
        if curr_successor and not curr_successor.is_wall:
            curr_successor.parent = curr
            curr_successor.g = curr.g + DIAGONAL
            curr_successor.h = curr_successor.calculate_distance(end_node)
            curr_successor.f = curr_successor.g + curr_successor.h
            successors.append(curr_successor)

        curr_successor = board.get_at(Coord(curr.coord.x, curr.coord.y - 1))
        if curr_successor and not curr_successor.is_wall:
            curr_successor.parent = curr
            curr_successor.g = curr.g + NON_DIAGONAL
            curr_successor.h = curr_successor.calculate_distance(end_node)
            curr_successor.f = curr_successor.g + curr_successor.h
            successors.append(curr_successor)

        curr_successor = board.get_at(Coord(curr.coord.x + 1, curr.coord.y - 1))
        if curr_successor and not curr_successor.is_wall:
            curr_successor.parent = curr
            curr_successor.g = curr.g + DIAGONAL
            curr_successor.h = curr_successor.calculate_distance(end_node)
            curr_successor.f = curr_successor.g + curr_successor.h
            successors.append(curr_successor)

        curr_successor = board.get_at(Coord(curr.coord.x - 1, curr.coord.y))
        if curr_successor and not curr_successor.is_wall:
            curr_successor.parent = curr
            curr_successor.g = curr.g + NON_DIAGONAL
            curr_successor.h = curr_successor.calculate_distance(end_node)
            curr_successor.f = curr_successor.g + curr_successor.h
            successors.append(curr_successor)

        curr_successor = board.get_at(Coord(curr.coord.x + 1, curr.coord.y))
        if curr_successor and not curr_successor.is_wall:
            curr_successor.parent = curr
            curr_successor.g = curr.g + NON_DIAGONAL
            curr_successor.h = curr_successor.calculate_distance(end_node)
            curr_successor.f = curr_successor.g + curr_successor.h
            successors.append(curr_successor)

        curr_successor = board.get_at(Coord(curr.coord.x - 1, curr.coord.y + 1))
        if curr_successor and not curr_successor.is_wall:
            curr_successor.parent = curr
            curr_successor.g = curr.g + DIAGONAL
            curr_successor.h = curr_successor.calculate_distance(end_node)
            curr_successor.f = curr_successor.g + curr_successor.h
            successors.append(curr_successor)

        curr_successor = board.get_at(Coord(curr.coord.x, curr.coord.y + 1))
        if curr_successor and not curr_successor.is_wall:
            curr_successor.parent = curr
            curr_successor.g = curr.g + NON_DIAGONAL
            curr_successor.h = curr_successor.calculate_distance(end_node)
            curr_successor.f = curr_successor.g + curr_successor.h
            successors.append(curr_successor)

        curr_successor = board.get_at(Coord(curr.coord.x + 1, curr.coord.y + 1))
        if curr_successor and not curr_successor.is_wall:
            curr_successor.parent = curr
            curr_successor.g = curr.g + DIAGONAL
            curr_successor.h = curr_successor.calculate_distance(end_node)
            curr_successor.f = curr_successor.g + curr_successor.h
            successors.append(curr_successor)

        # For testing
        for i in successors:
            print(i.__repr__(), end="\n")

        print("\n")
