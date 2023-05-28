from .item import Item


class Gear(Item):
    """
    Armaduras.

    elas podem ser dos seguintes tipos:
        - Armadura
        - Botas
        - Bracelete
        - Elmo
        - Escudo
    """
    def __init__(
        self,
        pp: int = 0,
        gear_name: str = "",
        gear_class: str = "",
        special: str = "",
    ) -> None:
        super().__init__(
            gear_name,
            gear_class,
            special,
        )
        self.pp: int = pp
        self.max_pp: int = pp

    def bronken_gear(self):
        if self.pp <= 0:
            ...