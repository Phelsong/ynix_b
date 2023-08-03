"""Calc V5"""
# libs
import numpy as np
import pandas as pd
from random import randint

# imports
from src.calc.calc_die import roll_range, roll_die
from src.calc.calc_dr import get_dr_range
from src.calc.calc_ap import (
    get_ap_range,
    get_species_ap_range,
    get_base_damage,
    calc_overcap_ap,
)


class CalcV5:
    """Contains damage calculation formulas and helpers
    Credit: @Honuamea for the Formula"""

    def simulate_damage(self, attacker, defender, skill, target, run_length=1):
        profile = {
            "min_ap": 0,
            "max_ap": 0,
            "min_species_ap": 0,
            "max_species_ap": 0,
            "dr": 0,
            "ap_cap": defender.ap_cap,
            "cap_modifier": defender.cap_modifier,
        }
        profile["min_ap"], profile["max_ap"] = get_ap_range(attacker)
        profile["min_species_ap"], profile["max_species_ap"] = get_species_ap_range(
            attacker, defender
        )
        profile["dr"] = defender.dr - defender.dr_debuffs

        # if run_type == "pve":
        self._run_pve(profile, skill)

    # ---------------------------------------------------------------
    def _run_pve(self, profile, skill, run_length=1):
        """Simulates damage for a given profile and skill"""
        dataset: dict = {}
        for i in range(run_length):
            hit_roll = self._calc_damage(profile, skill)
            dataset.setdefault(f"hit_{i}", hit_roll)

        return dataset

    # ---------------------------------------------------------------

    def _run_pvp(self, attacker, defender, skill):
        pass

    # ----------------------------------------------------------------
    # Damage calculations
    def _calc_damage(self, profile, skill):
        """General damage formula to be used if all input values are known.
        Applies base damage (5% of AP) below DR breakpoint, EAP damage
        (AP - DR + species) until any cap, and cap damage
        (ap_cap + cap_modifier * overcap_ap - enemy_dr + species) above the cap.
        All damage is then scaled by skill_percent."""
        # --------------
        rolled_ap: int = roll_range(profile["min_ap"], profile["max_ap"])
        rolled_species_ap: int = roll_range(
            profile["min_species_ap"], profile["max_species_ap"]
        )
        # --------------
        overcap_ap: int = calc_overcap_ap(rolled_ap, profile["ap_cap"])
        scalar_ap: int = rolled_ap - profile["dr"] + rolled_species_ap
        # -------------
        # This check is equivalent to eap_damage < 0.05 * ap_value
        # but is faster with no floating point issues
        if 20 * scalar_ap < rolled_ap:
            # Use the base damage formula
            return get_base_damage(rolled_ap, skill)

        e_ap: int = scalar_ap + (overcap_ap * profile["cap_modifier"])
        scaled_damage: int = e_ap * skill // 100
        return scaled_damage

    # ---------------------------------------------------------------

    # ---------------------------------------------------------------
    def get_median_eap_damage(ap_value, enemy_dr, skill_percent, species_ap=0):
        """Calculates damage below any AP cap. Note that AP & species AP inputs are
        both post-roll. This function should only be used over 'get_damage' when
        the AP Cap is not known."""
        eap_damage = ap_value - enemy_dr + species_ap
        # This check is equivalent to eap_damage < 0.05 * ap_value
        # but is faster with no floating point issues
        if 20 * eap_damage < ap_value:
            # Use the base damage formula
            return get_base_damage(ap_value, skill_percent)

        return eap_damage * skill_percent // 100

    # ---------------------------------------------------------------


# ================================

the_calc = CalcV5()


print("test debugger")


# def __init__(self, attacker, defender, skill):
#     self.attacker = attacker
#     self.defender = defender
#     self.skill = skill


# def get_pvp_base_damage(
#     ap_value, skill_percent, skill_pvp_damage_reduction, class_pvp_modifier
# ):
#     """Calcuates PvP base damage below the DR breakpoint. This function expects
#     that weapon/offhand modifiers have already been applied and are included
#     in 'ap_value'. This function should only be used over 'get_damage' when
#     enemy DR is not known."""
#     _global_pvp_modifier = 617  # 0.0617
#     denominator = 10000
#     # Integer equivalent of 0.05 * 0.0617 * AP * skill_percent/100 * pvp_mods
#     denominator *= 10000  # same as PvE formula
#     denominator *= 100  # adjust for extra 0.05
#     skill_pvp_damage_reduction = int(100 * skill_pvp_damage_reduction)
#     class_pvp_modifier = int(100 * class_pvp_modifier)
#     denominator *= 100 * 100  # adjust for integer skill pvp mod & class pvp mod
#     pvp_skill_percent = skill_percent * (100 - skill_pvp_damage_reduction)
#     # pylint: disable=line-too-long
#     return (
#         5
#         * ap_value
#         * pvp_skill_percent
#         * class_pvp_modifier
#         * _global_pvp_modifier
#         // denominator
#     )
