from .class_data import Class, Hit, Skill

# ----------------------------------------------------------------
maewha = Class(id=10, name="Maewha", dr=0, evasion=0)
# id = class ID xx = pre | 3xx = prime | 5xx = awk | 9xx = rabams
# ----------------------------------------------------------------
Slice_X = Skill(
    id=10.01,
    class_id=10,
    name="Maewha - Slice X",
    acc_rate=0.05,
    hit1=Hit(damage=9.96, hit_count=6, pvp_mod=0.64),
)
# ----------------------------------------------------------------
Slice = Skill(
    id=10.1,
    class_id=10,
    name="Maewha - Slice",
    acc_rate=0.05,
    hit1=Hit(damage=10.60, hit_count=6, pvp_mod=0.55),
)
# ----------------------------------------------------------------
