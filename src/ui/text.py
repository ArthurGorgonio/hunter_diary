# from pprint import pprint

from src.chars.player import PlayerChar
from src.translation.translation import translator
from src.ui.ui import UI


class Terminal(UI):
    """
    This is an interface for the game in text-based mode.
    """
    def available_chars(self, players: list) -> str:
        classes: str = '\n'.join(
            f'    ({index + 1}) {translator.translate("classes", class_name)}\n'
            f'        {"".join(translator.translate("description", class_name))}'
            for index, class_name in enumerate(players)
        )

        msg = '\n'.join([
            translator.translate('player', 'available'),
            str(classes),
        ])

        return msg

    # def select_char(self, player: dict) -> PlayerChar:
    #     print("Welcome to the character selection")
    #     return PlayerChar(**player)

    def player_status(self, player: PlayerChar) -> str:
        # msg = (
        #     f"Hero Name: {self.name}\t Class: {self.class_name}\n"
        #     + f"HP: {self.life_points} / {self.max_life_points}\n"
        #     + f"Remain Potions: {self.potions}\n"
        #     + f"Fatigue: {self.fatigue} / 6\n"
        #     + f"Damage: {self.damage}\n"
        #     + "\n----\n\n"
        #     + "Weapons:\n"
        #     + f"{'Name':^10}\t{'Type':^10}\t{'Weild':^9}\t{'Damage':^8}\n"
        # )

        # for weapon in self.equips:
        #     if isinstance(weapon, Weapon):
        #         msg += weapon.__str__()
        raise NotImplementedError("Requires override!")

    def player_equipments(self, player: PlayerChar):
        raise NotImplementedError("Requires override!")
