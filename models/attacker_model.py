""" Attacker Object"""
# from db.queries import get_class_basic_skills_query
from pydantic import BaseModel


class Attacker_Model(BaseModel):
    ap: int
    aap: int
    acc: int
    acc_rate: float
    crit_rate: float
    monster_ap: int
    kama_damage: int
    demi_damage: int
    human_damage: int
    other_damage: int
    crit_damage: float
    back_damage: float
    down_damage: float
    air_damage: float
    ap_combat_buffs: int
    crit_combat_buffs: float
    ap_debuffs: int
    acc_combat_buffs: float
    acc_debuffs: float
    human_damage_debuffs: int
    t_ap: int
    t_aap: int


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
