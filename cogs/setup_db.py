from config import *
import mysql.connector

config = {
    'user': DB_USER,
    'password': DB_PASSWORD,
    'host': DB_HOST
    # 'database': DB_NAME
}

db = mysql.connector.connect(**config)
cursor = db.cursor(buffered=True)
