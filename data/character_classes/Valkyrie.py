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

# ----------------------------------------------------------------


Valkyrie_Slash = Skill(
    id=6.002,
    class_id=6,
    name="Valkyrie Slash",
    acc_rate=0,
    hit1=Hit(damage=11.11, hit_count=3, pvp_mod=0.52),
)
# ----------------------------------------------------------------

Sharp_Light = Skill(
    id=6.011,
    class_id=6,
    name="Sharp_Light",
    acc_rate=0.1,
    hit1=Hit(
        damage=7.59, hit_count=3, pvp_mod=0.37, reduced_on_cd_amount=0.2, air_attack=True
    ),
    reduced_on_cd=True
)

# ----------------------------------------------------------------

Judgment_of_Light = Skill(
    id=6.029,
    class_id=6,
    name="Judgment of Light",
    acc_rate=0.15,
    hit1=Hit(damage=12.40, hit_count=11, pvp_mod=0.251, air_attack=True),
)

##====================================================================
############################## Prime #############################
##====================================================================

# -------------------------------------------------------------------
Prime_Judgment_of_Light = Skill(
    id=6.316,
    class_id=6,
    name="Prime Judgment of Light",
    acc_rate=0.15,
    hit1=Hit(damage=14.97, hit_count=7, pvp_mod=0.55, pve_crit_rate=1, air_attack=True),
    hit2=Hit(damage=14.97, hit_count=7, pvp_mod=0.55, pve_crit_rate=1, air_attack=True),
)

# --------------------------------------------------------------------


##====================================================================
############################## AWAKENING #############################
##====================================================================

# ----------------------------------------------------------------
Sacrum_Ferit = Skill(
    #''' Check reduced_on_cd_amount, .2 is placeholder '''
    id=6.503,
    class_id=6,
    name="Sacrum Ferit",
    acc_rate=0.05,
    hit1=Hit(
        damage=14.35,
        hit_count=3,
        pvp_mod=0.55,
        pve_crit_rate=1,
        reduced_on_cd_amount=0.2,
    ),
    hit2=Hit(
        damage=14.35,
        hit_count=3,
        pvp_mod=0.55,
        pve_crit_rate=1,
        reduced_on_cd_amount=0.2,
    ),
    hit3=Hit(
        damage=14.35,
        hit_count=3,
        pvp_mod=0.55,
        pve_crit_rate=1,
        reduced_on_cd_amount=0.2,
    ),
    reduced_on_cd=True,
)
# ---------------------------------------------------------------------

Luxem_Fluxum = Skill(
    id=6.504,
    class_id=6,
    name="Flow: Luxum Fluxum",
    acc_rate=Sacrum_Ferit.acc_rate,
    hit1=Hit(
        damage=Sacrum_Ferit.hit1["damage"],
        hit_count=7,
        pvp_mod=Sacrum_Ferit.hit1["pvp_mod"],
        reduced_pvp_hits=1,
    ),
)


# --------------------------------------------------------------------

Castigatio = Skill(
    id=6.507,
    class_id=6,
    name="Castigatio",
    acc_rate=0.08,
    hit1=Hit(damage=13.59, hit_count=3, pvp_mod=0.536, pve_crit_rate=0.5),
    hit2=Hit(damage=13.59, hit_count=3, pvp_mod=0.536, pve_crit_rate=0.5),
    hit3=Hit(damage=13.59, hit_count=4, pvp_mod=0.536, pve_crit_rate=0.5),
)

# ----------------------------------------------------------------

Verdict_Lancia_Iustitiae = Skill(
    id=6.510,
    class_id=6,
    name="Verdict: Lancia Iustitiae",
    acc_rate=0.08,
    hit1=Hit(
        damage=12.42, hit_count=6, pvp_mod=0.597, pve_crit_rate=1, pvp_crit_rate=1
    ),
    hit2=Hit(
        damage=13.57,
        hit_count=10,
        pvp_mod=0.68,
        pve_crit_rate=1,
        pvp_crit_rate=1,
        air_attack=True,
    ),
)

# ---------------------------------------------------------------------

Hastiludium = Skill(
    id=6.508,
    class_id=6,
    name="Hastiludium",
    acc_rate=0,
    hit1=Hit(damage=10.24, hit_count=3, pvp_mod=0.219),
    hit2=Hit(
        damage=11.91, hit_count=3, pvp_mod=0.578, pve_crit_rate=1, pvp_crit_rate=1
    ),
)


# ----------------------------------------------------------------

Sanctitas_de_Enslar = Skill(
    id=6.513,
    class_id=6,
    name="Sanctitas de Enslar",
    acc_rate=0,
    hit1=Hit(damage=15.88, hit_count=1, pvp_mod=0.45, pve_crit_rate=1, pvp_crit_rate=1),
    hit2=Hit(
        damage=15.88,
        hit_count=5,
        pvp_mod=0.45,
        pve_crit_rate=1,
        pvp_crit_rate=1,
        reduced_pvp_hits=2,
    ),
)


# ----------------------------------------------------------------

Purificatione = Skill(
    #''' Check reduced_on_cd_amount, .2 is placeholder '''
    id=6.505,
    class_id=6,
    name="Purificatione",
    acc_rate=0.5,
    hit1=Hit(damage=7.28, hit_count=1, pvp_mod=0),
    hit2=Hit(damage=10.96, hit_count=3, pvp_mod=0, reduced_on_cd_amount=0.2),
    reduced_on_cd=True,
)

# ----------------------------------------------------------------

Blitz_Stab = Skill(
    id=6.520,
    class_id=6,
    name="Blitz Stab",
    acc_rate=0,
    hit1=Hit(damage=14.09, hit_count=6, pvp_mod=0.65, pve_crit_rate=1, pvp_crit_rate=1),
)

# ----------------------------------------------------------------

Terra_Sancta = Skill(
    id=6.521,
    class_id=6,
    name="Terra Sancta",
    acc_rate=0,
    hit1=Hit(damage=16.96, hit_count=6, pvp_mod=0.198, pve_crit_rate=1),
)


# ----------------------------------------------------------------

##====================================================================
############################## Rabams #############################
##====================================================================

Celestial_Smite = Skill(
    id=6.902,
    class_id=6,
    name="Celestial Smite",
    acc_rate=0,
    hit1=Hit(
        damage=13.52, hit_count=3, pvp_mod=0.16, pve_crit_rate=0.8, pvp_crit_rate=0.8
    ),
)
