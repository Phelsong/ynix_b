from .class_data import Class, Hit, Skill

# ----------------------------------------------------------------
ranger = Class(id=2, name="Ranger", dr=0, evasion=0)
# id = class ID xx = pre | 3xx = prime | 5xx = awk | 9xx = rabams
# ----------------------------------------------------------------
Bow_Skill_X = Skill(
    id=2.01,
    class_id=2,
    name="Bow Skill X",
    acc_rate=0.1,
    hit1=Hit(damage=17.51, hit_count=3, pvp_mod=0.29),
    hit2=Hit(damage=17.51, hit_count=2, pvp_mod=0.29),
)
# ----------------------------------------------------------------

Bow_Skill = Skill(
    id=2.1,
    class_id=2,
    name="Bow Skill",
    acc_rate=0.1,
    hit1=Hit(damage=18.54, hit_count=3, pvp_mod=0.29),
    hit2=Hit(damage=18.54, hit_count=2, pvp_mod=0.29),
)
# ----------------------------------------------------------------
