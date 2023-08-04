import os

import psycopg as ppg
from psycopg import Connection, Cursor
from psycopg.rows import dict_row

import tomllib


# ----------------------------------------------------------------
try:
    with open("X:/0.code/ynix_b/db/env.toml", "rb") as f:
        data: dict = tomllib.load(f)
        config: dict[str, str | int] = data["DB_ENV"]
except ValueError as e:
    print(e)

# ----------------------------------------------------------------
conn: Connection = ppg.connect(
    hostaddr=config["LAB_DB_SERVER"],
    port=config["LAB_DB_PORT"],
    dbname=config["LAB_DB_NAME"],
    user=config["USER_NAME"],
    password=config["PASS_WORD"],
    row_factory=dict_row,
)

cur: Cursor = conn.cursor()
