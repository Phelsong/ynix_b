from .class_data import Class, Hit, Skill

# ----------------------------------------------------------------
kunoichi = Class(id=11, name="Kunoichi", dr=0, evasion=0)
# id = class ID xx = pre | 3xx = prime | 5xx = awk | 9xx = rabams
# ----------------------------------------------------------------
Kuno_Wind_Slash_X = Skill(
    id=11.01,
    class_id=11,
    name="Kuno - Wind Slash X",
    acc_rate=0.23,
    hit1=Hit(damage=9.89, hit_count=2, pvp_mod=0.52),
)
# ----------------------------------------------------------------

Kuno_Wind_Slash = Skill(
    id=11.1,
    class_id=11,
    name="Kuno - Wind Slash",
    acc_rate=0.23,
    hit1=Hit(damage=9.89, hit_count=2, pvp_mod=0.52),
)
# ----------------------------------------------------------------
