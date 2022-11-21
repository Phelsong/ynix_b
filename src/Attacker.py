""" Attacker Object"""
from db.queries import get_class_basic_skills_query

# ------------------------------
class Attacker(object):
    def __init__(self, attacker_in):
        self.class_id = attacker_in["class_id"]
        self.ap = attacker_in["ap"]
        self.aap = attacker_in["aap"]
        self.acc = attacker_in["acc"]
        self.acc_rate = attacker_in["acc_rate"]
        self.crit_rate = attacker_in["crit_rate"]
        self.monster_ap = attacker_in["monster_ap"]
        self.kama_damage = attacker_in["kama_damage"]
        self.demi_damage = attacker_in["demi_damage"]
        self.human_damage = attacker_in["human_damage"]
        self.other_damage = attacker_in["other_damage"]
        self.crit_damage = attacker_in["crit_damage"]
        self.back_damage = attacker_in["back_damage"]
        self.down_damage = attacker_in["down_damage"]
        self.air_damage = attacker_in["air_damage"]
        self.ap_combat_buffs = attacker_in["ap_combat_buffs"]
        self.crit_combat_buffs = attacker_in["crit_combat_buffs"]
        self.ap_debuffs = attacker_in["ap_debuffs"]
        self.acc_combat_buffs = attacker_in["acc_combat_buffs"]
        self.acc_debuffs = attacker_in["acc_debuffs"]
        self.human_damage_debuffs = attacker_in["human_damage_debuffs"]
        self.t_ap = 0
        self.t_aap = 0
        [basic] = get_class_basic_skills_query(self.class_id)
        self.basic = basic["skill_details"]["hit1"]["damage"]
