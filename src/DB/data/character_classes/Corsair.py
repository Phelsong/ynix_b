from .class_data import Class, Hit, Skill

# ----------------------------------------------------------------
corsair = Class(id=23, name="Corsair", dr=0, evasion=0)
# id = class ID xx = pre | 3xx = prime | 5xx = awk | 9xx = rabams
# ----------------------------------------------------------------
Splashin_Around_X = Skill(
    id=23.01,
    class_id=23,
    name="Splashin' Around X",
    acc_rate=0.05,
    hit1=Hit(damage=5.72, hit_count=3, pvp_mod=0.40),
)
# ----------------------------------------------------------------

Splashin_Around = Skill(
    id=23.1,
    class_id=23,
    name="Splashin' Around",
    acc_rate=0.05,
    hit1=Hit(damage=6.40, hit_count=3, pvp_mod=0.40),
)
# ----------------------------------------------------------------
