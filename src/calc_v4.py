"""Calc V4"""
import random
from re import A

# ------------------
from ..db.queries import get_class_basic_skills_query

# ----------------------------------------------------------------
# Find/Jump to : Attacker, Defender, Calc, calc_if_crit, calc_if_hit, calc__hits, run_calc

class Attacker(object):
    def __init__(
        self,
        class_id,
        ap,
        aap,
        acc,
        acc_rate,
        crit_rate,
        monster_ap,
        kama_damage,
        demi_damage,
        human_damage,
        other_damage,
        crit_damage,
        back_damage,
        down_damage,
        air_damage,
        ap_combat_buffs,
        crit_combat_buffs,
        ap_debuffs,
        acc_combat_buffs,
        acc_debuffs,
        human_damage_debuffs,
    ):
        self.class_id = class_id
        self.ap = ap
        self.aap = aap
        self.acc = acc
        self.acc_rate = acc_rate
        self.crit_rate = crit_rate
        self.monster_ap = monster_ap
        self.kama_damage = kama_damage
        self.demi_damage = demi_damage
        self.human_damage = human_damage
        self.other_damage = other_damage
        self.crit_damage = crit_damage
        self.back_damage = back_damage
        self.down_damage = down_damage
        self.air_damage = air_damage
        self.ap_combat_buffs = ap_combat_buffs
        self.crit_combat_buffs = crit_combat_buffs
        self.ap_debuffs = ap_debuffs
        self.acc_combat_buffs = acc_combat_buffs
        self.acc_debuffs = acc_debuffs
        self.human_damage_debuffs = human_damage_debuffs
        self.t_ap = 0
        self.t_aap = 0
        [basic] = get_class_basic_skills_query(class_id)
        self.basic = basic["skill_details"]["hit1"]["damage"]


# ----------------------------------------------------------------


class Defender(object):
    def __init__(
        self,
        dr,
        dr_rate,
        evasion,
        evasion_rate,
        dr_combat_buffs,
        dr_debuffs,
        evasion_combat_buffs,
        evasion_debuffs,
        class_id,
        species="other",
    ):
        self.dr = dr
        self.dr_rate = dr_rate
        self.evasion = evasion
        self.evasion_rate = evasion_rate
        self.dr_combat_buffs = dr_combat_buffs
        self.dr_debuffs = dr_debuffs
        self.evasion_combat_buffs = evasion_combat_buffs
        self.evasion_debuffs = evasion_debuffs
        self.class_id = class_id
        self.species = species
        # class_id = 100 = PvE


# -----------------------------------------------------------------


