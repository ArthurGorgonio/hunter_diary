from src.bag.weapons.weapon import Weapon

from .basechar import BaseChar


class PlayerChar(BaseChar):
    """Base class of the grouping all base attributes of a Hunter."""

    def __init__(
        self,
        **kargs,
    ):
        super().__init__(
            kargs.get("max_life_points", -1),
            kargs.get("damage", 0)
        )
        self.name = kargs.get("name", "Lucian")
        self.potions = kargs.get("hp_potions", 0)
        self.fatigue = 0
        self.equips = kargs.get("weapons", None)
        self.class_name = kargs.get("class_name")

    def __str__(self):
        msg = (
            f"Hero Name: {self.name}\t Class: {self.class_name}\n"
            + f"HP: {self.life_points} / {self.max_life_points}\n"
            + f"Remain Potions: {self.potions}\n"
            + f"Fatigue: {self.fatigue} / 6\n"
            + f"Damage: {self.damage}\n"
            + "\n----\n\n"
            + "Weapons:\n"
            + f"{'Name':^10}\t{'Type':^10}\t{'Weild':^9}\t{'Damage':^8}\n"
        )

        for weapon in self.equips:
            if isinstance(weapon, Weapon):
                msg += weapon.__str__()

        return msg
