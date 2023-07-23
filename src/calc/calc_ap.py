"""ap related calcs"""
# libs

# imports
from re import T
from src.calc.calc_die import roll_die


# ===========================================================================
def get_ap_range(attacker):
    return attacker.ap


def roll_ap(profile):
    """Calculates (min_ap, max_ap) for the given 'ap_value' using
    'attack_dice' (list of character + weapon dice) and 'gear_offsets'
    (list of other offsets, like Kutum's -2). Any given 'species_damage'
    can be included in this calculation, but it is not recommended, as it
    behaves differently than other AP both below DR & above caps."""
    # ---------
    # if skill == "Physical":
    #     damage = self.get_physical_damage(attacker, defender, min_dr, max_dr)
    # elif skill == "Magic":
    #     damage = self.get_magic_damage(attacker, defender, min_dr, max_dr)
    # else:
    #     damage = self.get_physical_damage(attacker, defender, min_dr, max_dr)

    min_ap = profile["min_ap"]
    max_ap = profile["max_ap"]

    return min_ap_roll, max_ap_roll


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
    min_species_ap = 7 * species_damage // 10
    return min_species_ap, species_damage


# ===========================================================================
def calc_overcap_ap(ap_value, ap_cap):
    overcap_ap = ap_value - ap_cap
    if overcap_ap > 0:
        ap_value = ap_cap
    else:
        overcap_ap = 0
    return overcap_ap
