from .class_data import Class, Hit, Skill

# ----------------------------------------------------------------
maegu = Class(id=99, name="Maegu", dr=0, evasion=0)
# id = class ID xx = pre | 3xx = prime | 5xx = awk | 9xx = rabams
# ----------------------------------------------------------------
Tal = Skill(
    id=8.01,
    class_id=8,
    name="Witch - Staff Attack X",
    acc_rate=0.45,
    hit1=Hit(damage=11.83, hit_count=3, pvp_mod=0.12),
)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
