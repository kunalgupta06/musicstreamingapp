from flask import request, jsonify
from models import User
from database import db
from flask_restful import Resource
from config import Config

class Usersignup(Resource):
    def get(self):
        return jsonify({'message':'Nothing'})
    

    def post(self):
        data=request.get_json()
        print("data=try",data)
        user=User.query.filter_by(user_email=data['email']).first()
        print(user)
        if user:
            return jsonify({'message': 'User Already Exist! Please use different E-Mail id.'})
        newuser = User(user_email=data['email'],user_name=data['user_name'],password=data['password'],role=data['role'])
        db.session.add(newuser)
        db.session.commit()
        if data['role']=='creator':
            return jsonify({'message':'New Creator Created!!'})
        return jsonify({'message':'New User Created!!'})
        
class Userlogin(Resource):
    def get(self):
        return jsonify({'message':'Nothing'})
    def post(self):
        return jsonify({'message':'Welcome to Musicoholic!!'})        