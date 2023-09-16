from random import seed
from unittest import TestCase

from PowerfulDiceRoller import DiceThrown, GRAMMAR_DICE, open_lark, Dice


class TesterDiceRoller(TestCase):
    def roll_dice(self, f: str) -> DiceThrown:
        seed(1)
        return open_lark(f, GRAMMAR_DICE)

    def setUp(self) -> None:
        seed(1)

    def test_roll_d20(self):
        "Должен кидать одинарный куб даже если это не указано явно"
        dice = Dice(20)
        dice.set_result(5)
        self.assertEqual(self.roll_dice("d20", ).dices, [dice])

    def test_roll_3d6(self):
        """Должен обрабатывать простую нотацию кубов"""
        dices = [Dice(6) for _ in range(3)]
        seed(1)
        self.assertEqual(self.roll_dice("3д6", ).dices, dices)

    def testing_filtration_high_2d20h(self):
        """Должен выбирать максимальный результат, даже если это не указано явно"""
        dices = [Dice(20) for _ in range(2)]
        seed(1)
        self.assertEqual(self.roll_dice("2d20h").dices, dices)

    def testing_filtration_high_3d6h2(self):
        """Должен выбирать N максимальных кубов"""
        dices = [Dice(6) for _ in range(3)]
        seed(1)
        self.assertEqual(self.roll_dice("3d6h2").dices, dices)

    def testing_filtration_high_2d20l(self):
        """Должен выбирать минимальный результат, даже если это не указано явно"""
        dices = [Dice(20) for _ in range(2)]
        seed(1)
        self.assertEqual(self.roll_dice("2d20l").dices, dices)

    def testing_filtration_high_3d6l2(self):
        """Должен выбирать N миниматьных кубов"""
        dices = [Dice(6) for _ in range(3)]
        seed(1)
        self.assertEqual(self.roll_dice("3d6l2").dices, dices)

    def testing_filtration_high_3d6l4(self):
        """Должен оставить все кубы, если их количество меньше чем необходимо оставить"""
        dices = [Dice(6) for _ in range(3)]
        seed(1)
        self.assertEqual(self.roll_dice("3d6l4").dices, dices)

    def testing_banchmarc(self):
        """Стресстест"""
        #1.486s
        self.assertIsNotNone(self.roll_dice("1000000d1000000").total)
