""" Defender Object"""
# ------------------------------


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
