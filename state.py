from enum import Enum


class AppState(Enum):
    none = 0
    adding_wall = 1
    removing_wall = 2
    running_algorithm = 3


class State:
    def __init__(self):
        self._state = AppState.none

    def get(self) -> AppState:
        return self._state

    def set(self, state: AppState):
        self._state = state
