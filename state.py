from enum import Enum


class AppState(Enum):
    none = 0
    adding_wall = 1
    setting_start = 2
    setting_end = 3
    running_algorithm = 4


class State:
    def __init__(self):
        self._state = AppState.none

    def get(self) -> AppState:
        return self._state

    def set(self, state: AppState):
        self._state = state
