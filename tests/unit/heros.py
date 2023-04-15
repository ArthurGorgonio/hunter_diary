from unittest import TestCase

from faker import Faker

from src.chars.player import PlayerChar


class HerosTest(TestCase):
    def test_create_basic_char_info_success(self):
        """Test the basic creation of the character."""
        hero_name = Faker().name()
        base_player = PlayerChar(**{
            "name": hero_name,
            "max_life_points": 30,
        })

        self.assertEqual(hero_name, base_player.name)
        self.assertEqual(0, base_player.damage)
        self.assertEqual(0, base_player.fatigue)
        self.assertEqual(30, base_player.life_points)
        self.assertEqual(30, base_player.max_life_points)
        self.assertEqual(0, base_player.potions)
        self.assertEqual(None, base_player.equips)

    def test_create_basic_char_info_raise_when_damage_is_lower_than_zero(self):
        """
        Test the creation of the character when damage is lower than 0,
        it should raise an exception.
        """
        hero_name = Faker().name()
        with self.assertRaises(ValueError) as err:
            PlayerChar(
                **{
                "name": hero_name,
                "max_life_points": 30,
                "damage": -3
            }
        )

        self.assertEqual(
            "Can't use this value!",
            str(err.exception)
        )
