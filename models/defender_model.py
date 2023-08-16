""" Defender Object"""
# ------------------------------
from pydantic import BaseModel


class Defender_Model(BaseModel):
    dr: int
    dr_rate: float
    evasion: int
    evasion_rate: float
    dr_combat_buffs: int
    dr_debuffs: int
    evasion_combat_buffs: float
    evasion_debuffs: float
    class_id: int
    species: str
    ap_cap: int
    cap_modifier: float
    # class_id = 100 = PvE


class Defender(object):
    def __init__(self, defender_in) -> None:
        self.dr: int = defender_in["dr"]
        self.dr_rate: float = defender_in["dr_rate"]
        self.evasion: int = defender_in["evasion"]
        self.evasion_rate: float = defender_in["evasion_rate"]
        self.dr_combat_buffs: int = defender_in["dr_combat_buffs"]
        self.dr_debuffs: int = defender_in["dr_debuffs"]
        self.evasion_combat_buffs: float = defender_in["evasion_combat_buffs"]
        self.evasion_debuffs: float = defender_in["evasion_debuffs"]
        self.class_id: int = defender_in["class_id"]
        self.species: str = defender_in["species"]
        self.ap_cap: int = defender_in["ap_cap"]
        self.cap_modifier: float = defender_in["cap_modifier"]
        # class_id = 100 = PvE
