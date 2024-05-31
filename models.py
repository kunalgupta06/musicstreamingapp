from database import db
class Admin(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    admin_name=db.Column(db.String(50),nullable=False,default='kunal1')
    admin_email=db.Column(db.String(50),nullable=False,default='kunalg2022@gmail.com')
    password=db.Column(db.String(50),nullable=False,default='spotify')
    role=db.Column(db.String(50),nullable=False,default='admin')
class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    user_name=db.Column(db.String(50),nullable=False, unique=False)
    user_email=db.Column(db.String(50),nullable=False, unique=False)
    password=db.Column(db.String(50),nullable=False)
    role=db.Column(db.String(50),nullable=False)



    

