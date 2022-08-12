from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv
from sys import argv

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = argv[1]
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = argv[2]

db = SQLAlchemy(app)

import application.routes 

#pesronal access token - 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 
#python3 create.py mysql+pymysql://root:@34.105.248.63:3306/hackathon hdhhjsjsjrydjkyskykks