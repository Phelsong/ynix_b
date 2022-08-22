from .class_data import Class, Hit, Skill

# ----------------------------------------------------------------
nova = Class(id=21, name="Nova", dr=0, evasion=0)
# id = class ID xx = pre | 3xx = prime | 5xx = awk | 9xx = rabams
# ----------------------------------------------------------------
Flowing_Star_X = Skill(
    id=21.01,
    class_id=21,
    name="Flowing Star X",
    acc_rate=0.08,
    hit1=Hit(damage=8.75, hit_count=15, pvp_mod=0.3),
)
# ----------------------------------------------------------------


Flowing_Star = Skill(
    id=21.1,
    class_id=21,
    name="Flowing Star",
    acc_rate=0.08,
    hit1=Hit(damage=9.68, hit_count=15, pvp_mod=0.3),
)
# ----------------------------------------------------------------
