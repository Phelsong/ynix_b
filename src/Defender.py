""" Defender Object"""
# ------------------------------
class Defender(object):
    def __init__(self, defender_in):
        self.dr = defender_in["dr"]
        self.dr_rate = defender_in["dr_rate"]
        self.evasion = defender_in["evasion"]
        self.evasion_rate = defender_in["evasion_rate"]
        self.dr_combat_buffs = defender_in["dr_combat_buffs"]
        self.dr_debuffs = defender_in["dr_debuffs"]
        self.evasion_combat_buffs = defender_in["evasion_combat_buffs"]
        self.evasion_debuffs = defender_in["evasion_debuffs"]
        self.class_id = defender_in["class_id"]
        self.species = defender_in["species"]
        # class_id = 100 = PvE
