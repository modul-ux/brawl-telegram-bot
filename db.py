import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS clubs (
    tag TEXT PRIMARY KEY,
    name TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS players (
    player_tag TEXT PRIMARY KEY,
    tg_username TEXT
)
""")

conn.commit()

def add_club(tag, name):
    cursor.execute(
        "INSERT OR IGNORE INTO clubs VALUES (?, ?)",
        (tag, name)
    )
    conn.commit()

def link_player(player_tag, tg_username):
    cursor.execute(
        "INSERT OR REPLACE INTO players VALUES (?, ?)",
        (player_tag, tg_username)
    )
    conn.commit()

def get_player_link(player_tag):
    cursor.execute(
        "SELECT tg_username FROM players WHERE player_tag = ?",
        (player_tag,)
    )
    return cursor.fetchone()
