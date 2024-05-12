'''
Resource classes for ores and trees.
'''

from typing import Literal

class Resource:
    def __init__(self, type: str, location: tuple[int, int]) -> None:
        self.health: int = 100 # Gets destroyed when health reaches zero
        self.type = type
        self.location = location

    def mine(self, amount: int):
        self.health = max(self.health - amount, 0)

    def is_mined(self) -> bool:
        return self.health == 0
