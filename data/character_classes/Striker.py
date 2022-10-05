from .class_data import Class, Hit, Skill

# ----------------------------------------------------------------
striker = Class(id=14, name="Striker", dr=0, evasion=0)
# id = class ID xx = pre | 3xx = prime | 5xx = awk | 9xx = rabams
# ----------------------------------------------------------------
Heavy_Fist_X = Skill(
    id=14.01,
    class_id=14,
    name="Heavy Fist X",
    acc_rate=0.20,
    hit1=Hit(damage=6.97, hit_count=2, pvp_mod=0.29),
)

# ----------------------------------------------------------------
Heavy_Fist = Skill(
    id=14.1,
    class_id=14,
    name="Heavy Fist",
    acc_rate=0.20,
    hit1=Hit(damage=7.42, hit_count=2, pvp_mod=0.29),
)
# ----------------------------------------------------------------
