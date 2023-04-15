from json import loads

from src.chars.player import PlayerChar

with open(
    "src/chars/classes.json",
    mode='r',
    encoding='utf-8',
) as f:
    available_classes = loads(f.read())

choosen_class = 'noble'

academic: dict = available_classes.get(choosen_class)

academic.update(
    {
        'name': 'Bob',
        'class_name': choosen_class.capitalize(),
    }
)

print(PlayerChar(**academic))
