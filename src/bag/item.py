from abc import ABC


class Item(ABC):
    """
    Classe base dos itens do jogo.
    """

    def __init__(
        self,
        item_name,
        item_class,
        item_special,
    ) -> None:
        self.item_name = item_name
        self.item_class = item_class
        self.item_special = item_special


class Equipment(Item):
    def __init__(
        self,
        item_name,
        item_class,
        item_special,
        wear: bool,
    ) -> None:
        super().__init__(item_name, item_class, item_special)
        self.wear = wear
