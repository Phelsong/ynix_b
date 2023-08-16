"""ap related calcs"""
# libs
# import numpy as np

# imports
from functions.calc.calc_die import roll_die


# ===========================================================================
def get_ap_range(attacker) -> tuple[int, int]:
    """Calculates (min_ap, max_ap) for the given 'ap_value' using
    'attack_dice' (list of character + weapon dice) and 'gear_offsets'
    (list of other offsets, like Kutum's -2). Any given 'species_damage'
    can be included in this calculation, but it is not recommended, as it
    behaves differently than other AP both below DR & above caps."""
    # TODO: this is temporarily set till weapon die data can be built out
    min_ap: int = attacker.ap - 5
    max_ap: int = attacker.ap + 5
    return min_ap, max_ap


# ============================================================================


def get_base_damage(ap_value, skill_percent) -> float:
    """Calculates base damage below the DR breakpoint. This function expects
    that weapon/offhand modifiers have already been applied and are
    included in 'ap_value'. This function should only be used over
    'get_damage' when enemy DR is not known."""
    # Integer equivalent of 0.05 * AP * skill_percent/100
    return 5 * ap_value * skill_percent // 10000


# ===========================================================================


def get_species_ap_range(species_damage) -> tuple[int, int]:
    min_species_ap: int = 7 * species_damage // 10
    return min_species_ap, species_damage


# ===========================================================================
def calc_overcap_ap(ap_value: int, ap_cap: int) -> int:
    overcap_ap: int = ap_value - ap_cap
    if overcap_ap > 0:
        ap_value = ap_cap
    else:
        overcap_ap = 0
    return overcap_ap
