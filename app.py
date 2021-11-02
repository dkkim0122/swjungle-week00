from flask import Flask
from flask import jsonify
from flask import request

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.week00

app.config["JWT_SECRET_KEY"] = "week00_team_6"
jwt = JWTManager(app)

# API를 여기 아래서부터 만들어주세요.



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)