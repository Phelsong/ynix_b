# PvP DR Functions

# imports
from src.calc.calc_die import roll_range


# ======================================================
def roll_dr(dr_value, min_dr, max_dr) -> int:
    """Provides a random (PvP) DR roll for the given 'dr_value'. Results can
    be coerced to the absolute max or min dice rolls by providing 'min_roll'
    or 'max_roll' as True."""
    # np.random(min_dr, max_dr)
    dr_shred = roll_range(min_dr, max_dr)
    return dr_value - dr_shred


# ======================================================
def get_dr_range(dr_value) -> Tuple[int, int]:
    """Calculates (min_dr, max_dr) applied in PvP for the given 'dr_value'"""
    min_shred = 3 * dr_value // 20
    max_shred = dr_value // 3
    min_dr = dr_value - max_shred
    max_dr = dr_value - min_shred
    return min_dr, max_dr
