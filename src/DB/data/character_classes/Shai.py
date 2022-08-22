from .class_data import Class, Hit, Skill

#----------------------------------------------------------------
shai = Class(id=18, name="Shai", dr=23, evasion=0)
# id = class ID xx = pre | 3xx = prime | 5xx = awk | 9xx = rabams
# ----------------------------------------------------------------
Swing_Swing_X = Skill(id=18.01, class_id=18, name="Swing Swing X", acc_rate=.11,
                    hit1=Hit(damage=16.63, hit_count=2, pvp_mod=0.2),
                    hit2=Hit(damage=16.63, hit_count=2, pvp_mod=0.2),                               
                    hit3=Hit(damage=16.63, hit_count=2, pvp_mod=0.2),
                    hit4=Hit(damage=16.63, hit_count=2, pvp_mod=0.2))
# ------------------------------------------------------------------
Twirl = Skill(id=18.2, class_id= 18, name="Twirl", acc_rate=.09,
              hit1=Hit(damage=6.12, hit_count=26, pvp_mod=0.333),
              hit2=Hit(damage=6.12, hit_count=35, pvp_mod=0.333))
# -------------------------------------------------------------------
Go_Away = Skill(id=18.3, class_id=18, name="Go Away", acc_rate=.12,
                hit1=Hit(damage=7.91, hit_count=3, pvp_mod=0.1))
# ---------------------------------------------------------------------
One_Two_Three = Skill(id=18.4, class_id=18, name="One-Two-Three", acc_rate=.11,
                      hit1=Hit(damage=7.44, hit_count=29, pvp_mod=0.218),
                      hit2=Hit(damage=7.44, hit_count=27, pvp_mod=0.218),
                      hit3=Hit(damage=7.13, hit_count=37, pve_crit_rate=.5, pvp_mod=0.237))
#----------------------------------------------------------------------
Go = Skill(id=18.5, class_id=18, name="Go!", acc_rate=.11, 
           hit1=Hit(damage=7.13, hit_count=40, pvp_mod=0.237))
# ---------------------------------------------------------------------
Kwik_Two = Skill(id=18.6, class_id=18, name="Kwik Two", acc_rate=.07,
                 hit1=Hit(damage=8.82, hit_count=39, pvp_mod=0.112))
#----------------------------------------------------------------------
Twirl_Three = Skill(id=18.7, class_id=18, name="Twirl Three", acc_rate=.15, 
                    hit1=Hit(damage=8.21, hit_count=8, pvp_mod=0.2),
                    hit2=Hit(damage=8.21, hit_count=40, pvp_mod=0.2))
#----------------------------------------------------------------------
Eat_This = Skill(id=18.8, class_id=18, name="Eat This!", acc_rate=.05,
                 hit1=Hit(damage=14.52, hit_count=4, pve_crit_rate=1, pvp_mod=0.2))
# ---------------------------------------------------------------------
Hop_Three = Skill(id=18.9, class_id=18, name="Hop-Three", acc_rate=.05,
                  hit1=Hit(damage=8.12, hit_count=36, pvp_mod=.112))
#----------------------------------------------------------------------
Try_This = Skill(id=18.11, class_id=18, name="Try This!", acc_rate=.1, 
                 hit1=Hit(damage=11.22, hit_count=14, pve_crit_rate=1, pvp_mod=.091))
#----------------------------------------------------------------------
Forests_Echo = Skill(id=18.57, class_id=18, name="Forest's Echo", acc_rate=.5, 
                     hit1=Hit(damage=13.12, hit_count=16, pvp_mod=.3))
#----------------------------------------------------------------------
Suns_Fury = Skill(id=18.58, class_id=18, name="Sun's Fury", acc_rate=.5,
                  hit1=Hit(damage=13.12, hit_count=7, pvp_mod=.3))
#----------------------------------------------------------------------
Earths_Tremble = Skill(id=18.59, class_id=18, name="Earth's Tremble", acc_rate=.5, 
                       hit1=Hit(damage=12.04, hit_count=7, pvp_mod=.3))
#----------------------------------------------------------------------
Twirl_Boom = Skill(id=18.93, class_id=18, name="Twirl-Boom!", acc_rate=.05, hit1=Hit(damage=18.38, hit_count=7, pve_crit_rate=1, pvp_crit_rate=.25, pvp_mod=.5))
#----------------------------------------------------------------------