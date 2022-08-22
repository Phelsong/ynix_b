from .class_data import Class, Hit, Skill

#----------------------------------------------------------------
archer = Class(id=17, name="Archer", dr=0, evasion=0)
# id = class ID xx = pre | 3xx = prime | 5xx = awk | 9xx = rabams
Spirit_Arrow_X = Skill(id=17.01, class_id=17, name="Spirit Arrow X",  acc_rate=.28,
                   hit1=Hit(damage=8.14, hit_count=1, pvp_mod=0))
#----------------------------------------------------------------
Spirit_Arrow = Skill(id=17.1, class_id=17, name="Spirit Arrow",  acc_rate=.28,
                   hit1=Hit(damage=8.14, hit_count=1, pvp_mod=0))
#----------------------------------------------------------------