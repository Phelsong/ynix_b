from .class_data import Class, Hit, Skill

# ----------------------------------------------------------------
ninja = Class(id=12, name="Ninja", dr=0, evasion=0)
# id = class ID xx = pre | 3xx = prime | 5xx = awk | 9xx = rabams
# ----------------------------------------------------------------
Wind_Slash_X = Skill(
    id=12.01,
    class_id=12,
    name="Wind Slash X",
    acc_rate=0.23,
    hit1=Hit(damage=9.29, hit_count=1, pvp_mod=0.46),
)
# ----------------------------------------------------------------

Wind_Slash = Skill(
    id=12.1,
    class_id=12,
    name="Wind Slash",
    acc_rate=0.23,
    hit1=Hit(damage=9.89, hit_count=1, pvp_mod=0.46),
)
# ----------------------------------------------------------------
