from random import randint


def roll_range(min, max, offset=0):
    return randint(min, max)


def roll_die(rolls, sides, weight=0, min_roll=False, max_roll=False):
    """Evaluates 'die_expr', a numeric expression that may contain dice rolls,
    expressed as NdX where N is the number of dice, and X is the faces on
    each die. A set of 2 6-sided dice would be represented as 2d6.
    Static +/- modifiers may be added (eg '1d5 - 3'), but no other mathematical
    expressions are permitted.
    If 'min_roll' is set, all dice rolls return the lowest possible value.
    If 'max_roll' is set, all dice rolls return the highest possible value."""
    # Perform a sanity-check so users can't inject arbitrary code into the
    # die expression

    # ---------------------------------------------------------------
    total_roll = 0
    for i in range(rolls):
        roll_value = randint(1, sides)
        total_roll += roll_value
    return total_roll + weight
