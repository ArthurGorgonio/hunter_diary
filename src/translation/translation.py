from src.utils import get_config


class Translation:
    """
    Translate manager for internacionalization.
    """

    def __init__(self,) -> None:
        self.lang = 'en'
        self.load_data(self.lang)

    def load_data(self, translate_language: str) -> None:
        """Reload the translate file."""
        self.data = get_config(
            f'cloud/translate/{translate_language}.json'
        )

    def translate(self, scope: str, key: str) -> str:
        """
        Recover the text in the right language based on user
        preference. If a key is not found the text `Not Found` will
        appear instead the right translate.
        """
        options = self.data.get(scope, '')

        return options.get(key, self.data['error']["key_not_found"])


translator = Translation()
