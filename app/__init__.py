# app/__init__.py
import psycopg2
import os

def get_connection():
    return psycopg2.connect(
        dbname="mydb",
        user="myuser",
        password="mypassword",
        host="db",  # هذا اسم الخدمة في docker-compose
        port="5432"
    )
