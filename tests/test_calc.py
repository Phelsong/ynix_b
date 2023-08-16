from typing import Any

from functions.calc_v5 import the_calc
from functions.Attacker import Attacker
from functions.Defender import Defender
from db.queries import get_skill_details_query


def run_calc_test() -> None:
    attacker_in: dict[str, int | float | str] = {
        "class_id": 3,
        "ap": 600,
        "aap": 0,
        "acc": 0,
        "acc_rate": 0,
        "crit_rate": 0.2,
        "monster_ap": 25,
        "kama_damage": 18,
        "demi_damage": 0,
        "human_damage": 21,
        "other_damage": 0,
        "crit_damage": 0.04,
        "back_damage": 0,
        "down_damage": 0,
        "air_damage": 0,
        "ap_combat_buffs": 0,
        "crit_combat_buffs": 0,
        "ap_debuffs": 0,
        "acc_combat_buffs": 0,
        "acc_debuffs": 0,
        "human_damage_debuffs": 0,
    }
    defender_in: dict[str, int | float | str] = {
        "dr": 430,
        "dr_rate": 0,
        "evasion": 0,
        "evasion_rate": 0,
        "dr_combat_buffs": 0,
        "dr_debuffs": 0,
        "evasion_combat_buffs": 0,
        "evasion_debuffs": 0,
        "class_id": 100,
        "species": "kamasylvian",
        "ap_cap": 9999,
        "cap_modifier": 1,
    }
    skill_id = [3.1]
    # ------------------------------
    attacker = Attacker(attacker_in)
    defender = Defender(defender_in)
    [skill] = get_skill_details_query(skill_id[0])
    print(the_calc.simulate_damage(attacker, defender, skill["skill_details"]))


if __name__ == "__main__":
    for i in range(10):
        run_calc_test()
