from .parser import (
    simple_calculation,
    parse_roll_dice,
    filtration_dices,
    get_next_point,
    open_lark,
    get_result,
)
from .models import (Dice, Result)
from .resources.grammar import GRAMMAR_DICE, GRAMMAR_CALCULATOR
from .src.exceptions import ParseError, DiceError, NotFoundMethod

__author__ = "M_9SCO"
__version__ = "1.0.0"
