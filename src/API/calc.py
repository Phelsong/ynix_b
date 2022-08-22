import random

# ------------------
from __init__ import get_class_basic_skills_query

# ----------------------------------------------------------------
# Find/Jump to : Attacker, Defender, Calc, calc_mean, calc_range, calc_if_crit, calc_hits, run_calc


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
        # 100 = PvE


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
        )

        self.t_acc_rate = (
            attacker.acc_rate
            + attacker.acc_combat_buffs
            + (attacker.acc * 0.21)
            - attacker.acc_debuffs
        )

        self.t_evasion_rate = (
            defender.evasion_rate
            + (defender.evasion * 0.21)
            + defender.evasion_combat_buffs
            - defender.evasion_debuffs
        )

        self.t_dr = defender.dr + defender.dr_combat_buffs - defender.dr_debuffs

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
    def calc_mean(self):
        hit_value = self.skill["hit1"]["damage"]
        damage_mean = self.t_ap - self.t_dr
        species_ap_mean = 0
        # -------------------------------------
        if damage_mean > 0:
            damage_mean += self.species_damage * 2
        elif damage_mean < 0:
            d_temp = self.species_damage - abs(damage_mean) / 2
            species_ap_mean = (
                d_temp * 2 + abs(damage_mean) / 2
                if d_temp > 0
                else self.species_damage / 2
            )
        # --------------------------------------
        e_ap_mean = damage_mean + species_ap_mean
        base_damage_mean = (self.t_ap + species_ap_mean) * (
            hit_value / self.attacker.basic
        )
        hit_damage_mean = (
            e_ap_mean * hit_value + base_damage_mean
            if e_ap_mean > 0
            else base_damage_mean
        ) * 0.8
        # -------------------------------------
        return round(hit_damage_mean)

    # ------------------------------------------------------------------------------------------------
    def calc_range(self):
        hit_value = self.skill["hit1"]["damage"]
        damage_low = (self.t_ap - 9) - self.t_dr
        damage_high = (self.t_ap + 9) - self.t_dr
        species_ap_low = 0
        species_ap_high = 0

        # ------------------------------
        if damage_low > 0:
            damage_low += self.species_damage * 2
        elif damage_low < 0:
            hd_temp = self.species_damage - abs(damage_low) / 2
            species_ap_low = (
                hd_temp * 2 + abs(damage_low) / 2
                if hd_temp > 0
                else self.species_damage / 2
            )
        # --------
        if damage_high > 0:
            damage_high += self.species_damage * 2
        elif damage_high < 0:
            hd_temp = self.species_damage - abs(damage_high) / 2
            species_ap_high = (
                hd_temp * 2 + abs(damage_high) / 2
                if hd_temp > 0
                else self.species_damage / 2
            )
        # ------------------------------
        e_ap_low = damage_low + species_ap_low
        base_damage_low = (self.t_ap + species_ap_low) * (
            hit_value / self.attacker.basic
        )
        # ---------
        e_ap_high = damage_high + species_ap_high
        base_damage_high = (self.t_ap + species_ap_high) * (
            hit_value / self.attacker.basic
        )
        # ------------------------------
        hit_damage_low = (
            e_ap_low * hit_value + base_damage_low if e_ap_low > 0 else base_damage_low
        ) * 0.8

        hit_damage_high = (
            e_ap_high * hit_value + base_damage_high
            if e_ap_high > 0
            else base_damage_high
        ) * 0.8
        # ------------------------------
        # crit range =
        crit_range_low = hit_damage_low + hit_damage_low * (
            1 + self.attacker.crit_damage
        )
        crit_range_high = hit_damage_high + hit_damage_high * (
            1 + self.attacker.crit_damage
        )
        # ------------------------------
        return [
            round(hit_damage_low),
            round(hit_damage_high),
            round(crit_range_low),
            round(crit_range_high),
        ]

    # --------------------------------------------------------------------------------------------

    def calc_if_crit(self, hit_in, this_hit):
        crit_chance = (
            self.attacker.crit_rate
            + self.attacker.crit_combat_buffs
            + hit_in["pvp_crit_rate"]
            if self.defender.class_id != 100
            else self.attacker.crit_rate
            + self.attacker.crit_combat_buffs
            + hit_in["pve_crit_rate"]
        )
        roll = random.randrange(0, 100)

        return (
            this_hit + this_hit * (1 + self.attacker.crit_damage)
            if roll < (crit_chance * 100)
            else this_hit
        )

    # ---------------------------------------------------------------------------------------------

    def calc_hits(self, hit_in):
        hit_value = hit_in["damage"]
        hit_count = hit_in["hit_count"]
        hit_counter = 1
        hits = []
        # ----------------------------------------
        while hit_counter <= hit_count:
            e_ap = (self.t_ap - 9 + random.randrange(0, 18)) - self.t_dr
            species_ap = 0
            if e_ap > 0:
                e_ap += self.species_damage * 2
            elif e_ap < 0:
                hd_temp = self.species_damage - abs(e_ap) / 2
                species_ap = (
                    hd_temp * 2 + abs(e_ap) / 2
                    if hd_temp > 0
                    else self.species_damage / 2
                )
            # -------------------------------------
            # Core output calc !!!!!!!!!!!!!!!!!!!
            e_ap += species_ap
            base_damage = (self.t_ap + species_ap) * (hit_value / self.attacker.basic)
            print(e_ap)
            hit_damage = (
                e_ap * hit_value + base_damage 
                if e_ap > 0 
                else base_damage
            ) * 0.8
            # !!!!!!!!!^^^^^^!!!!!!!!!!!!
            hits.append(round(self.calc_if_crit(hit_in, hit_damage)))
            hit_counter += 1
        # -----------------------------------------
        hits.append(sum(hits))
        return hits

    # ---------------------------------------------------------------------------------------------------------------------------

    def run_calc(self):
        data = {
            "Hit 1 mean": self.calc_mean(),
            "Hit 1 range": self.calc_range(),
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
        return data