class Calc:
    def __init__(self, attacker, defender, skill):
        self.attacker = attacker
        self.defender = defender
        self.skill = skill
        # -----------------------------
        # totals
        self.t_ap = (
            attacker.ap + attacker.ap_combat_buffs - attacker.ap_debuffs
            if defender.class_id != 100
            else attacker.ap
            + attacker.monster_ap
            + attacker.ap_combat_buffs
            - attacker.ap_debuffs
            - 9
            # -x = the min of the range of attack
        )

        self.t_acc_rate = (
            attacker.acc_rate
            + attacker.acc_combat_buffs
            + (attacker.acc * 0.21)
            - attacker.acc_debuffs
        )

        self.defender_t_evasion_rate = (
            defender.evasion_rate
            + (defender.evasion * 0.21)
            + defender.evasion_combat_buffs
            - defender.evasion_debuffs
        )

        self.defender_t_dr = (
            defender.dr + defender.dr_combat_buffs - defender.dr_debuffs
        )

        self.dr_rate = defender.dr_rate if defender.class_id != 100 else 0.8

        # ------------------------------
        # species damage aka +damage
        self.species_damage = 0
        if self.defender.species == "human":
            self.species_damage = attacker.human_damage
        elif self.defender.species == "demihuman":
            self.species_damage = attacker.demi_damage
        elif self.defender.species == "kamasylvian":
            self.species_damage = attacker.kama_damage
        elif self.defender.species == "other":
            self.species_damage = attacker.other_damage

    # --------------------------------------------------------------------------

    # =================================================================================
    # =============== Crits =================================
    # =================================================================================
    def calc_if_crit(self, hit_in):
        crit_chance = (
            self.attacker.crit_rate
            + self.attacker.crit_combat_buffs
            + hit_in["pvp_crit_rate"]
            if self.defender.class_id != 100
            # ^ PvP
            # > PvE :
            else self.attacker.crit_rate
            + self.attacker.crit_combat_buffs
            + hit_in["pve_crit_rate"]
        )
        crit_roll = random.randrange(0, 100)

        return True if crit_roll < (crit_chance * 100) else False

    # ---------------------------------------------------------------------------------------------

    # =================================================================================
    # =============== Hit Calc =================================
    # =================================================================================
    def calc_if_hit(self):
        hit_chance = self.t_acc_rate - self.defender_t_evasion_rate
        hit_roll = random.randrange(0, 100)
        return True if hit_roll > (hit_chance * 100) else False

    # ---------------------------------------------------------------------------------------------

    # =================================================================================
    # =============== Core Calc =================================
    # =================================================================================
    def calc_hits(self, hit_in, core=True):
        ap_range = ["Min, Max, Mean", 0, 18, 9]
        hit_value = hit_in["damage"]
        hit_count = 3 if core != True else hit_in["hit_count"]
        hit_counter = 1
        hits = []
        # ----------------------------------------
        while hit_counter <= hit_count:
            # did_hit = self.calc_if_hit()
            # if did_hit != True:
            #     hits.append(0)
            #     hit_counter += 1
            #     continue 
            is_crit = False if core != True else self.calc_if_crit(hit_in)
            rand_range = 0 if is_crit != True else 9
            ap_roll = (
                self.t_ap + random.randrange(rand_range, 18)
                if core == True
                else self.t_ap + ap_range[hit_counter]
            )
            e_ap = ap_roll - self.defender_t_dr
            conversion = False
            if e_ap < 0:
                e_ap += self.species_damage
                conversion = True
            # -------------------------------------
            # Core output calc !!!!!!!!!!!!!!!!!!!
            base_damage = (ap_roll) * (hit_value / self.attacker.basic)
            bonus_damage = (
                (self.species_damage * hit_value)
                if conversion != True
                else 0
            )
            rate = 0 if e_ap < 150 else 1
            ap_softcap_rolloff = .0825 * rate
            dr_rate = self.dr_rate if e_ap < 150 else self.dr_rate - ap_softcap_rolloff
            # --- ^ modifiers ---
            hit_damage = (
                ((base_damage + (e_ap * hit_value)) * dr_rate) + bonus_damage
                if e_ap > 0
                else base_damage * dr_rate
            )
            # !!!!!!!!!^^^^^^!!!!!!!!!!!!
            if is_crit:
                hits.append(round(hit_damage * (1 + self.attacker["crit_damage"])))
            else:
                hits.append(round(hit_damage))
            hit_counter += 1
        # -----------------------------------------
        hits.append(sum(hits))
        return hits

    # ---------------------------------------------------------------------------------------------------------------------------

    def run_calc(self):
        data = {
            "Hit_1_mean": None,
            "Hit_1_range": self.calc_hits(self.skill["hit1"], core=False),
            "Hit1": self.calc_hits(self.skill["hit1"]),
            "Hit2": self.calc_hits(self.skill["hit2"])
            if self.skill["hit2"] != None
            else None,
            "Hit3": self.calc_hits(self.skill["hit3"])
            if self.skill["hit3"] != None
            else None,
            "Hit4": self.calc_hits(self.skill["hit4"])
            if self.skill["hit4"] != None
            else None,
            "Hit5": self.calc_hits(self.skill["hit5"])
            if self.skill["hit5"] != None
            else None,
            "Hit6": self.calc_hits(self.skill["hit6"])
            if self.skill["hit6"] != None
            else None,
        }
        data['Hit_1_mean'] = data["Hit_1_range"][2],
        data["Hit_1_range"].pop(3)
        data["Hit_1_range"].pop(2)
        # print("Running Calc V4")
        # print("range =", data["Hit_1_range"][0], "-", data["Hit_1_range"][1])
        return data
