import psycopg
import os
from dotenv import dotenv_values
from psycopg.rows import dict_row


# ----------------------------------------------------------------
config = dotenv_values("./.env")


my_user = os.environ.get("USER_NAME") if os.environ.get("USER_NAME") != None else config["USER_NAME"]
my_pass = config["PASS_WORD"] if config["PASS_WORD"] != None else None
lab_db = config["LAB_DB"] if config["LAB_DB"] != None else None
lab_db_port = config["LAB_DB_PORT"] if config["LAB_DB_PORT"] != None else "5432"
lab_db_server = os.environ.get("DATABASE_URL") if os.environ.get("DATABASE_URL") != None else config["LAB_DB_SERVER"]



# ----------------------------------------------------------------
conn = psycopg.connect(
    hostaddr=lab_db_server,
    port=lab_db_port,
    dbname=lab_db,
    user=my_user,
    password=my_pass,
    row_factory=dict_row,
)
alt_conn = psycopg.connect(
    hostaddr=lab_db_server,
    port=lab_db_port,
    dbname=lab_db,
    user=my_user,
    password=my_pass,
)
alt_cur = alt_conn.cursor()
cur = conn.cursor()
