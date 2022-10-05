from .class_data import Class, Hit, Skill

# ----------------------------------------------------------------
warrior = Class(id=1, name="Warrior", dr=0, evasion=0)
# id = class ID xx = pre | 3xx = prime | 5xx = awk | 9xx = rabams
# ----------------------------------------------------------------
Slash_X = Skill(
    id=1.01,
    class_id=1,
    name="Slash X",
    acc_rate=0.1,
    hit1=Hit(damage=13.30, hit_count=4, pvp_mod=0.06),
    hit2=Hit(damage=13.30, hit_count=3, pvp_mod=0.06),
)


Slash = Skill(
    id=1.1,
    class_id=1,
    name="Slash",
    acc_rate=0.1,
    hit1=Hit(damage=13.30, hit_count=4, pvp_mod=0.06),
    hit2=Hit(damage=13.30, hit_count=3, pvp_mod=0.06),
)
# ----------------------------------------------------------------
