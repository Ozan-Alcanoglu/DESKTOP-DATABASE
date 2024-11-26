import mysql.connector
import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv(dotenv_path='.env')

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

class Moviedb:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )

    def get_cursor(self):
        if self.connection.is_connected():
            return self.connection.cursor()
        else:
            print("Connection is not open")
            return None

    def close_connection(self):
        if self.connection.is_connected():
            self.connection.close()
