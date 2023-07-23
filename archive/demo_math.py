from calc import *

from ..DB.queries import get_skill_details_query

# ----------------------------------------------------------------
demo_attacker = {
    'ap': 529,  
    'aap': 0,
    'acc': 0,
    'acc_rate': 0,
    'crit_rate': .50,
    'monster_ap': 190,
    'kama_damage': 24,
    'demi_damage': 24,
    'human_damage': 24,
    'other_damage': 24,
    'crit_damage': 0,
    'back_damage': 0,
    'down_damage': 0,
    'air_damage': 0,
    'ap_combat_buffs': 50,
    'crit_combat_buffs': 0,
    'ap_debuffs': 0,
    'acc_combat_buffs': 0,
    'acc_debuffs': 0,
    'human_damage_debuffs': 0,
}
demo_defender = {
    'dr': 850,
    'dr_rate': 0,
    'evasion': 0,
    'evasion_rate': 0,
    'dr_combat_buffs': 0,
    'dr_debuffs': 35,
    'evasion_combat_buffs': 0,
    'evasion_debuffs': 0,
    'class': 100,
    'species': 'human',
}


def demo_run(attacker_in, defender_in, skill_id=18.01):
    [skill] = get_skill_details_query(skill_id)
    attacker = Attacker(attacker_in['ap'], attacker_in['aap'], attacker_in['acc'], attacker_in['acc_rate'], attacker_in['crit_rate'], attacker_in['monster_ap'], attacker_in['kama_damage'], attacker_in['demi_damage'], attacker_in['human_damage'], attacker_in['other_damage'], attacker_in['crit_damage'], attacker_in['back_damage'], attacker_in['down_damage'], attacker_in['air_damage'], attacker_in['ap_combat_buffs'], attacker_in['crit_combat_buffs'], attacker_in['ap_debuffs'], attacker_in['acc_combat_buffs'], attacker_in['acc_debuffs'], attacker_in['human_damage_debuffs'])
    defender = Defender(defender_in['dr'], defender_in['dr_rate'], defender_in['evasion'], defender_in['evasion_rate'], defender_in['dr_combat_buffs'], defender_in['dr_debuffs'], defender_in['evasion_combat_buffs'], defender_in['evasion_debuffs'])
    calc = Calc(attacker, defender, skill["skill_details"])
    return calc.run_calc()
print (demo_run(demo_attacker, demo_defender))