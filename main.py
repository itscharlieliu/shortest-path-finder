#! /usr/bin/env python3

import threading
from queue import Queue

from pynput import keyboard

from a_star import a_star
from board import Board
from coord import Coord
from state import State, AppState
from terminal_utils import clear_board

OPTIONS = "1) Add wall | 2) Remove Wall | 3) Run A* | 0) Exit"


def main():
    print(OPTIONS)

    width = 10
    height = 10

    board = Board(width, height)
    print(board)

    stop_calculation = Queue()

    a_star_thread = []

    state = State()

    def handle_edit_wall(key):
        print(str(key))

    def handle_run_algorithm():
        """run A* in a separate thread"""
        state.set(AppState.running_algorithm)

        while len(a_star_thread) > 0:
            a_star_thread.pop()

        a_star_thread.append(
            threading.Thread(
                target=a_star, args=(stop_calculation, board, Coord(1, 1), Coord(5, 9)),
            )
        )
        a_star_thread[0].start()

    def on_press(key):

        if state.get() == AppState.running_algorithm:
            # Clear the board whenever the user presses a button
            board.clear()
            try:
                if a_star_thread[0].is_alive():
                    stop_calculation.put(1)
                    a_star_thread[0].join()
            except IndexError:
                # Thread hasn't started yet
                pass

        if state.get() == AppState.adding_wall:
            handle_edit_wall(key)
        try:
            if key.char == "1":
                state.set(AppState.adding_wall)
                return
            if key.char == "3":
                handle_run_algorithm()
                return
            if key.char == "0":
                return False
        except AttributeError:
            if key == keyboard.Key.esc:
                return False

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()


if __name__ == "__main__":
    main()
