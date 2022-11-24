from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.secret_key = "super secret key"

currentDirectory = os.getcwd()
databasePath = os.path.join(currentDirectory, "database.db")

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + databasePath
#mysql:
#app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://user_name:password@IP:3306/db_name"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://jonat:best1234@192.168.1.150:3306/testingdb'   # 後端(flask)連結資料庫(mysql)
db = SQLAlchemy(app)
import routes, models

