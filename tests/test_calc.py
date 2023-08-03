from src.calc_v5 import the_calc
from src.Attacker import Attacker
from src.Defender import Defender


def run_calc_test():
    attacker_in = {
        "class_id": 18,
        "ap": 430,
        "aap": 0,
        "acc": 0,
        "acc_rate": 0,
        "crit_rate": 0.2,
        "monster_ap": 0,
        "kama_damage": 18,
        "demi_damage": 0,
        "human_damage": 0,
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
    }
    defender_in = {
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
    }
    skill_id = [18.01]
    # ------------------------------
    attacker = Attacker(attacker_in)
    defender = Defender(defender_in)
    [skill] = get_skill_details_query(skill_id[0])
    print(the_calc.simulate_damage(attacker, defender, skill, target="human"))


if __name__ == "__main__":
    run_calc_test()