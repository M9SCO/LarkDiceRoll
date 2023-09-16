from random import seed
from unittest import TestCase

from PowerfulDiceRoller import DiceThrown, DiceError, Dice


class TesterDice(TestCase):

    def setUp(self) -> None:
        seed(1)

    def test_actual_times(self):
        """значение Dice.times сответвует поданному числу"""


        self.assertEqual(DiceThrown(times=1, faces=20).times, 1)

    def test_actual_face(self):
        """значение Dice.face сответвует поданному числу"""
        self.assertEqual(DiceThrown(times=1, faces=20).face, 20)

    def test_roll_1d20(self):
        """если кидать 1Кчто-то-там, то должно вернуть число"""
        dice = Dice(face=20)
        seed(1)
        self.assertEqual(DiceThrown(times=1, faces=20).dices, [dice])

    def test_roll_20d20(self):
        """если кидать много-чего-то-тамКчто-там то должно вернуть лист кубов"""
        dices = [Dice(face=20) for _ in range(20)]
        seed(1)
        self.assertEqual(DiceThrown(times=20, faces=20).dices, dices)

    def test_roll_3d20l(self):
        """если к кубам добавить сортировку "меньше", то должен поубирать результаты, не проходящие по условию"""
        dices = [Dice(face=20) for _ in range(3)]
        minimal_dice = min(dices)
        seed(1)

        self.assertEqual(DiceThrown(times=3, faces=20, dropout_function=min, dropout_rate=1).amount, [minimal_dice])

    def test_roll_2d20l3(self):
        """если сортируемое количество превышает количество бросков, то сортировка подавляется"""

        dices = [Dice(face=20) for _ in range(2)]
        seed(1)

        self.assertEqual(DiceThrown(times=2, faces=20, dropout_function=min, dropout_rate=3).amount, dices)

    def test_roll_4d20h3(self):
        """если к инициализированным кубам добавить сортировку то должно "урезать" результаты """
        dices = [Dice(face=20) for _ in range(4)]
        sorted_dice = sorted(dices, reverse=True)[:3]
        seed(1)
        actual = DiceThrown(times=4, faces=20)

        actual.amount  # []
        actual._amount_function = max
        actual._amount_rate = 3
        self.assertEqual(actual.amount, sorted_dice)

    def test_raise_if_use_part_retain(self):
        """если необходимо урезать количесво бросков, то необходимо подавать retain_f месте с retain_n, а не по одиночке"""
        with self.assertRaises(DiceError):
            dices = Dice(face=20)
            seed(1)
            self.assertEqual(DiceThrown(times=1, faces=20, dropout_function=max).dices, [dices])
