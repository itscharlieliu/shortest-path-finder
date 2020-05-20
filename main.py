#! /usr/bin/env python3

import threading
from queue import Queue
from time import sleep

from pynput import keyboard

from a_star import a_star
from board import Board, print_board
from coord import Coord
from state import State, AppState

OPTIONS = "1) Edit wall | 2) Set start | 3) Run A* | 0) Exit"

EDIT_WALL_OPTIONS = "Use space bar to Toggle wall | WASD to move cursor"


def main():
    width = 10
    height = 10

    board = Board(width, height)
    print_board(board, message=OPTIONS)

    stop_calculation = Queue()

    a_star_thread = []

    state = State()

    def handle_edit_wall(key):
        # try:
        #     if key.char == "a":
        #         board.set_cursor(board.get_cursor() + Coord(-1, 0))
        #     if key.char == "w":
        #         board.set_cursor(board.get_cursor() + Coord(0, -1))
        #     if key.char == "d":
        #         board.set_cursor(board.get_cursor() + Coord(1, 0))
        #     if key.char == "s":
        #         board.set_cursor(board.get_cursor() + Coord(0, 1))
        # except AttributeError:
        if key == keyboard.Key.left:
            board.set_cursor(board.get_cursor() + Coord(-1, 0))
        if key == keyboard.Key.up:
            board.set_cursor(board.get_cursor() + Coord(0, -1))
        if key == keyboard.Key.right:
            board.set_cursor(board.get_cursor() + Coord(1, 0))
        if key == keyboard.Key.down:
            board.set_cursor(board.get_cursor() + Coord(0, 1))
        if key == keyboard.Key.space:
            board.toggle_wall(board.get_cursor())

    def handle_run_algorithm():
        """run A* in a separate thread"""
        state.set(AppState.running_algorithm)

        board.clear_cursor()

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
                board.set_cursor(Coord(0, 0))
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
            if key == keyboard.Key.enter:
                input()
                return False
        finally:
            message = OPTIONS + "\n"
            if state.get() == AppState.adding_wall:
                message += EDIT_WALL_OPTIONS
            print_board(board, message=message)

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()


if __name__ == "__main__":
    main()
