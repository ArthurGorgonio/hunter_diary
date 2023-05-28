from abc import ABC, abstractmethod

from src.chars.player import PlayerChar


class UI(ABC):
    @abstractmethod
    def available_chars(self, players: list) -> str:
        raise NotImplementedError("Requires override!")

    # @abstractmethod
    # def select_char(self, player: PlayerChar) -> str:
    #     raise NotImplementedError("Requires override!")

    @abstractmethod
    def player_status(self, player: PlayerChar) -> str:
        raise NotImplementedError("Requires override!")

    def players_status(self, players: list) -> str:
        """Wrapper function for `self.player_status(player)`"""
        msg = str([self.players_status(player) for player in players])

        return msg

    @abstractmethod
    def player_equipments(self, player: PlayerChar):
        raise NotImplementedError("Requires override!")
