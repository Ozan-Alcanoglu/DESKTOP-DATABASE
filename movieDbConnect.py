import mysql.connector
import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv(dotenv_path='.env')

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

moviedb=mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    database=DB_NAME,  
    password=DB_PASSWORD  
)
