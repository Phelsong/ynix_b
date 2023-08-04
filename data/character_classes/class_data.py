# --------------------------------------------------------------------------------
from typing import Any


class Class:
    def __init__(self, id, name, dr, evasion) -> None:
        self.id: int = id
        self.name: str = name
        self.dr: int = dr
        self.evasion: int = evasion
        self.species: str = "human"
        class_list.setdefault(self.name, self)
        # self.skills = {}


# --------------------------------------------------------------------------------
class Hit:
    def __init__(
        self,
        damage: float,
        hit_count: int,
        pvp_mod: float,
        pve_crit_rate: float = 0,
        pvp_crit_rate: float = 0,
        reduced_on_cd_amount: float = None,
        reduced_pvp_hits: int = None,
        down_attack: bool = True,
        air_attack: bool = False,
    ) -> None:
        self.damage: float = damage
        self.hit_count: int = hit_count
        self.pvp_mod: float = pvp_mod
        self.pve_crit_rate: float = pve_crit_rate
        self.pvp_crit_rate: float = pvp_crit_rate
        self.reduced_on_cd_amount: float | None = reduced_on_cd_amount
        self.reduced_pvp_hits: int | None = reduced_pvp_hits
        self.down_attack: bool = down_attack
        self.air_attack: bool = air_attack


# --------------------------------------------------------------------------------

# id = class ID xx = pre | 3xx = prime | 5xx = awk | 9xx = rabams
class Skill:
    def __init__(
        self,
        id: int | float,
        name: str,
        *,
        class_id: int,
        acc_rate: float,
        attack_count: int = 1,
        hit1: Hit,
        hit2: Hit | None = None,
        hit3: Hit | None = None,
        hit4: Hit | None = None,
        hit5: Hit | None = None,
        hit6: Hit | None = None,
        reduced_on_cd: bool = False,
    ) -> None:
        self.id: int | float = id
        self.class_id: int = class_id
        self.name: str = name
        self.acc_rate: float = acc_rate
        self.attack_count: int = attack_count
        self.hit1: dict = hit1.__dict__
        self.hit2: dict | None = hit2.__dict__ if hit2 is not None else None
        self.hit3: dict | None = hit3.__dict__ if hit3 is not None else None
        self.hit4: dict | None = hit4.__dict__ if hit4 is not None else None
        self.hit5: dict | None = hit5.__dict__ if hit5 is not None else None
        self.hit6: dict | None = hit6.__dict__ if hit6 is not None else None
        self.reduced_on_cd: bool = reduced_on_cd
        skill_list.setdefault(self.name, self)


# ------------------------------------------------------------------------------

class_list: dict = {}
skill_list: dict = {}

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
from .Woosa import *
from .Maegu import *

# list variables are for seed functions
# -------------------------------------------------------------------------------
