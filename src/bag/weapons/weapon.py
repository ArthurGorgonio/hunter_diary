from abc import ABC


class Weapon(ABC):
    def __init__(
        self,
        damage: int = 0,
        two_hands: bool = False,
        weapon_type: str = "",
        name: str = "",
        special: str = "",
    ) -> None:
        self.damage = damage
        self.type = weapon_type
        self.two_hands = two_hands
        self.name = name
        self.special = special

    def __str__(self) -> str:
        msg = (
            f"{self.name:^10}\t"
            + f"{self.type:^10}\t"
            + f"{'Two hands' if self.two_hands else 'One hand':>9}\t"
            + f"{self.damage:>5}\n"
        )

        if self.special:
            msg += f"{self.special}\n"

        return msg