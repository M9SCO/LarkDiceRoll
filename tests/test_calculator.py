from unittest import TestCase

from rolling_dice import open_lark, GRAMMAR_CALCULATOR


class TesterCalculator(TestCase):
    "Checking base math logic"

    def run_func(self, f: str, expected: int):
        self.assertEqual(open_lark(f, GRAMMAR_CALCULATOR), expected, f"{f}!={expected}")

    def testing_sum(self):
        self.run_func("1+1", 2)

    def testing_sub(self):
        self.run_func("10-1", 9)

    def testing_mul(self):
        self.run_func("3*3", 9)

    def testing_dev(self):
        self.run_func("10/2", 5)

    def testing_complex_math_expression(self):
        self.run_func("((2+2)*2+2+2*2)/2", 7)

    def testing_simple_sum(self):
        self.run_func("2+2", 4)

    def testing_simple_mul(self):
        self.run_func("2*2", 4)

    def testing_hard_mul_and_div(self):
        self.run_func("2+2*2", 6)

    def testing_complex_mul_and_div(self):
        self.run_func("(2+2)*2", 8)

    def testing_wrong_formula(self):
        with self.assertRaises(Exception):
            # ToDo Пофиксить на пробрасывание собственной ошибки
            self.run_func("2?2", 0)
