from .class_data import Class, Hit, Skill

# ----------------------------------------------------------------
tamer = Class(id=5, name="Tamer", dr=0, evasion=0)
# id = class ID xx = pre | 3xx = prime | 5xx = awk | 9xx = rabams
# ----------------------------------------------------------------
Leaf_Slash_X = Skill(
    id=5.01,
    class_id=5,
    name="Tamer - Leaf Slash X",
    acc_rate=0.1,
    hit1=Hit(damage=9.48, hit_count=5, pvp_mod=0.6),
)

# ----------------------------------------------------------------

Leaf_Slash = Skill(
    id=5.1,
    class_id=5,
    name="Tamer - Leaf Slash",
    acc_rate=0.1,
    hit1=Hit(damage=10.10, hit_count=5, pvp_mod=0.6),
)
# ----------------------------------------------------------------
