from flask import Flask
from flask_cors import CORS
import pymysql
from dbconfig.dbconfig import config



app = Flask(__name__)
CORS(app)

db = pymysql.connect(
    config["DB_HOST"], config["DB_USERNAME"], config["DB_PASSWORD"], config["DB_NAME"])


cursor = db.cursor()

if cursor:
    print(" DB connect successfully")
