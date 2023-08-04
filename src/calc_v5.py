"""Calc V5"""
# libs
import numpy as np
import pandas as pd
from random import randint
from typing import Any

# imports
from src.Attacker import Attacker
from src.Defender import Defender
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

    def simulate_damage(
        self,
        attacker: Attacker,
        defender: Defender,
        skill: dict,
        run_length: int = 1,
        run_type=1,
    ) -> dict[str, int | float | Any]:
        # ----------

        profile: dict[str, int | float] = {
            "min_ap": 0,
            "max_ap": 0,
            "min_species_ap": 0,
            "max_species_ap": 0,
            "dr": 0,
            "ap_cap": defender.ap_cap,
            "cap_modifier": defender.cap_modifier,
        }
        profile["min_ap"], profile["max_ap"] = get_ap_range(attacker)
        profile["dr"] = defender.dr - defender.dr_debuffs

        attacker_vs_species = self._defender_species(attacker, defender)
        profile["min_species_ap"], profile["max_species_ap"] = get_species_ap_range(
            attacker_vs_species
        )

        if run_type == 1:
            return self._run_skill_pve(profile=profile, skill=skill)
        elif run_type == 2:
            return {"pvp": 0}
            # return self._run_pvp(profile, skill)
        else:
            return {"error": "invalid parameters"}

    # ---------------------------------------------------------------
    def get_median_eap_damage(self, ap_value, enemy_dr, skill_percent, species_ap=0):
        """Calculates damage below any AP cap. Note that AP & species AP inputs are
        both post-roll. This function should only be used over 'get_damage' when
        the AP Cap is not known."""

        eap_damage = ap_value - enemy_dr + species_ap

        # This check is equivalent to eap_damage < 0.05 * ap_value
        if 20 * eap_damage < ap_value:
            # Use the base damage formula
            return get_base_damage(ap_value, skill_percent)

        return eap_damage * skill_percent // 100

    # ---------------------------------------------------------------

    def _run_skill_pve(self, profile, skill) -> dict[str, str | list[float]]:
        """Simulates damage for a given profile and skill"""

        dataset: dict[str, str | list[float]] = {"skill": skill["name"]}

        for i in range(1, skill["attack_count"] + 1):
            rolls: list[float] = []
            for u in range(1, skill[f"hit{i}"]["hit_count"] + 1):
                rolls.append(
                    int(self._calc_damage(profile=profile, skill=skill[f"hit{i}"]))
                )
            dataset.setdefault(f"hit_{i}", rolls)

        return dataset

    # ---------------------------------------------------------------

    def _run_pvp(self, profile, skill) -> None:
        """TBI"""
        pass

    # ----------------------------------------------------------------
    # Damage calculations
    def _calc_damage(self, profile, skill) -> float | int:
        """General damage formula to be used if all input values are known.
        Applies base damage (5% of AP) below DR breakpoint, EAP damage
        (AP - DR + species) until any cap, and cap damage
        (ap_cap + cap_modifier * overcap_ap - enemy_dr + species) above the cap.
        All damage is then scaled by skill_percent."""
        # --------------
        rolled_ap: int = roll_range(min=profile["min_ap"], max=profile["max_ap"])
        rolled_species_ap: int = roll_range(
            profile["min_species_ap"], profile["max_species_ap"]
        )
        # --------------
        overcap_ap: int = calc_overcap_ap(ap_value=rolled_ap, ap_cap=profile["ap_cap"])
        scalar_ap: int = rolled_ap - profile["dr"] + rolled_species_ap
        # -------------
        # This check is equivalent to eap_damage < 0.05 * ap_value
        # but is faster with no floating point issues
        if 20 * scalar_ap < rolled_ap:
            # Use the base damage formula
            print("returning base damage")
            return get_base_damage(ap_value=rolled_ap, skill_percent=skill["damage"])

        e_ap: int = scalar_ap + (overcap_ap * profile["cap_modifier"])
        scaled_damage: int = np.multiply(e_ap, skill["damage"])

        return scaled_damage

    # ---------------------------------------------------------------

    def _defender_species(self, attacker: Attacker, defender: Defender) -> int:
        """returns attacker species damage"""
        if defender.species == "human":
            return attacker.human_damage
        elif defender.species == "demihuman":
            return attacker.demi_damage
        elif defender.species == "kamasylvian":
            return attacker.kama_damage
        else:
            return attacker.other_damage


# ================================

the_calc = CalcV5()


# def __init__(self, attacker, defender, skill):
#     self.attacker = attacker
#     self.defender = defender
#     self.skill = skill


# def _get_pvp_base_damage(
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
