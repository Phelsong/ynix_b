""" Attacker Object"""
# from db.queries import get_class_basic_skills_query


# ------------------------------
class Attacker(object):
    def __init__(
        self,
        attacker_in,
    ) -> None:
        self.class_id: int = attacker_in["class_id"]
        self.ap: int = attacker_in["ap"]
        self.aap: int = attacker_in["aap"]
        self.acc: int = attacker_in["acc"]
        self.acc_rate: float = attacker_in["acc_rate"]
        self.crit_rate: float = attacker_in["crit_rate"]
        self.monster_ap: int = attacker_in["monster_ap"]
        self.kama_damage: int = attacker_in["kama_damage"]
        self.demi_damage: int = attacker_in["demi_damage"]
        self.human_damage: int = attacker_in["human_damage"]
        self.other_damage: int = attacker_in["other_damage"]
        self.crit_damage: float = attacker_in["crit_damage"]
        self.back_damage: float = attacker_in["back_damage"]
        self.down_damage: float = attacker_in["down_damage"]
        self.air_damage: float = attacker_in["air_damage"]
        self.ap_combat_buffs: int = attacker_in["ap_combat_buffs"]
        self.crit_combat_buffs: float = attacker_in["crit_combat_buffs"]
        self.ap_debuffs: int = attacker_in["ap_debuffs"]
        self.acc_combat_buffs: float = attacker_in["acc_combat_buffs"]
        self.acc_debuffs: float = attacker_in["acc_debuffs"]
        self.human_damage_debuffs: int = attacker_in["human_damage_debuffs"]
        self.t_ap: int = 0
        self.t_aap: int = 0
        # [basic] = get_class_basic_skills_query(self.class_id)
        # self.basic = basic["skill_details"]["hit1"]["damage"]
