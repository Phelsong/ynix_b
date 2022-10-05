from .class_data import Class, Hit, Skill

# ----------------------------------------------------------------
hashashin = Class(id=20, name="Hashashin", dr=0, evasion=0)
# id = class ID xx = pre | 3xx = prime | 5xx = awk | 9xx = rabams
# ----------------------------------------------------------------
Shamshir_Training_X = Skill(
    id=20.01,
    class_id=20,
    name="Shamshir Training X",
    acc_rate=0,
    hit1=Hit(damage=9.96, hit_count=2, pvp_mod=0.20),
)
# ----------------------------------------------------------------


Shamshir_Training = Skill(
    id=20.1,
    class_id=20,
    name="Shamshir Training",
    acc_rate=0,
    hit1=Hit(damage=10.60, hit_count=2, pvp_mod=0.20),
)
# ----------------------------------------------------------------
