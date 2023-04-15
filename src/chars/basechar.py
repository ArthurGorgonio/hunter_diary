from abc import ABC


class BaseChar(ABC):
    """Base class for Hunters, Companions, and Enemies for the game"""

    def __init__(
        self,
        max_life_points: int = 1,
        dmg: int = 1,
    ):
        self.life_points = max_life_points
        self.max_life_points = max_life_points
        self.damage = dmg

    @property
    def damage(self):
        return self._damage

    @damage.setter
    def damage(self, dmg):
        if dmg < 0:
            raise ValueError("Can't use this value!")
        self._damage = dmg
