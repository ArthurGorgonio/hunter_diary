from ..player import PlayerChar
from ...bag import Melee, Range


class Academic(PlayerChar):
    """Academic class."""

    def __init__(self, **kargs):
        kargs.update({
            "max_life_points": 20,
            "hp_potions": 2,
            "resistence_potion": 1,
            "weapons": [
                Melee(
                    damage=3,
                    two_hands=False,
                    weapon_type="throwable",
                    name="War Lance",
                ),
                Range(
                    damage=2,
                    two_hands= True,
                    weapon_type="arrow",
                    name="Simple Bow",
                )
            ]
        })
        super().__init__(**kargs)
