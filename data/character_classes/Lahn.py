from .class_data import Class, Hit, Skill

# ----------------------------------------------------------------
lahn = Class(id=16, name="Lahn", dr=0, evasion=0)
# id = class ID xx = pre | 3xx = prime | 5xx = awk | 9xx = rabams
# ----------------------------------------------------------------
Moondance_X = Skill(
    id=16.01,
    class_id=16,
    name="Moondance X",
    acc_rate=0.115,
    hit1=Hit(damage=4.72, hit_count=5, pvp_mod=0.199),
)
# ----------------------------------------------------------------


Moondance = Skill(
    id=16.1,
    class_id=16,
    name="Moondance",
    acc_rate=0.115,
    hit1=Hit(damage=5.02, hit_count=5, pvp_mod=0.199),
)
# ----------------------------------------------------------------
