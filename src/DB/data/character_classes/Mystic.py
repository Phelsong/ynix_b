from .class_data import Class, Hit, Skill

# ----------------------------------------------------------------
mystic = Class(id=15, name="Mystic", dr=0, evasion=0)
# id = class ID xx = pre | 3xx = prime | 5xx = awk | 9xx = rabams
# ----------------------------------------------------------------
Mystic_Heavy_Fist_X = Skill(
    id=15.01,
    class_id=15,
    name="Mystic - Heavy Fist X",
    acc_rate=0.20,
    hit1=Hit(damage=7.60, hit_count=2, pvp_mod=0.23),
)
# ----------------------------------------------------------------

Mystic_Heavy_Fist = Skill(
    id=15.1,
    class_id=15,
    name="Mystic - Heavy Fist",
    acc_rate=0.20,
    hit1=Hit(damage=8.09, hit_count=2, pvp_mod=0.23),
)
# ----------------------------------------------------------------

Hurricane_Sweep = Skill(
    id=15.517,
    class_id=15,
    name="Hurricane Sweep",
    acc_rate=0.08,
    hit1=Hit(
        damage=10.03, hit_count=5, pvp_mod=0.696, pve_crit_rate=0.5, pvp_crit_rate=0.5
    ),
    hit2=Hit(
        damage=10.03, hit_count=5, pvp_mod=0.696, pve_crit_rate=0.5, pvp_crit_rate=0.5
    ),
    hit3=Hit(
        damage=10.03, hit_count=5, pvp_mod=0.696, pve_crit_rate=0.5, pvp_crit_rate=0.5
    ),
)

# ----------------------------------------------------------------

Tidal_Burst = Skill(
    id=15.505,
    class_id=15,
    name="Tidal Burst",
    acc_rate=0.10,
    hit1=Hit(
        damage=11.28, hit_count=4, pvp_mod=0.74, pve_crit_rate=0.65, pvp_crit_rate=0.65
    ),
    hit2=Hit(
        damage=11.28, hit_count=4, pvp_mod=0.74, pve_crit_rate=0.65, pvp_crit_rate=0.65
    ),
    hit3=Hit(
        damage=11.28, hit_count=4, pvp_mod=0.74, pve_crit_rate=0.65, pvp_crit_rate=0.65
    ),
    hit4=Hit(
        damage=11.28, hit_count=4, pvp_mod=0.74, pve_crit_rate=0.65, pvp_crit_rate=0.65
    ),
)

# ------------------------------------------------------------------------------

Rapid_Stream = Skill(
    id=15.508,
    class_id=15,
    name="Rapid Stream",
    acc_rate=0.1,
    hit1=Hit(
        damage=7.43, hit_count=4, pvp_mod=0.72, pve_crit_rate=0.5, pvp_crit_rate=0.5
    ),
    hit2=Hit(
        damage=7.43, hit_count=4, pvp_mod=0.72, pve_crit_rate=0.5, pvp_crit_rate=0.5
    ),
    hit3=Hit(
        damage=7.43, hit_count=4, pvp_mod=0.72, pve_crit_rate=0.5, pvp_crit_rate=0.5
    ),
    hit4=Hit(
        damage=7.43, hit_count=8, pvp_mod=0.72, pve_crit_rate=0.5, pvp_crit_rate=0.5
    ),
)
