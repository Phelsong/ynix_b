import json

# ----------------------------------------------------------------
from db.connection import conn, cur

# ----------------------------------------------------------------

test = "test"

def get_class_list_query():
    cur.execute("""SELECT * FROM classes""")
    return cur.fetchall()


# ----------------------------------------------------------------


def get_class_query(class_id):
    cur.execute(
        """SELECT * FROM classes
                WHERE class_id= %s ;""",
        (class_id,),
    )
    return cur.fetchall()


# -----------------------------------------------------------------
def get_zone_list_query():
    cur.execute("""SELECT * FROM zones""")
    return cur.fetchall()


# ----------------------------------------------------------------
def get_zone_query(zone_id):
    cur.execute(
        """SELECT * FROM zones
                WHERE zone_id = %s ; """,
        (zone_id,),
    )
    return cur.fetchall()


# ----------------------------------------------------------------
def get_class_skills_query(class_id):
    cur.execute(
        """SELECT * FROM class_skills
                WHERE class_id = %s;""",
        (class_id,),
    )
    return cur.fetchall()


# ----------------------------------------------------------------
def get_skill_details_query(skill_id):
    cur.execute(
        """ SELECT skill_details from class_skills
                WHERE skill_id = %s::float4;""",
        (skill_id,),
    )
    return cur.fetchall()


# ----------------------------------------------------------------
def get_class_basic_skills_query(class_id):
    cur.execute(
        """SELECT * FROM class_skills WHERE skill_id = %s::float4;""",
        (class_id + 0.01,),
    )
    return cur.fetchall()


# ----------------------------------------------------------------
conn.commit()
