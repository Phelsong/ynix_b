import pandas as pd
from pandas import DataFrame

# ----------------------------------------------------------------------------


class Zone:
    """Zone template for DB entry. Stuctured to Throw soft errors for invalid data intentional"""

    def __init__(
        self,
        name,
        *,
        id: int = 9999,  #! type:ignore
        recommended_ap: int = 9999,
        region: str = "todo",
        dr: int = 0,
        dr_breakpoint: int = 0,
        mob_type: str = "monster",
        ap_cap: int = 1000,
        dr_cap_mod: float = 0.7,
        evasion: int = 0,
    ) -> None:
        self.name: str = name
        self.id: int = id
        self.mob_type: str = mob_type
        self.region: str = region
        self.recommended_ap: int = recommended_ap
        self.dr_breakpoint: int = dr_breakpoint
        self.ap_cap: int = ap_cap
        self.dr: int = dr
        self.dr_cap_mod: float = dr_cap_mod
        self.evasion: int = evasion
        zone_list.setdefault(self.name, self)


# =======================================================
zone_list: dict[str, Zone] = {}

# ================================================================

solo: DataFrame = pd.read_csv("X:/0.code/ynix_b/data/PvE/solo_spots.csv")
party: DataFrame = pd.read_csv("X:/0.code/ynix_b/data/PvE/party_spots.csv")
spots: DataFrame = pd.merge(solo, party, how="outer")
spots.sort_values(by="Recommended", inplace=True, ignore_index=True)


for idx, row in spots.iterrows():
    Zone(
        name=row["Grindspot"],
        id=idx + 1,  # type: ignore
        mob_type=row["Mob_Type"],
        recommended_ap=row["Recommended"],
        dr_breakpoint=row["DR_Breakpoint"],
        dr=row["Actual_Mob_DR"],
        ap_cap=row["AP_Cap"],
        dr_cap_mod=row["Modifier"],
    )
