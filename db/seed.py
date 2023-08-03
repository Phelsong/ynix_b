""" db seed"""
# libs
import ujson

# imports
from db.connection import conn, cur
from data.character_classes.class_data import class_list, skill_list
from data.pve_data import zone_list

# ----------------------------------------------------------------


def drop_tables():
    """drops existing tables"""
    cur.execute(
        """
                   DROP TABLE IF EXISTS zones;
                   DROP TABLE IF EXISTS class_skills;
                   DROP TABLE IF EXISTS class_data;
                   DROP TABLE IF EXISTS classes;
                   DROP TABLE IF EXISTS users;
                   """
    )


# ----------------------------------------------------------------
def create_tables():
    """creates new table structure"""
    cur.execute(
        """CREATE TABLE users
                    (user_id SERIAL PRIMARY KEY
                    , username varchar(100) NOT NULL,
                    password varchar(200))"""
    )
    cur.execute(
        """CREATE TABLE classes
                    (class_id INT PRIMARY KEY ,
                    class_name VARCHAR(150) NOT NULL)"""
    )
    cur.execute(
        """CREATE TABLE class_skills
                   (skill_id float4 PRIMARY KEY NOT NULL,
                   "class_id" INT REFERENCES classes(class_id) NOT NULL,
                   skill_name VARCHAR(200) NOT NULL,
                   skill_details JSON);
                   """
    )
    cur.execute(
        """CREATE TABLE class_data
                (class_id INT REFERENCES classes(class_id) NOT NULL,
                pvp_class_mods json);"""
    )
    cur.execute(
        """CREATE TABLE zones
                (zone_id INT PRIMARY KEY,
                zone_name VARCHAR(200) NOT NULL,
                mob_type VARCHAR(200) NOT NULL,
                region VARCHAR(200) NOT NULL,
                zone_recommended_ap INT NOT NULL,
                zone_dr_breakpoint INT NOT NULL,
                zone_dr INT NOT NULL,
                zone_ap_cap INT NOT NULL, 
                zone_dr_cap_mod float4 NOT NULL, 
                zone_evasion INT
                );"""
    )


# ----------------------------------------------------------------


def class_seed():
    """populates the database with initial data"""

    for char in class_list.values():
        cur.execute(
            """INSERT INTO classes (class_id, class_name)
                   VALUES (%s , %s )""",
            (char.id, char.name),
        )

    for skill in skill_list.values():
        details = ujson.dumps(skill.__dict__)
        cur.execute(
            """INSERT INTO class_skills (skill_id, class_id, skill_name, skill_details)
                    values (%s , %s, %s, %s)""",
            (skill.id, skill.class_id, skill.name, details),
        )


# ----------------------------------------------------------------
def zone_seed():
    """populates the database with initial data"""

    for zone in zone_list.values():
        cur.execute(
            """INSERT INTO zones (zone_id, zone_name, mob_type, region, zone_recommended_ap, zone_dr_breakpoint,  zone_dr, zone_ap_cap, zone_dr_cap_mod, zone_evasion)
                VALUES ( %s , %s , %s , %s , %s , %s, %s, %s, %s, %s )""",
            (
                zone.id,
                zone.name,
                zone.mob_type,
                zone.region,
                zone.recommended_ap,
                zone.dr_breakpoint,
                zone.dr,
                zone.ap_cap,
                zone.dr_cap_mod,
                zone.evasion,
            ),
        )


# ----------------------------------------------------------------
if __name__ == "__main__":
    drop_tables()
    create_tables()
    class_seed()
    zone_seed()
    conn.commit()
    conn.close()
# ----------------------------------------------------------------
