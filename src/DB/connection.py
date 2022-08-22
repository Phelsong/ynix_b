import psycopg
import os
from dotenv import dotenv_values
from psycopg.rows import dict_row


# ----------------------------------------------------------------
config = dotenv_values("./.env")

# my_user = config["USER_NAME"] if  len(config) != 0 else os.environ.get("USER_NAME")
# my_pass = config["PASS_WORD"] if len(config) != 0 else None
# lab_db = config["LAB_DB"] if len(config) != 0 else None
# lab_db_port = config["LAB_DB_PORT"] if len(config) != 0 else None
# lab_db_server = config["LAB_DB_SERVER"] if len(config) != 0 else os.environ.get("DATABASE_URL")



# ----------------------------------------------------------------
conn = psycopg.connect(
    hostaddr= config["LAB_DB_SERVER"] if len(config) != 0 else os.environ.get("DATABASE_URL"),
    port=config["LAB_DB_PORT"] if len(config) != 0 else None,
    dbname=config["LAB_DB"] if len(config) != 0 else None,
    user=config["USER_NAME"] if  len(config) != 0 else os.environ.get("USER_NAME"),
    password=config["PASS_WORD"] if len(config) != 0 else None,
    row_factory=dict_row,
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
