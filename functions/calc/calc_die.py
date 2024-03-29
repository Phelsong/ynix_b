from typing import Generator
import numpy as np

rng: Generator = np.random.default_rng()


def roll_range(min: int, max: int, offset: int = 0) -> int:
    return rng.integers(min, max) + offset  # type: ignore


def roll_die(rolls, sides, weight=0) -> int:
    """Evaluates 'die_expr', a numeric expression that may contain dice rolls,
    expressed as NdX where N is the number of dice, and X is the faces on
    each die. A set of 2 6-sided dice would be represented as 2d6.
    Static +/- modifiers may be added (eg '1d5 - 3'), also known as weighted die"""

    # ---------------------------------------------------------------
    total_roll = 0
    for i in range(rolls):
        total_roll += rng.integers(1, sides)  # type: ignore
    return total_roll + weight
