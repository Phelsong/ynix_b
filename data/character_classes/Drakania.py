from .class_data import Class, Hit, Skill

# ----------------------------------------------------------------
drakania = Class(id=24, name="Drakania", dr=0, evasion=0)
# id = class ID xx = pre | 3xx = prime | 5xx = awk | 9xx = rabams
# ----------------------------------------------------------------
Slayer_Training_X = Skill(
    id=24.01,
    class_id=24,
    name="Slayer Training X",
    acc_rate=0.07,
    hit1=Hit(damage=7.52, hit_count=6, pvp_mod=0.4),
)
# ----------------------------------------------------------------


Slayer_Training = Skill(
    id=24.1,
    class_id=24,
    name="Slayer Training",
    acc_rate=0.07,
    hit1=Hit(damage=8.43, hit_count=6, pvp_mod=0.4),
)
# ----------------------------------------------------------------
