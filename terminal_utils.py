def clear_board(height):
    for i in range(height):
        print("\033[A", end="")
