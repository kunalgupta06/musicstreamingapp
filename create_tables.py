from app import app
from database import db
from models import Admin
from flask_migrate import Migrate
migrate=Migrate(app,db)
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        admin=Admin.query.first()
        if not admin:
            admin=Admin(admin_name='kunal',admin_email='kunalg2022@gmail.com',password='spotify')
            db.session.add(admin)
            db.session.commit()


            