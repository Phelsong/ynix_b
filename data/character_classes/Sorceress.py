from .class_data import Class, Hit, Skill

# ----------------------------------------------------------------
sorceress = Class(id=3, name="Sorceress", dr=0, evasion=0)
# id = class ID xx = pre | 3xx = prime | 5xx = awk | 9xx = rabams
# ----------------------------------------------------------------
Dark_Split_X = Skill(
    id=3.01,
    class_id=3,
    name="Dark Split X",
    acc_rate=0.1,
    hit1=Hit(damage=12.19, hit_count=1, pvp_mod=0.54),
    hit2=Hit(damage=12.19, hit_count=1, pvp_mod=0.54),
    hit3=Hit(damage=12.19, hit_count=2, pvp_mod=0.54),
    hit4=Hit(damage=12.19, hit_count=3, pvp_mod=0.54),
)

# ----------------------------------------------------------------
Dark_Split = Skill(
    id=3.1,
    class_id=3,
    name="Dark Split",
    acc_rate=0.1,
    hit1=Hit(damage=12.98, hit_count=1, pvp_mod=0.54),
    hit2=Hit(damage=12.98, hit_count=1, pvp_mod=0.54),
    hit3=Hit(damage=12.98, hit_count=2, pvp_mod=0.54),
    hit4=Hit(damage=12.98, hit_count=3, pvp_mod=0.54),
)
# ----------------------------------------------------------------
