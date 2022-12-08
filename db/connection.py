import os

import psycopg
from psycopg.rows import dict_row
import tomllib


# ----------------------------------------------------------------
with open("db\\env.toml", "rb") as f:
    data = tomllib.load(f)
    config = data["DB_ENV"]
# ----------------------------------------------------------------
conn = (
    psycopg.connect(
        hostaddr=config["LAB_DB_SERVER"],
        port=config["LAB_DB_PORT"],
        dbname=config["LAB_DB"],
        user=config["USER_NAME"],
        password=config["PASS_WORD"],
        row_factory=dict_row,
    )
    if len(data) != 0
    else psycopg.connect(conninfo=os.environ.get("DATABASE_URL"), row_factory=dict_row)
)
# alt_conn = psycopg.connect(
#     hostaddr=lab_db_server,
#     port=lab_db_port,
#     dbname=lab_db,
#     user=my_user,
#     password=my_pass,
# )
# alt_cur = alt_conn.cursor()
cur = conn.cursor()
