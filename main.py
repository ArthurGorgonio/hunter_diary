from src.chars.player import PlayerChar
from src.translation.translation import translator
from src.ui.text import Terminal
from src.utils import get_config

if __name__ == "__main__":
    text = Terminal()
    translator.load_data('en')
    players_data: dict = get_config('cloud/classes.json')
    classes: list = list(players_data.keys())
    classes.sort()

    print(text.available_chars(classes))
    player = int(input("Qual a sua classe/Profissão? 1-6\n"))

    print(
        # text.player_status(
        PlayerChar(**players_data.get(classes[player - 1], {}))
        # )
    )

    # choosen_class = text.select_char(get_config('cloud/classes.json'))

    # print(PlayerChar(**choosed_class))
