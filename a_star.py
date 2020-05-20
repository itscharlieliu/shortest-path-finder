from queue import Queue, Empty
from time import sleep
from typing import List

from board import Board, print_board
from coord import Coord
from search_node import SearchNode, NodeType

DIAGONAL = 14.142135623730951
NON_DIAGONAL = 10


def a_star(stop_calculation: Queue, board: Board):
    """
    Function to find the shortest path on the board using the A* method
    :param stop_calculation: A queue where if we put anything, this thread will stop
    :param board: The game board that we use to navigate
    """

    if board.get_start() is None or board.get_end() is None:
        sleep(0.01)
        print_board(board, message="Must provide a start and end")
        return

    start_node = board.get_at(board.get_start())
    end_node = board.get_at(board.get_end())

    open_list: List[SearchNode] = []
    closed_list: List[SearchNode] = []

    # Initialize open list
    open_list.append(start_node)

    while len(open_list) > 0:
        try:
            stop_calculation.get_nowait()
            return
        except Empty:
            pass

        # find the min in the list and remove it
        min_open = open_list.index(min(open_list))
        curr = open_list.pop(min_open)

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

        if curr == end_node:
            curr.set_path()
            break

        for coord in successor_coords:
            if (
                board.get_at(coord)
                and board.get_at(coord).get_type() is not NodeType.wall
            ):
                curr_successor = board.get_at(coord).copy()

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
                    # first, look in open_list
                    open_index = open_list.index(board.get_at(coord))
                    if open_list[open_index] < curr_successor:
                        # The one we found has a higher f than curr, so we skip it
                        continue

                    # Otherwise, we edit it on the open list
                    open_list[open_index] = curr_successor
                    board.set_at(curr_successor)

                    continue
                except ValueError:
                    # it's not in the list, so we add it
                    pass
                try:
                    # then, look in closed list
                    closed_index = closed_list.index(board.get_at(coord))
                    if closed_list[closed_index] < curr_successor:
                        # The one we found has a higher f than curr, so we skip it
                        continue
                except ValueError:
                    pass

                board.set_at(curr_successor)
                curr_successor.set_type(NodeType.open)
                open_list.append(curr_successor)

        curr.set_type(NodeType.closed)
        closed_list.append(curr)

        print_board(board)
        sleep(0.05)

    print_board(board)
