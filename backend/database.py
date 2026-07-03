import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "database", "users.db")

connection = sqlite3.connect(
    DB_PATH,
    check_same_thread=False
)

cursor = connection.cursor()


cursor.execute("""

CREATE TABLE IF NOT EXISTS users(

id INTEGER PRIMARY KEY AUTOINCREMENT,

name TEXT,

age INTEGER,

gender TEXT,

height REAL,

weight REAL,

goal TEXT,

bmi REAL,

calories INTEGER,

protein INTEGER,

carbs INTEGER,

fats INTEGER,

water REAL

)

""")

connection.commit()


def save_user(data):

    cursor.execute("""

    INSERT INTO users(

    name,

    age,

    gender,

    height,

    weight,

    goal,

    bmi,

    calories,

    protein,

    carbs,

    fats,

    water

    )

    VALUES(?,?,?,?,?,?,?,?,?,?,?,?)

    """,

    (

    data["name"],

    data["age"],

    data["gender"],

    data["height"],

    data["weight"],

    data["goal"],

    data["bmi"],

    data["calories"],

    data["protein"],

    data["carbs"],

    data["fats"],

    data["water"]

    )

    )

    connection.commit()