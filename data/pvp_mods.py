import pandas as pd

# ----------------------------------------------------------------------------


class ClassMod:
    """Class vs Class PvP Modifiers
    https://www.naeu.playblackdesert.com/en-US/Wiki?wikiNo=225"""

    def __init__(self, name: str, *, classes):
        self.name = name
        class_mods.setdefault(self.name, self)


# ============================================================================

class_mods: dict[str, ClassMod] = {}


warrior_mods = pd.read_csv("X:/0.code/ynix_b/data/PvP/warrior_vs.csv")


for idx, row in warrior_mods.iterrows():
    ClassMod(name="warrior")
