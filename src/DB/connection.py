import psycopg
from dotenv import dotenv_values
from psycopg.rows import dict_row

# ----------------------------------------------------------------
config = dotenv_values("../../.env")


my_user = config["USER_NAME"] if not None else "postgres"
my_pass = config["PASS_WORD"] if not None else None
lab_db = config["LAB_DB"] if True else "ynix-app"
lab_db_server = config["LAB_DB_SERVER"] if not None else config["DATABASE_URL"]
lab_db_port = config["LAB_DB_PORT"] if not None else '5432'

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
