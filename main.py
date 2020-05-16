import threading
from queue import Queue

from pynput import keyboard

from a_star import a_star
from board import Board
from coord import Coord

OPTIONS = "1) Add wall | 2) Remove Wall | 3) Run A* | 0) Exit"


def main():
    print(OPTIONS)

    width = 10
    height = 10

    board = Board(width, height)
    print(board)

    stop_calculation = Queue()

    a_star_thread = []

    # Don't run a* in the listener thread. Rather, start another thread to run it
    def on_press(key):
        try:
            if key.char == "3":
                try:
                    if a_star_thread[0].is_alive():
                        stop_calculation.put(1)
                        a_star_thread[0].join()
                except IndexError:
                    # Thread hasn't started yet
                    pass

                if len(a_star_thread) > 0:
                    a_star_thread.pop()

                work_board = Board(width, height)

                a_star_thread.append(
                    threading.Thread(
                        target=a_star,
                        args=(stop_calculation, work_board, Coord(1, 1), Coord(5, 9)),
                    )
                )
                a_star_thread[0].start()
            if key.char == "0":
                return False
        except AttributeError:
            if key == keyboard.Key.esc:
                return False

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()


if __name__ == "__main__":
    main()
