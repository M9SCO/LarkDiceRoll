from operator import add, mul, sub, truediv as div
from re import findall, search
from typing import List, Union

from lark import Lark, Tree

from resources.grammar import GRAMMAR_DICE, GRAMMAR_CALCULATOR
from src.exceptions import ParseError

__all__ = ["get_result"]

from models import Dice

from models import Result


def simple_calculation(tree: Tree) -> int:
    values = [get_next_point(child) for child in tree.children]
    if tree.data == "add":
        return add(*values)
    elif tree.data == "sub":
        return sub(*values)
    elif tree.data == "mul":
        return mul(*values)
    elif tree.data == "div":
        return div(*values)


def parse_roll_dice(tree: Tree) -> Dice:
    if len(tree.children) == 2:
        thrown, face = [get_next_point(child) for child in tree.children]
    else:
        thrown, face = 1, get_next_point(*tree.children)
    return Dice(throw=thrown, face=face)


def filtration_dices(tree: Tree) -> Dice:
    dice: Dice = get_next_point(tree.children[0])

    if tree.data == "max":
        dice._retain_f = max
    elif tree.data == "min":
        dice._retain_f = min
    dice._retain_n = get_next_point(tree.children[1]) if len(tree.children) > 1 else 1
    return dice


def get_next_point(tree: Tree) -> Union[int, Dice, Tree]:
    if tree.data in ("add", "sub", "mul", "div"):
        return simple_calculation(tree)
    elif tree.data == "to_int":
        return int(tree.children[0])
    elif tree.data == "res":
        return sum([get_next_point(child) for child in tree.children])
    elif tree.data == "dice":
        return parse_roll_dice(tree)
    elif tree.data in ("max", "min"):
        return filtration_dices(tree)


def open_lark(text, grammar):
    return get_next_point(Lark(grammar, start="start").parse(text))


def get_result(text,
               grammar_dice=GRAMMAR_DICE,
               grammar_calc=GRAMMAR_CALCULATOR) -> List:
    results = []
    repeats_math = search(r"(^\d+)[хx]|[хx](\d+$)", text)
    repeats = repeats_math.group(1) or repeats_math.group(2) if repeats_math else 1
    for _ in range(int(repeats) if int(repeats) < 10 else 10):
        t = text.replace(repeats_math.group(0), "") if repeats_math else text
        result = Result(raw=t)
        result.dices = []
        for dice in findall(r"(\d*[dkдк]\d+[hlвнd]?\d*)", t):
            value: Dice = open_lark(text=dice, grammar=grammar_dice)
            result.dices.append((dice, value))
        result.total = open_lark(text=result.replaced_dices, grammar=grammar_calc)
        if str(result.total) == t:
            raise ParseError
        results.append(result)
    return results
