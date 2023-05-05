"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaa6fik728r886293lg-a.oregon-postgres.render.com",
        database="todo_o6io",
        user="root",
        password="SD4bFpbs3yn22QUnxvBj1Zf2OPU3EJBh")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
