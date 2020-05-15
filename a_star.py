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
    open_list.append(board.get_at(Coord(0, 0)))

    while len(open_list) > 0:
        print("looped")

        for node in open_list:
            print(node.__repr__())

        # find the min in the list and remove it
        min_open = open_list.index(min(open_list))
        curr = open_list.pop(min_open)

        successors: List[SearchNode] = []

        # generate all the positions for the successors
        successor_coords = [
            Coord(curr.coord.x - 1, curr.coord.y - 1),
            Coord(curr.coord.x, curr.coord.y - 1),
            Coord(curr.coord.x + 1, curr.coord.y - 1),
            Coord(curr.coord.x - 1, curr.coord.y),
            Coord(curr.coord.x + 1, curr.coord.y),
            Coord(curr.coord.x - 1, curr.coord.y + 1),
            Coord(curr.coord.x, curr.coord.y + 1),
            Coord(curr.coord.x + 1, curr.coord.y + 1),
        ]

        for coord in successor_coords:
            curr_successor = SearchNode(coord)
            if curr_successor and not curr_successor.is_wall:
                curr_successor.parent = curr
                # Set it to diagonal length if it is on a diagonal, otherwise set it to non-diagonal length
                curr_successor.g = curr.g + (
                    DIAGONAL
                    if coord.x != curr.coord.x and coord.y != curr.coord.y
                    else NON_DIAGONAL
                )
                curr_successor.h = curr_successor.calculate_distance(end_node)
                curr_successor.f = curr_successor.g + curr_successor.h
                try:
                    index = open_list.index(curr_successor)
                    print(
                        "{}\n{}\n------".format(
                            open_list[index].__repr__(), curr_successor.__repr__()
                        )
                    )
                    if open_list[index] < curr_successor:
                        # The one we found has a lower f than curr, so we skip it
                        continue
                    # Otherwise, we add it
                except ValueError:
                    # it's not in the list, so we add it
                    pass
                board.set_at(curr_successor)
                successors.append(curr_successor)
                print(curr_successor.__repr__())
