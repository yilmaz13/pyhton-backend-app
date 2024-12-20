from flask_sqlalchemy import SQLAlchemy

database = SQLAlchemy()

def init_db(app):
    database.init_app(app)
    with app.app_context():
        database.create_all()