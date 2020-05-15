from pynput import keyboard

from a_star import a_star
from board import Board
from coord import Coord
from terminal_utils import clear_board

OPTIONS = "1) Add wall | " "2) Remove Wall | " "0) Exit"


def main():

    print(OPTIONS)

    def on_press(key):
        try:
            print("alphanumeric key {0} pressed".format(key.char))
        except AttributeError:
            print("special key {0} pressed".format(key))

    def on_release(key):
        print("{0} released".format(key))
        if key == keyboard.Key.esc:
            # Stop listener
            return False

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

    # width = 10
    # height = 10
    #
    # board = Board(width, height)
    #
    # print(str(board))
    # a_star(board, Coord(1, 1), Coord(5, 9))
    # clear_board(height)
    # print(str(board))

    # while True:
    #     print(OPTIONS)
    #     if input() == "0":
    #         break


if __name__ == "__main__":
    main()
