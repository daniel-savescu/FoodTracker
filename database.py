from flask import g
import sqlite3
def connect_db():
    sql = sqlite3.connect('E:\\Python\\Flask Projects\\Flask_Food_Tracker\\food_log.db')
    sql.row_factory = sqlite3.Row
    return sql

def get_db():
    if not hasattr(g, 'sqlite3_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db