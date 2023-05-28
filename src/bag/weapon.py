from .item import Item


class Weapon(Item):
    """
    Armas.

    elas podem ser dos seguintes tipos:
        - adaga
        - arco simples
        - escudo
        - espada longa
        - espada simples
        - lança de cavalaria
        - lança de guerra
        - machado
        - marreta
        - maça
    """
    def __init__(
        self,
        damage: int = 0,
        two_hands: bool = False,
        weapon_type: str = "",
        weapon_name: str = "",
        weapon_class: str = "",
        special: str = "",
    ) -> None:
        super().__init__(
            weapon_name,
            weapon_class,
            special,
        )
        self.damage = damage
        self.type = weapon_type
        self.two_hands = two_hands

    def __str__(self) -> str:
        msg = (
            f"{self.item_name:^10}\t"
            + f"{self.type:^10}\t"
            + f"{'Two hands' if self.two_hands else 'One hand':>9}\t"
            + f"{self.damage:>5} "
            + f"{self.item_special if self.item_special else ''}\n"
        )
        return msg
