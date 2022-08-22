from .class_data import Class, Hit, Skill

# ----------------------------------------------------------------
mystic = Class(id=15, name="Mystic", dr=0, evasion=0)
# id = class ID xx = pre | 3xx = prime | 5xx = awk | 9xx = rabams
# ----------------------------------------------------------------
Mystic_Heavy_Fist_X = Skill(
    id=15.01,
    class_id=15,
    name="Mystic - Heavy Fist X",
    acc_rate=0.20,
    hit1=Hit(damage=7.60, hit_count=2, pvp_mod=0.23),
)
# ----------------------------------------------------------------

Mystic_Heavy_Fist = Skill(
    id=15.1,
    class_id=15,
    name="Mystic - Heavy Fist",
    acc_rate=0.20,
    hit1=Hit(damage=8.09, hit_count=2, pvp_mod=0.23),
)
# ----------------------------------------------------------------
