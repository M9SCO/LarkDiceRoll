import random
import unittest

from PowerfulDiceRoller import Dice
from PowerfulDiceRoller.models.errors import NegativeDiceFaces


class TesterDice(unittest.TestCase):
    def setUp(self) -> None:
        random.seed(1)

    def testDiceRepr(self):
        self.assertEqual(str(Dice(20)), "5")

    def testExceptedInputTypeFace(self):
        self.assertRaises(TypeError, lambda: Dice("20"))

    def testExceptedNegativeFace(self):
        self.assertRaises(NegativeDiceFaces, lambda: Dice(-20))

    def testAssertFace(self):
        self.assertEqual(Dice(face=20).face, 20)

    def testResult(self):
        self.assertIsNotNone(Dice(20).result)

    def testDiceToInt(self):
        self.assertEqual(int(Dice(20)), 5)

    def testAddDiceToInt(self):
        dice = Dice(1)
        self.assertEqual(dice + 1, 2)

    def testAddIntToDice(self):
        dice = Dice(1)
        self.assertEqual(1 + dice, 2)

    def testAddDiceToDice(self):
        dice_1 = Dice(face=100)
        dice_2 = Dice(face=100)
        self.assertEqual(dice_2 + dice_1, 91)

    def testExceptedAddDiceToString(self):
        dice = Dice(face=100)
        self.assertRaises(TypeError, lambda: dice + "10")

    def testAddInlineIntToDice(self):
        dice = Dice(face=2)
        result = 40
        result += dice
        self.assertEqual(result, 41)

    def testSumListOfDice(self):
        self.assertEqual(sum(Dice(face=100) for _ in range(10)), 528)

    def testSubDiceToInt(self):
        dice = Dice(1)
        self.assertEqual(dice - 1, 0)

    def testSubIntToDice(self):
        dice = Dice(1)
        self.assertEqual(1 - dice, 0)

    def testSubDiceToDice(self):
        dice_1 = Dice(face=100)
        dice_2 = Dice(face=100)
        self.assertEqual(dice_2 - dice_1, 55)

    def testSubInlineIntToDice(self):
        dice = Dice(face=2)
        result = 40
        result -= dice
        self.assertEqual(result, 39)

    def testMulDiceToInt(self):
        dice = Dice(1)
        self.assertEqual(dice * 1, 1)

    def testMulIntToDice(self):
        dice = Dice(1)
        self.assertEqual(1 * dice, 1)

    def testMulDiceToDice(self):
        dice_1 = Dice(face=100)
        dice_2 = Dice(face=100)
        self.assertEqual(dice_2 * dice_1, 1314)

    def testMulInlineIntToDice(self):
        dice = Dice(face=2)
        result = 40
        result *= dice
        self.assertEqual(result, 40)

    def testTrueDivDiceToInt(self):
        dice = Dice(1)
        self.assertEqual(dice / 1, 1)

    def testTrueDivIntToDice(self):
        dice = Dice(1)
        self.assertEqual(1 / dice, 1)

    def testTrueDivDiceToDice(self):
        dice_1 = Dice(face=1)
        dice_2 = Dice(face=10)
        self.assertEqual(dice_2 / dice_1, 10)

    def testTrueDivInlineIntToDice(self):
        dice = Dice(face=2)
        result = 40
        result /= dice
        self.assertEqual(result, 40)

    def testFloorDivDiceToInt(self):
        dice = Dice(1)
        self.assertEqual(dice // 1, 1)

    def testFloorDivIntToDice(self):
        dice = Dice(1)
        self.assertEqual(1 // dice, 1)

    def testFloorDivDiceToDice(self):
        dice_1 = Dice(face=100)
        dice_2 = Dice(face=100)
        self.assertEqual(dice_2 // dice_1, 4)

    def testFloorDivInlineIntToDice(self):
        dice = Dice(face=2)
        result = 40
        result //= dice
        self.assertEqual(result, 40)
