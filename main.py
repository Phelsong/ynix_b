import os

# libs
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# imports
from src.Attacker import Attacker
from src.Defender import Defender
from src.calc_v4 import *
from db.queries import *


# =============================================================================
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
    attacker = Attacker(attacker_in)
    defender = Defender(defender_in)
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
server_config = uvicorn.Config(
    "main:app",
    host="0.0.0.0",
    port=(os.environ.get("PORT") or 8000),
    reload=True if os.getenv["ENVIRONMENT"] == "dev" else False,
)
server = uvicorn.Server(server_config)
if __name__ == "__main__":
    server.run()

#
