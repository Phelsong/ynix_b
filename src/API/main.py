import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn


from __init__ import * 
# from calc import *
from alt_calc import *

# -----------------------------------------------------------------------------
app = FastAPI()
# -----------------------------------------------------------------------------
origins = [
    "http://localhost",
    "http://localhost:3000",
    "https://localhost:3000",
    "http://127.0.0.1",
    "http://ynix-b.herokuapp.com", 
    "https://ynix-b.herokuapp.com",
]   
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------


@app.get("/api")
def health_check():
    return {"Server Status": "You've got Py"}
# -----------------------------------------------------------------------------


@app.get("/class/{class_id}")
async def get_class(class_id):
    [data] = get_class_query(class_id)
    return data
# -----------------------------------------------------------------------------


@app.get("/class/{class_id}/skill_list")
def get_class_skill_list(class_id):
    skill_list = get_class_skills_query(class_id)
    return skill_list
# -----------------------------------------------------------------------------


@app.get("/class/{class_id}/{skill_id}")
async def get_class_skill(class_id, skill_id):
    [skill] = get_skill_details_query(skill_id)
    return skill["skill_details"]

# -----------------------------------------------------------------------------


@app.put("/basic_calc")
async def basic_calc(attacker_in: dict, defender_in: dict, skill_id: tuple):
    attacker = Attacker(attacker_in['class_id'],
                        attacker_in['ap'],
                        attacker_in['aap'],
                        attacker_in['acc'],
                        attacker_in['acc_rate'],
                        attacker_in['crit_rate'],
                        attacker_in['monster_ap'],
                        attacker_in['kama_damage'],
                        attacker_in['demi_damage'],
                        attacker_in['human_damage'],
                        attacker_in['other_damage'],
                        attacker_in['crit_damage'],
                        attacker_in['back_damage'],
                        attacker_in['down_damage'],
                        attacker_in['air_damage'],
                        attacker_in['ap_combat_buffs'],
                        attacker_in['crit_combat_buffs'],
                        attacker_in['ap_debuffs'],
                        attacker_in['acc_combat_buffs'],
                        attacker_in['acc_debuffs'],
                        attacker_in['human_damage_debuffs'])
    defender = Defender(defender_in['dr'],
                        defender_in['dr_rate'],
                        defender_in['evasion'],
                        defender_in['evasion_rate'],
                        defender_in['dr_combat_buffs'],
                        defender_in['dr_debuffs'],
                        defender_in['evasion_combat_buffs'],
                        defender_in['evasion_debuffs'],
                        defender_in['class_id'],
                        defender_in['species'])
    [skill] = get_skill_details_query(skill_id[0])
    calc = Calc(attacker, defender, skill["skill_details"])
    return calc.run_calc()
# ------------------------------------------------------------------------------


@app.get("/zones")
def get_zone_list():
    data = get_zone_list_query()
    return data

# ------------------------------------------------------------------------------


@app.get("/zones/{zone_id}")
async def get_zone_info(zone_id):
    [data] = get_zone_query(zone_id)
    return data

# ------------------------------------------------------------------------------

if __name__ == "__main__":
    config = uvicorn.Config("main:app", host="0.0.0.0", port=(os.environ.get("PORT") or "8000"), log_level="info",)
    server = uvicorn.Server(config)
    server.run()

#