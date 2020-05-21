#! /usr/bin/env python3

import threading
from queue import Queue
from time import sleep

from pynput import keyboard

from a_star import a_star
from board import Board, print_board
from coord import Coord
from state import State, AppState

EDIT_WALL_OPTIONS = "Press A to Toggle wall | Arrow Keys to move cursor"
SETTING_START = "Press A to set start | Arrow Keys to move cursor"
SETTING_END = "Press A to set end | Arrow Keys to move cursor"
RUNNING_A_STAR = "Running A*. Press any button to stop"


def main():
    width = 30
    height = 20

    board = Board(width, height)
    print_board(board)

    stop_calculation = Queue()

    a_star_thread = []

    state = State()

    def handle_move_cursor(key):
        if key == keyboard.Key.left:
            if board.get_cursor().x == 0:
                return
            board.set_cursor(board.get_cursor() + Coord(-1, 0))
        if key == keyboard.Key.up:
            if board.get_cursor().y == 0:
                return
            board.set_cursor(board.get_cursor() + Coord(0, -1))
        if key == keyboard.Key.right:
            if board.get_cursor().x == width - 1:
                return
            board.set_cursor(board.get_cursor() + Coord(1, 0))
        if key == keyboard.Key.down:
            if board.get_cursor().y == height - 1:
                return
            board.set_cursor(board.get_cursor() + Coord(0, 1))

    def handle_run_algorithm():
        """run A* in a separate thread"""
        state.set(AppState.running_algorithm)

        board.clear_cursor()

        while len(a_star_thread) > 0:
            a_star_thread.pop()

        a_star_thread.append(
            threading.Thread(target=a_star, args=(stop_calculation, board),)
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
            handle_move_cursor(key)
            try:
                if key.char == "a":
                    board.toggle_wall(board.get_cursor())
            except AttributeError:
                pass
        if state.get() == AppState.setting_start:
            handle_move_cursor(key)
            try:
                if key.char == "a":
                    board.set_start(board.get_cursor())
            except AttributeError:
                pass
        if state.get() == AppState.setting_end:
            handle_move_cursor(key)
            try:
                if key.char == "a":
                    board.set_end(board.get_cursor())
            except AttributeError:
                pass

        try:
            if key.char == "1":
                board.set_cursor(Coord(0, 0))
                state.set(AppState.adding_wall)
                return
            if key.char == "2":
                board.set_cursor(Coord(0, 0))
                state.set(AppState.setting_start)
            if key.char == "3":
                board.set_cursor(Coord(0, 0))
                state.set(AppState.setting_end)
            if key.char == "4":
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
            message = ""
            curr_state = state.get()
            if curr_state == AppState.adding_wall:
                message = EDIT_WALL_OPTIONS
            if curr_state == AppState.setting_start:
                message = SETTING_START
            if curr_state == AppState.setting_end:
                message = SETTING_END
            if curr_state == AppState.running_algorithm:
                message = RUNNING_A_STAR
            print_board(board, message=message)

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()


if __name__ == "__main__":
    main()
