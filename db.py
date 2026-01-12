# all database access goes through this file

import mysql.connector
from config import DB_config

def get_connection():
    return mysql.connector.connect(**DB_config)
