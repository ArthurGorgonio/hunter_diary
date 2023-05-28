from json import loads


def get_config(config: str) -> dict:
    with open(
        config,
        mode='r',
        encoding='utf-8',
    ) as f:
        return loads(f.read())
