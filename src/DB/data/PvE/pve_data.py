#----------------------------------------------------------------------------
zone_list = {}
class Zone:
    def __init__(self, id, name, region, dr, evasion, mob_type):
        self.id = id
        self.name = name
        self.region = region
        self.dr = dr
        self.evasion = evasion
        self.mob_type = mob_type
        zone_list.setdefault(self.name, self)

#--------------------------------------------------------------------------
centaurus_herd = Zone(15, "Centaurus Herd", "Valencia", 340, 0, "demihuman")

# castle_ruins_elvia = Zone(34, "Elvia - Castle Ruins", "Serendia", 0, 0, "human")


tunkuta = Zone(44, "Turos", "O'dyllita", 460, 0, "kamasylvian")
elvia_fogans = Zone(65, "Elvia - Fogans", "Calpheon", 480, 0, "other")
elvia_orcs = Zone(75, "Elvia - Orcs", "Calpheon", 640, 0, "demihuman") #lights are -130dr

gyfin_underground = Zone(96, "Gyfin Underground", "Kamasylvia", 600, 0, "kamasylvian")
olun_valley = Zone(97, "Olun Valley", "O'dyllita", 490, 0, "kamasylvian")
elvia_hexe_sanctuary = Zone(98, "Elvia - Hexe Sanctuary", "Calpheon", 800, 0, "other")
crypt_of_resting_thoughts = Zone(99, "Crypt of Resting Thoughts", "Kamasylvia", 465, 0, "kamasylvian") # soft_ap cap at: 300? - damage
elvia_quint_hill = Zone(100, "Elvia - Quint Hill", "Calpheon", 800, 0, "demihuman") #?
elvia_saunels = Zone(82, "Elvia - Saunels", "Calpheon", 630, 0, "demihuman")
elvia_giants = Zone(84, "Elvia - Giants", "Calpheon", 695, 0, "human") # alt 730?

#new math verified
manshaum_forest = Zone(33, "Manshaum Forest", "Kamasylvia", 363, 0, "kamasylvian") # 420-430? soft_ap cap at: 300? - damage
thornwood_forest = Zone(35, "Thornwood Forest", "O'dyllita", 395, 0, "kamasylvian") # soft_ap cap at: 300? - damage