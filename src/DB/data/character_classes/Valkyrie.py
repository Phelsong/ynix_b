from .class_data import Class, Hit, Skill

# ----------------------------------------------------------------
valkyrie = Class(id=6, name="Valkyrie", dr=0, evasion=0)
# id = class ID xx = pre | 3xx = prime | 5xx = awk | 9xx = rabams
# ----------------------------------------------------------------
Valkyrie_Slash_X = Skill(
    id=6.01,
    class_id=6,
    name="Valkyrie Slash X",
    acc_rate=0,
    hit1=Hit(damage=10.43, hit_count=6, pvp_mod=0.52),
)

#----------------------------------------------------------------



Valkyrie_Slash = Skill(
    id=6.1,
    class_id=6,
    name="Valkyrie Slash",
    acc_rate=0,
    hit1=Hit(damage=11.11, hit_count=3, pvp_mod=0.52),
)
# ----------------------------------------------------------------
