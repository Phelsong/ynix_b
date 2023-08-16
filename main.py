import os
from typing import Any

# libs
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# imports
from models import Float_Id, Int_Id, Attacker_Model, Defender_Model
from functions.calc_v5 import the_calc
from db.queries import (
    get_class_basic_skills_query,
    get_class_list_query,
    get_class_query,
    get_class_skills_query,
    get_skill_details_query,
    get_zone_list_query,
    get_zone_query,
)


# =============================================================================
app = FastAPI()
# -----------------------------------------------------------------------------
origins: list[str] = [
    "http://localhost",
    "http://127.0.0.1",
]
app.add_middleware(
    middleware_class=CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"Server Status": "You've got Py"}


# -----------------------------------------------------------------------------


@app.get("/class/{class_id}")
async def get_class(class_id):
    [data] = get_class_query(class_id=class_id)
    return data


# -----------------------------------------------------------------------------


@app.get("/class/{class_id}/skill_list")
def get_class_skill_list(class_id) -> list[dict[str, Any]]:
    skill_list: list[dict[str, Any]] = get_class_skills_query(class_id=class_id.id)
    return skill_list


# -----------------------------------------------------------------------------


@app.get("/class/{skill_id}")
async def get_class_skill(skill_id):
    [skill] = get_skill_details_query(skill_id)
    return skill["skill_details"]


# -----------------------------------------------------------------------------


@app.put("/basic_calc")
async def basic_calc(
    attacker_in: Attacker_Model,
    defender_in: Defender_Model,
    skill_id: Float_Id,
):
    [skill] = get_skill_details_query(skill_id.id)
    return the_calc.simulate_damage(attacker_in, defender_in, skill["skill_details"])


# ------------------------------------------------------------------------------


@app.get("/zones")
def get_zone_list() -> list[dict[str, Any]]:
    data = get_zone_list_query()
    return data


# ------------------------------------------------------------------------------


@app.get("/zones/{zone_id}")
async def get_zone_info(zone_id) -> dict[str, Any]:
    [data] = get_zone_query(zone_id)
    return data


# ------------------------------------------------------------------------------
server_config = uvicorn.Config(
    "main:app",
    host="::",
    port=(8321),
    reload=True if os.getenv("ENVIRONMENT") == "dev" else False,
)
server = uvicorn.Server(server_config)
if __name__ == "__main__":
    server.run()

#
