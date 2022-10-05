# --------------------------------------------------------------------------------
class Class:
    def __init__(self, id, name, dr, evasion):
        self.id = id
        self.name = name
        self.dr = dr
        self.evasion = evasion
        self.species = "human"
        class_list.setdefault(self.name, self)
        # self.skills = {}


# --------------------------------------------------------------------------------
# id = class ID xx = pre | 3xx = prime | 5xx = awk | 9xx = rabams
class Skill:
    def __init__(
        self,
        id,
        class_id,
        name,
        acc_rate,
        hit1,
        hit2=None,
        hit3=None,
        hit4=None,
        hit5=None,
        hit6=None,
        reduced_on_cd=False,
    ):
        self.id = id
        self.class_id = class_id
        self.name = name
        self.acc_rate = acc_rate
        self.hit1 = hit1.__dict__ if hit1 is not None else None
        self.hit2 = hit2.__dict__ if hit2 is not None else None
        self.hit3 = hit3.__dict__ if hit3 is not None else None
        self.hit4 = hit4.__dict__ if hit4 is not None else None
        self.hit5 = hit5.__dict__ if hit5 is not None else None
        self.hit6 = hit6.__dict__ if hit6 is not None else None
        self.reduced_on_cd = reduced_on_cd
        skill_list.setdefault(self.name, self)


class Hit:
    def __init__(
        self,
        damage,
        hit_count,
        pvp_mod,
        pve_crit_rate=0,
        pvp_crit_rate=0,
        reduced_on_cd_amount=None,
        reduced_pvp_hits=None,
        down_attack=True,
        air_attack=False,
    ):
        self.damage = damage
        self.hit_count = hit_count
        self.pvp_mod = pvp_mod
        self.pve_crit_rate = pve_crit_rate
        self.pvp_crit_rate = pvp_crit_rate
        self.reduced_on_cd_amount = reduced_on_cd_amount
        self.reduced_pvp_hits = reduced_pvp_hits
        self.down_attack = down_attack
        self.air_attack = air_attack


# ------------------------------------------------------------------------------

class_list = {}
skill_list = {}

from .Archer import *
from .Corsair import *
from .Dark_Knight import *
from .Drakania import *
from .Guardian import *
from .Hashashin import *
from .Kuno import *
from .Lahn import *
from .Maewha import *
from .Musa import *
from .Mystic import *
from .Ninja import *
from .Nova import *
from .Ranger import *
from .Sage import *
from .Shai import *
from .Sorceress import *
from .Striker import *
from .Tamer import *
from .Valkyrie import *
from .Warrior import *
from .Witch import *
from .Wizard import *

# list variables are for seed functions
# -------------------------------------------------------------------------------
