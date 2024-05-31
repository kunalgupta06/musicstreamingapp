from flask import Flask, request
from database import db
from config import Config
from flask_restful import Api
from flask_cors import CORS
from controllers.user_auth import Usersignup


app=Flask(__name__)

app.config.from_object(Config)
db.init_app(app)


api=Api(app)
CORS(app,resources={r'/*':{'origins':'*'}})

api.add_resource(Usersignup,'/user/signup')

api.add_resource(Userlogin,'/user/login')

if __name__ == '__main__':
    app.run(debug=True,use_reloader=True)