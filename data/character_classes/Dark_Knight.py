from .class_data import Class, Hit, Skill

# ----------------------------------------------------------------
dark_knight = Class(id=13, name="Dark Knight", dr=0, evasion=0)
# id = class ID xx = pre | 3xx = prime | 5xx = awk | 9xx = rabams
# ----------------------------------------------------------------
DK_Base = Skill(
    id=13.01,
    class_id=13,
    name="DK Base",
    acc_rate=0.20,
    hit1=Hit(damage=6.43, hit_count=1, pvp_mod=0.13),
)
# ----------------------------------------------------------------


Kriegsmesser_Training = Skill(
    id=13.1,
    class_id=13,
    name="Kriegsmesser Training",
    acc_rate=0.20,
    hit1=Hit(damage=6.85, hit_count=9, pvp_mod=0.13),
)
# ----------------------------------------------------------------

Touch_of_Explotation = Skill(
    id=13.503,
    class_id=13,
    name="Touch_of_Explotation",
    acc_rate=0.06,
    hit1=Hit(damage=9.23, hit_count=3, pvp_mod=0.15, pve_crit_rate=0.5),
    hit2=Hit(damage=9.23, hit_count=3, pvp_mod=0.15, pve_crit_rate=0.5),
    hit3=Hit(damage=9.23, hit_count=3, pvp_mod=0.15, pve_crit_rate=0.5),
    hit4=Hit(damage=9.23, hit_count=5, pvp_mod=0.15, pve_crit_rate=0.5),
)
