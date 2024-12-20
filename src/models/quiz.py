from database.db import database

class Question(database.Model):
    __tablename__ = 'questions'

    id = database.Column(database.Integer, primary_key=True)
    question_text = database.Column(database.String(255), nullable=False)
    options = database.relationship('Option', backref='question', lazy=True)

class Option(database.Model):
    __tablename__ = 'options'

    id = database.Column(database.Integer, primary_key=True)
    question_id = database.Column(database.Integer, database.ForeignKey('questions.id'), nullable=False)
    option_text = database.Column(database.String(255), nullable=False)
    is_correct = database.Column(database.Boolean, default=False)