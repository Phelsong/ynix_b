from .class_data import Class, Hit, Skill

# ----------------------------------------------------------------
sage = Class(id=22, name="Sage", dr=0, evasion=0)
# id = class ID xx = pre | 3xx = prime | 5xx = awk | 9xx = rabams
# ----------------------------------------------------------------
Kyve_Mastery_X = Skill(
    id=22.01,
    class_id=22,
    name="Kyve Mastery X",
    acc_rate=0.2,
    hit1=Hit(damage=10.06, hit_count=2, pvp_mod=0.3),
)

#----------------------------------------------------------------

Kyve_Mastery = Skill(
    id=22.1,
    class_id=22,
    name="Kyve Mastery",
    acc_rate=0.2,
    hit1=Hit(damage=10.70, hit_count=2, pvp_mod=0.3),
)
# ----------------------------------------------------------------
