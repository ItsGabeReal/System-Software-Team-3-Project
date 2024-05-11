'''
Resource classes for ores and trees.
'''

from typing import Literal

type resource_type = Literal['iron', 'copper', 'wood']

class Resource:
    def __init__(self, type: resource_type, location: tuple[int, int]) -> None:
        self.health: int = 100 # Gets destroyed when health reaches zero
        self.type = type
        self.location = location

    def mine(self, amount: int):
        self.health = max(self.health - amount, 0)

    def is_mined(self) -> bool:
        return self.health == 0
