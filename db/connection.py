import os

import psycopg
from psycopg.rows import dict_row

import tomllib


# ----------------------------------------------------------------
try:
    with open("env.toml", "rb") as f:
        data = tomllib.load(f)
        config = data["DB_ENV"]
except ValueError as e:
    print(e)

# ----------------------------------------------------------------
conn = (
    psycopg.connect(
        hostaddr=config["LAB_DB_SERVER"],
        port=config["LAB_DB_PORT"],
        dbname=config["LAB_DB_NAME"],
        user=config["USER_NAME"],
        password=config["PASS_WORD"],
        row_factory=dict_row,
    )
    if data != None
    else psycopg.connect(conninfo=os.environ.get("DATABASE_URL"), row_factory=dict_row)
)

cur = conn.cursor()
